"""Run the lab setup checker from the repository root.

    python day08_setup.py check --light
    python day08_setup.py check
"""
import os
import runpy
from pathlib import Path


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    os.chdir(root)
    runpy.run_path(str(root / "docs" / "day08_setup.py"), run_name="__main__")
