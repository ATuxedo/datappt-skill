#!/usr/bin/env python3
"""Initialize resumable DataPPT project state without overwriting existing files."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


TEMPLATE_NAMES = (
    "PROJECT_HANDOFF.md",
    "STRATEGY_FRAMEWORK.md",
    "DECISION_LOG.md",
    "DATA_MAP.csv",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace_root", type=Path, help="Existing workspace or task root")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace existing state templates; never removes other project files",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.workspace_root.expanduser().resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Workspace root is not an existing directory: {root}")

    skill_root = Path(__file__).resolve().parent.parent
    template_root = skill_root / "assets" / "project-starter"
    state_root = root / "work" / "datappt" / "state"

    for folder in (
        state_root,
        root / "work" / "datappt" / "data",
        root / "work" / "datappt" / "modules",
        root / "work" / "datappt" / "qa",
        root / "work" / "datappt" / "renders",
        root / "outputs",
    ):
        folder.mkdir(parents=True, exist_ok=True)

    created: list[Path] = []
    kept: list[Path] = []
    for name in TEMPLATE_NAMES:
        source = template_root / name
        target = state_root / name
        if target.exists() and not args.force:
            kept.append(target)
            continue
        shutil.copy2(source, target)
        created.append(target)

    print(f"state_root={state_root}")
    for path in created:
        print(f"created={path}")
    for path in kept:
        print(f"kept={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
