#!/usr/bin/env python
from __future__ import annotations

import pathlib
import sys


def _ensure_spec_arg(default_spec: pathlib.Path) -> None:
    if "--spec" in sys.argv:
        return
    sys.argv.extend(["--spec", str(default_spec)])


def main() -> None:
    skill_scripts = pathlib.Path(
        "C:/Users/Grimakis/.codex/skills/tandy-m100-programming/scripts"
    )
    sys.path.insert(0, str(skill_scripts))
    from run_8085_spec import main as run_main  # type: ignore

    default_spec = pathlib.Path(__file__).resolve().parent / "specs" / "snowed_in_init.json"
    _ensure_spec_arg(default_spec)
    run_main()


if __name__ == "__main__":
    main()
