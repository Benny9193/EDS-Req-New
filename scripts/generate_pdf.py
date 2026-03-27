#!/usr/bin/env python3
"""
Generate formatted PDF files from Markdown documentation.

Creates visually polished PDF documents with:
- Cover pages with EDS branding
- Styled headers (H1, H2, H3)
- Formatted tables with shading
- Code blocks with monospace font
- Bulleted and numbered lists
- Table of contents

Usage:
    python scripts/generate_pdf.py
    python scripts/generate_pdf.py --file docs/SCHEMA.md
    python scripts/generate_pdf.py --output-dir docs/pdf
"""

import re
import os
import sys
from pathlib import Path
from datetime import datetime

from fpdf import FPDF
from fpdf.enums import XPos, YPos


# EDS Brand Colors (RGB tuples)
EDS_NAVY = (28, 26, 131)
EDS_DARK_BLUE = (26, 54, 93)
EDS_RED = (183, 12, 13)
CODE_BG = (245, 245, 245)
TABLE_HEADER_BG = (28, 26, 131)
TABLE_ALT_ROW = (245, 245, 245)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
LIGHT_GRAY = (200, 200, 200)


class EDSPdf(FPDF):
    """Custom PDF class with EDS styling."""

    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=25)
        self.set_margins(25, 25, 25)
        self.title_text = ''
        self.subtitle_text = ''

        # Add fonts
        self.add_font('DejaVu', '', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', uni=True)
        self.add_font('DejaVu', 'B', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', uni=True)
        self.add_font('DejaVu', 'I', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf', uni=True)
        self.add_font('DejaVuMono', '', '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', uni=True)

    def header(self):
        """Page header."""
        if self.page_no() > 1:
            self.set_font('DejaVu', 'I', 8)
            self.set_text_color(*GRAY)
            self.cell(0, 10, self.title_text, align='L')
            self.cell(0, 10, f'Page {self.page_no()}', align='R')
            self.ln(15)
            # Draw line
            self.set_draw_color(*LIGHT_GRAY)
            self.line(25, 20, self.w - 25, 20)

    def footer(self):
        """Page footer."""
        if self.page_no() > 1:
            self.set_y(-20)
            self.set_font('DejaVu', 'I', 8)
            self.set_text_color(*GRAY)
            self.set_draw_color(*LIGHT_GRAY)
            self.line(25, self.h - 25, self.w - 25, self.h - 25)
            self.cell(0, 10, 'EDS Universal Requisition System', align='C')

    def add_cover_page(self, title, subtitle=''):
        """Add a styled cover page."""
        self.title_text = title
        self.subtitle_text = subtitle
        self.add_page()

        # Background accent
        self.set_fill_color(*EDS_NAVY)
        self.rect(0, 0, self.w, 80, 'F')

        # Title
        self.set_y(100)
        self.set_font('DejaVu', 'B', 32)
        self.set_text_color(*EDS_NAVY)
        self.multi_cell(0, 15, title, align='C')

        # Subtitle
        if subtitle:
            self.ln(5)
            self.set_font('DejaVu', '', 14)
            self.set_text_color(*EDS_DARK_BLUE)
            self.multi_cell(0, 8, subtitle, align='C')

        # Horizontal line
        self.ln(20)
        self.set_draw_color(*EDS_NAVY)
        self.set_line_width(0.5)
        self.line(60, self.get_y(), self.w - 60, self.get_y())

        # Footer info
        self.set_y(self.h - 80)
        self.set_font('DejaVu', '', 11)
        self.set_text_color(*EDS_DARK_BLUE)
        self.cell(0, 8, 'EDS Universal Requisition System', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.set_font('DejaVu', '', 10)
        self.set_text_color(*GRAY)
        self.cell(0, 8, f'Generated: {datetime.now().strftime("%B %d, %Y")}', align='C')

    def add_h1(self, text):
        """Add Heading 1."""
        self.ln(8)
        self.set_x(25)
        self.set_font('DejaVu', 'B', 18)
        self.set_text_color(*EDS_NAVY)
        try:
            self.multi_cell(0, 10, text[:100])  # Limit length
        except Exception:
            self.cell(0, 10, text[:60], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)
        # Underline
        self.set_draw_color(*EDS_NAVY)
        self.set_line_width(0.3)
        y = self.get_y()
        self.line(25, y, self.w - 25, y)
        self.ln(6)

    def add_h2(self, text):
        """Add Heading 2."""
        self.ln(6)
        self.set_x(25)
        self.set_font('DejaVu', 'B', 14)
        self.set_text_color(*EDS_DARK_BLUE)
        try:
            self.multi_cell(0, 8, text[:100])
        except Exception:
            self.cell(0, 8, text[:60], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(3)

    def add_h3(self, text):
        """Add Heading 3."""
        self.ln(4)
        self.set_x(25)
        self.set_font('DejaVu', 'B', 12)
        self.set_text_color(*EDS_DARK_BLUE)
        try:
            self.multi_cell(0, 7, text[:100])
        except Exception:
            self.cell(0, 7, text[:60], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

    def add_h4(self, text):
        """Add Heading 4."""
        self.ln(3)
        self.set_x(25)
        self.set_font('DejaVu', 'B', 11)
        self.set_text_color(*BLACK)
        try:
            self.multi_cell(0, 6, text[:100])
        except Exception:
            self.cell(0, 6, text[:60], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1)

    def add_paragraph(self, text):
        """Add a regular paragraph with inline formatting."""
        self.set_font('DejaVu', '', 10)
        self.set_text_color(*BLACK)
        self.set_x(25)  # Reset X position

        # Handle inline formatting
        text = self.process_inline_formatting(text)

        # Handle very long lines by wrapping
        if len(text) > 500:
            text = text[:500] + '...'

        try:
            self.multi_cell(0, 6, text)
        except Exception:
            # Fallback for problematic text
            self.cell(0, 6, text[:80] + '...', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

    def process_inline_formatting(self, text):
        """Process inline markdown formatting."""
        # Remove inline code backticks (we'll handle separately)
        text = re.sub(r'`([^`]+)`', r'\1', text)
        # Remove bold markers
        text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
        text = re.sub(r'__([^_]+)__', r'\1', text)
        # Remove italic markers
        text = re.sub(r'\*([^*]+)\*', r'\1', text)
        text = re.sub(r'_([^_]+)_', r'\1', text)
        return text

    def add_bullet_item(self, text, level=0):
        """Add a bulleted list item."""
        indent = 25 + (level * 10)
        self.set_x(indent)
        self.set_font('DejaVu', '', 10)
        self.set_text_color(*BLACK)

        # Bullet character
        bullet = '-' if level == 0 else '>'
        text = self.process_inline_formatting(text)

        # Truncate very long items
        if len(text) > 200:
            text = text[:200] + '...'

        self.cell(8, 6, bullet)
        try:
            self.multi_cell(0, 6, text)
        except Exception:
            self.cell(0, 6, text[:60] + '...', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def add_numbered_item(self, number, text, level=0):
        """Add a numbered list item."""
        indent = 25 + (level * 10)
        self.set_x(indent)
        self.set_font('DejaVu', '', 10)
        self.set_text_color(*BLACK)

        text = self.process_inline_formatting(text)

        # Truncate very long items
        if len(text) > 200:
            text = text[:200] + '...'

        self.cell(10, 6, f'{number}.')
        try:
            self.multi_cell(0, 6, text)
        except Exception:
            self.cell(0, 6, text[:60] + '...', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def add_code_block(self, code, language=''):
        """Add a code block with background."""
        self.ln(3)
        self.set_x(25)

        # Background
        self.set_fill_color(*CODE_BG)
        self.set_font('DejaVuMono', '', 8)
        self.set_text_color(*BLACK)

        lines = code.split('\n')

        # Limit lines for very long code blocks
        if len(lines) > 50:
            lines = lines[:50] + ['... (truncated)']

        start_y = self.get_y()

        # Calculate height needed
        line_height = 5
        block_height = min(len(lines) * line_height + 10, 200)  # Cap height

        # Check if we need a page break
        if self.get_y() + block_height > self.h - 30:
            self.add_page()
            start_y = self.get_y()

        # Draw background
        self.set_fill_color(*CODE_BG)
        self.rect(25, start_y, self.w - 50, block_height, 'F')

        # Draw border
        self.set_draw_color(*LIGHT_GRAY)
        self.rect(25, start_y, self.w - 50, block_height, 'D')

        self.set_y(start_y + 5)
        self.set_x(30)

        for line in lines:
            if self.get_y() > self.h - 30:
                self.add_page()
                self.set_x(30)
            # Truncate long lines
            if len(line) > 90:
                line = line[:87] + '...'
            try:
                self.cell(0, line_height, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            except Exception:
                self.cell(0, line_height, '', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.set_x(30)

        self.ln(8)

    def add_table(self, rows, has_header=True):
        """Add a formatted table."""
        if not rows or not rows[0]:
            return

        self.ln(3)

        # Calculate column widths
        num_cols = len(rows[0])
        available_width = self.w - 50
        col_width = available_width / num_cols

        # Limit column width for many columns
        if num_cols > 4:
            col_width = min(col_width, 40)

        self.set_font('DejaVu', '', 9)

        for row_idx, row in enumerate(rows):
            # Check for page break
            if self.get_y() > self.h - 30:
                self.add_page()

            row_height = 7

            # Header row styling
            if row_idx == 0 and has_header:
                self.set_fill_color(*TABLE_HEADER_BG)
                self.set_text_color(*WHITE)
                self.set_font('DejaVu', 'B', 9)
            elif row_idx % 2 == 0:
                self.set_fill_color(*TABLE_ALT_ROW)
                self.set_text_color(*BLACK)
                self.set_font('DejaVu', '', 9)
            else:
                self.set_fill_color(*WHITE)
                self.set_text_color(*BLACK)
                self.set_font('DejaVu', '', 9)

            for col_idx, cell in enumerate(row):
                cell_text = str(cell).strip()[:50]  # Truncate long text
                self.cell(col_width, row_height, cell_text, border=1, fill=True)

            self.ln(row_height)

        self.ln(4)

    def add_horizontal_rule(self):
        """Add a horizontal rule."""
        self.ln(5)
        self.set_draw_color(*LIGHT_GRAY)
        self.set_line_width(0.3)
        self.line(25, self.get_y(), self.w - 25, self.get_y())
        self.ln(5)


def get_title_from_content(content):
    """Extract title from markdown content."""
    lines = content.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    return 'Documentation'


def get_subtitle_from_filename(filename):
    """Generate subtitle from filename."""
    subtitles = {
        # Main Documentation
        'DEVELOPMENT': 'Developer Setup Guide',
        'DEPLOYMENT': 'Deployment & Docker Guide',
        'TESTING': 'Testing Guide',
        'CONFIGURATION': 'Configuration Reference',
        'TROUBLESHOOTING': 'Troubleshooting Guide',
        'ARCHITECTURE': 'System Architecture',
        'SCHEMA': 'Database Schema Reference',
        'API_REFERENCE': 'API Documentation',
        'UNIVERSAL_REQUISITION': 'Frontend User Guide',
        'AGENT_CLI': 'AI Agent & CLI Guide',
        'README': 'Project Overview',
        # Database Schema & Structure
        'EDS_SUMMARY': 'Database Summary',
        'EDS_DATA_DICTIONARY': 'Complete Data Dictionary',
        'EDS_ERD': 'Entity Relationship Diagrams',
        # Business Logic & Domains
        'EDS_BUSINESS_DOMAINS': 'Business Domain Analysis',
        'EDS_BUSINESS_WORKFLOWS': 'Business Workflow Documentation',
        'EDS_STATUS_CODES': 'Status Codes Reference',
        'EDS_DATA_OWNERSHIP': 'Data Ownership Guide',
        'EDS_ACCESS_CONTROL': 'Access Control Documentation',
        # Stored Procedures
        'EDS_STORED_PROCEDURES': 'Stored Procedures Reference',
        'EDS_PROCEDURES_GUIDE': 'Procedures Usage Guide',
        'EDS_ROOT_PROCEDURES': 'Root Procedures Documentation',
        'EDS_PROCEDURE_DEPENDENCIES': 'Procedure Dependencies',
        'EDS_SP_DEPENDENCIES': 'SP Dependencies Analysis',
        'EDS_RECURSIVE_PROCEDURES': 'Recursive Procedures',
        'EDS_CIRCULAR_DEPS': 'Circular Dependencies Analysis',
        'EDS_INFINITE_LOOP_ANALYSIS': 'Infinite Loop Analysis',
        # Views
        'EDS_VIEWS': 'Views Reference',
        'EDS_VIEWS_GUIDE': 'Views Usage Guide',
        # Triggers & Indexes
        'EDS_TRIGGERS': 'Triggers Documentation',
        'EDS_INDEXES': 'Index Documentation',
        # Archive & ETL
        'EDS_ARCHIVE_ANALYSIS': 'Archive Analysis',
        'EDS_ARCHIVE_STRATEGY': 'Archive Strategy Guide',
        'EDS_ETL_INTEGRATIONS': 'ETL Integration Guide',
    }
    name = Path(filename).stem.upper()
    return subtitles.get(name, '')


def convert_markdown_to_pdf(md_content, pdf):
    """Convert markdown content to PDF."""
    lines = md_content.split('\n')
    i = 0

    in_code_block = False
    code_content = []
    code_language = ''

    in_table = False
    table_rows = []

    numbered_list_counter = 0

    while i < len(lines):
        line = lines[i]

        # Code block handling
        if line.startswith('```'):
            if in_code_block:
                # End code block
                pdf.add_code_block('\n'.join(code_content), code_language)
                code_content = []
                code_language = ''
                in_code_block = False
            else:
                # Start code block
                in_code_block = True
                code_language = line[3:].strip()
            i += 1
            continue

        if in_code_block:
            code_content.append(line)
            i += 1
            continue

        # Table handling
        if '|' in line and not line.startswith('```'):
            cells = [c.strip() for c in line.split('|')]
            cells = [c for c in cells if c or cells.index(c) not in [0, len(cells)-1]]

            if cells and not all(c.replace('-', '').replace(':', '').replace(' ', '') == '' for c in cells):
                if not in_table:
                    in_table = True
                    table_rows = []
                table_rows.append(cells)
            i += 1
            continue
        elif in_table:
            pdf.add_table(table_rows)
            table_rows = []
            in_table = False

        # Horizontal rule
        if line.strip() in ['---', '***', '___']:
            pdf.add_horizontal_rule()
            i += 1
            continue

        # Headers
        if line.startswith('# '):
            # Skip the main title (already on cover)
            i += 1
            continue
        elif line.startswith('## '):
            pdf.add_h1(line[3:].strip())
            numbered_list_counter = 0
            i += 1
            continue
        elif line.startswith('### '):
            pdf.add_h2(line[4:].strip())
            numbered_list_counter = 0
            i += 1
            continue
        elif line.startswith('#### '):
            pdf.add_h3(line[5:].strip())
            numbered_list_counter = 0
            i += 1
            continue
        elif line.startswith('##### '):
            pdf.add_h4(line[6:].strip())
            numbered_list_counter = 0
            i += 1
            continue

        # Bulleted list
        if line.strip().startswith('- ') or line.strip().startswith('* '):
            text = line.strip()[2:]
            level = (len(line) - len(line.lstrip())) // 2
            pdf.add_bullet_item(text, level)
            numbered_list_counter = 0
            i += 1
            continue

        # Numbered list
        match = re.match(r'^(\s*)(\d+)\.\s(.+)$', line)
        if match:
            level = len(match.group(1)) // 2
            numbered_list_counter += 1
            pdf.add_numbered_item(numbered_list_counter, match.group(3), level)
            i += 1
            continue
        else:
            numbered_list_counter = 0

        # Regular paragraph
        if line.strip():
            pdf.add_paragraph(line)

        i += 1

    # Handle any remaining table
    if in_table and table_rows:
        pdf.add_table(table_rows)


def convert_file(input_path, output_path):
    """Convert a single markdown file to PDF."""
    print(f"  Converting: {input_path}")

    # Read markdown content
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create PDF
    pdf = EDSPdf()

    # Add cover page
    title = get_title_from_content(content)
    subtitle = get_subtitle_from_filename(input_path)
    pdf.add_cover_page(title, subtitle)

    # Start content on new page
    pdf.add_page()

    # Convert content
    convert_markdown_to_pdf(content, pdf)

    # Save
    pdf.output(output_path)
    print(f"  Created: {output_path}")


def main():
    """Main function."""
    import argparse

    parser = argparse.ArgumentParser(description='Convert Markdown to PDF')
    parser.add_argument('--file', help='Single file to convert')
    parser.add_argument('--output-dir', default='docs/pdf', help='Output directory')
    args = parser.parse_args()

    # Find project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    docs_dir = project_root / 'docs'
    output_dir = project_root / args.output_dir

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*60}")
    print("EDS Documentation - PDF Generator")
    print(f"{'='*60}")
    print(f"Output directory: {output_dir}\n")

    if args.file:
        # Convert single file
        input_path = Path(args.file)
        if not input_path.exists():
            input_path = project_root / args.file

        output_path = output_dir / f"{input_path.stem}.pdf"
        convert_file(input_path, output_path)
    else:
        # Convert all documentation files (34 total)
        files_to_convert = [
            # Main Documentation
            'README.md',
            'ARCHITECTURE.md',
            'DEVELOPMENT.md',
            'DEPLOYMENT.md',
            'CONFIGURATION.md',
            'TESTING.md',
            'TROUBLESHOOTING.md',
            'API_REFERENCE.md',
            'UNIVERSAL_REQUISITION.md',
            'AGENT_CLI.md',
            # Database Schema & Structure
            'SCHEMA.md',
            'EDS_SUMMARY.md',
            'EDS_DATA_DICTIONARY.md',
            'EDS_ERD.md',
            # Business Logic & Domains
            'EDS_BUSINESS_DOMAINS.md',
            'EDS_BUSINESS_WORKFLOWS.md',
            'EDS_STATUS_CODES.md',
            'EDS_DATA_OWNERSHIP.md',
            'EDS_ACCESS_CONTROL.md',
            # Stored Procedures
            'EDS_STORED_PROCEDURES.md',
            'EDS_PROCEDURES_GUIDE.md',
            'EDS_ROOT_PROCEDURES.md',
            'EDS_PROCEDURE_DEPENDENCIES.md',
            'EDS_SP_DEPENDENCIES.md',
            'EDS_RECURSIVE_PROCEDURES.md',
            'EDS_CIRCULAR_DEPS.md',
            'EDS_INFINITE_LOOP_ANALYSIS.md',
            # Views
            'EDS_VIEWS.md',
            'EDS_VIEWS_GUIDE.md',
            # Triggers & Indexes
            'EDS_TRIGGERS.md',
            'EDS_INDEXES.md',
            # Archive & ETL
            'EDS_ARCHIVE_ANALYSIS.md',
            'EDS_ARCHIVE_STRATEGY.md',
            'EDS_ETL_INTEGRATIONS.md',
        ]

        converted = 0
        for filename in files_to_convert:
            input_path = docs_dir / filename
            if input_path.exists():
                output_path = output_dir / f"{input_path.stem}.pdf"
                try:
                    convert_file(input_path, output_path)
                    converted += 1
                except Exception as e:
                    print(f"  ERROR converting {filename}: {e}")
                    import traceback
                    traceback.print_exc()
            else:
                print(f"  Skipping (not found): {filename}")

        print(f"\n{'='*60}")
        print(f"Conversion complete: {converted} files created")
        print(f"Output location: {output_dir}")
        print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
