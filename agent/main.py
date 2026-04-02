"""Entry point for the EDS DBA Agent.

Supports both:
  - CLI: `eds-agent chat`, `eds-agent ask "question"`, etc.
  - Module: `python -m agent chat`, `python -m agent ask "question"`, etc.
"""

from agent.cli.app import cli


def main():
    cli()


if __name__ == "__main__":
    main()
