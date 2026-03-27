"""
Screenshot comparison utilities for visual regression testing.

Uses Pillow for pixel-level image comparison with configurable thresholds.
Generates diff images highlighting changed regions.
"""

from pathlib import Path

from PIL import Image, ImageChops, ImageDraw


def compare_screenshots(
    actual_path: Path,
    expected_path: Path,
    diff_path: Path | None = None,
    threshold: float = 0.1,
    pixel_threshold: int = 25,
) -> dict:
    """
    Compare two screenshots and return similarity metrics.

    Args:
        actual_path: Path to the actual (current) screenshot.
        expected_path: Path to the expected (baseline) screenshot.
        diff_path: Optional path to save a visual diff image.
        threshold: Maximum allowed mismatch ratio (0.0–1.0). Default 0.1 (10%).
        pixel_threshold: Per-channel delta below which a pixel is considered
            unchanged (0–255).  Accommodates antialiasing/subpixel rendering.

    Returns:
        dict with keys:
            - match (bool): True if images are within threshold.
            - mismatch_ratio (float): Fraction of pixels that differ.
            - mismatch_count (int): Number of differing pixels.
            - total_pixels (int): Total pixel count.
            - diff_path (Path | None): Path to the diff image if generated.
            - size_match (bool): Whether image dimensions match.
    """
    actual = Image.open(actual_path).convert("RGB")
    expected = Image.open(expected_path).convert("RGB")

    result: dict = {
        "match": False,
        "mismatch_ratio": 1.0,
        "mismatch_count": 0,
        "total_pixels": 0,
        "diff_path": None,
        "size_match": actual.size == expected.size,
    }

    if not result["size_match"]:
        # Different dimensions → automatic mismatch, but still try to diff
        # by resizing expected to actual size for the overlay.
        expected = expected.resize(actual.size, Image.LANCZOS)

    total_pixels = actual.size[0] * actual.size[1]
    result["total_pixels"] = total_pixels

    # Pixel-level comparison
    diff_img = ImageChops.difference(actual, expected)

    # Count pixels that exceed the per-channel threshold
    mismatch_count = 0
    diff_data = diff_img.getdata()
    for pixel in diff_data:
        if any(channel > pixel_threshold for channel in pixel):
            mismatch_count += 1

    mismatch_ratio = mismatch_count / total_pixels if total_pixels > 0 else 0.0
    result["mismatch_count"] = mismatch_count
    result["mismatch_ratio"] = mismatch_ratio
    result["match"] = mismatch_ratio <= threshold

    # Generate diff visualization if requested
    if diff_path is not None:
        diff_visual = _create_diff_overlay(actual, expected, pixel_threshold)
        diff_path.parent.mkdir(parents=True, exist_ok=True)
        diff_visual.save(str(diff_path))
        result["diff_path"] = diff_path

    return result


def _create_diff_overlay(
    actual: Image.Image,
    expected: Image.Image,
    pixel_threshold: int,
) -> Image.Image:
    """
    Create a side-by-side diff visualization.

    Layout: [ Expected | Actual | Diff Heatmap ]
    Changed pixels are highlighted in red on the diff panel.
    """
    w, h = actual.size

    # Build the diff heatmap
    diff_raw = ImageChops.difference(actual, expected)
    heatmap = Image.new("RGB", (w, h), (0, 0, 0))
    draw = ImageDraw.Draw(heatmap)

    diff_data = list(diff_raw.getdata())
    actual_data = list(actual.getdata())

    for i, (pixel, orig) in enumerate(zip(diff_data, actual_data)):
        x = i % w
        y = i // w
        if any(channel > pixel_threshold for channel in pixel):
            # Red highlight for changed pixels
            draw.point((x, y), fill=(255, 60, 60))
        else:
            # Dimmed original for unchanged pixels
            r, g, b = orig
            draw.point((x, y), fill=(r // 3, g // 3, b // 3))

    # Composite: expected | actual | diff
    canvas = Image.new("RGB", (w * 3 + 4, h + 20), (40, 40, 40))
    canvas.paste(expected, (0, 20))
    canvas.paste(actual, (w + 2, 20))
    canvas.paste(heatmap, (w * 2 + 4, 20))

    # Labels
    label_draw = ImageDraw.Draw(canvas)
    label_draw.text((w // 2 - 30, 2), "Expected", fill=(200, 200, 200))
    label_draw.text((w + 2 + w // 2 - 20, 2), "Actual", fill=(200, 200, 200))
    label_draw.text((w * 2 + 4 + w // 2 - 15, 2), "Diff", fill=(255, 100, 100))

    return canvas


def assert_screenshot_match(
    page,
    name: str,
    snapshot_dir: Path,
    *,
    update: bool = False,
    threshold: float = 0.1,
    pixel_threshold: int = 25,
    full_page: bool = False,
    selector: str | None = None,
    mask_selectors: list[str] | None = None,
    wait_ms: int = 500,
):
    """
    High-level assertion: take a screenshot and compare against baseline.

    Args:
        page: Playwright Page object.
        name: Snapshot name (without extension).
        snapshot_dir: Root directory for baseline/actual/diff images.
        update: If True, save the current screenshot as the new baseline.
        threshold: Mismatch tolerance (0.0–1.0).
        pixel_threshold: Per-channel pixel tolerance (0–255).
        full_page: Capture full scrollable page vs. viewport only.
        selector: Optional CSS selector to capture instead of full page.
        mask_selectors: List of CSS selectors to mask (paint over) before
            comparison — useful for dynamic content like timestamps.
        wait_ms: Milliseconds to wait before capturing (for animations).
    """
    baseline_dir = snapshot_dir / "baseline"
    actual_dir = snapshot_dir / "actual"
    diff_dir = snapshot_dir / "diff"

    baseline_dir.mkdir(parents=True, exist_ok=True)
    actual_dir.mkdir(parents=True, exist_ok=True)

    baseline_path = baseline_dir / f"{name}.png"
    actual_path = actual_dir / f"{name}.png"
    diff_path = diff_dir / f"{name}.png"

    # Wait for animations / layout to settle
    page.wait_for_timeout(wait_ms)

    # Mask dynamic content before capturing
    if mask_selectors:
        for sel in mask_selectors:
            page.evaluate(
                """(selector) => {
                    document.querySelectorAll(selector).forEach(el => {
                        el.style.visibility = 'hidden';
                    });
                }""",
                sel,
            )
        page.wait_for_timeout(100)

    # Capture screenshot
    screenshot_opts = {"path": str(actual_path), "full_page": full_page}
    if selector:
        element = page.locator(selector)
        element.screenshot(path=str(actual_path))
    else:
        page.screenshot(**screenshot_opts)

    # Update mode: save as baseline and return
    if update or not baseline_path.exists():
        import shutil

        shutil.copy2(actual_path, baseline_path)
        # Clean up old diff if it exists
        if diff_path.exists():
            diff_path.unlink()
        return  # No assertion in update mode

    # Compare
    result = compare_screenshots(
        actual_path=actual_path,
        expected_path=baseline_path,
        diff_path=diff_path,
        threshold=threshold,
        pixel_threshold=pixel_threshold,
    )

    if not result["match"]:
        pct = result["mismatch_ratio"] * 100
        msg = (
            f"Visual regression detected for '{name}': "
            f"{pct:.2f}% pixels changed ({result['mismatch_count']:,} / "
            f"{result['total_pixels']:,}), threshold={threshold * 100:.1f}%"
        )
        if result["diff_path"]:
            msg += f"\n  Diff image: {result['diff_path']}"
        msg += f"\n  Baseline:   {baseline_path}"
        msg += f"\n  Actual:     {actual_path}"
        msg += "\n  Run with --update-snapshots to accept the new baseline."
        raise AssertionError(msg)
