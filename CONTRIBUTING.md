# Contributing to EVALFlow

1. Create a virtual environment and install dev deps:
   ```bash
   python -m venv .venv && source .venv/Scripts/activate  # Windows Git Bash
   pip install -e .[dev]
   ```
2. Run tests:
   ```bash
   pytest -q
   ```
3. Submit PRs with a brief description and a before/after metric snapshot if relevant.
