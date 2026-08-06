#!/usr/bin/env python3
"""Replace fragile PPTX CJK font declarations and optionally normalize package structure."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
import sys
import tempfile
import zipfile


FONT_TAG_RE = re.compile(
    r'(<a:(?:latin|ea|cs)\b[^>]*\btypeface=")([^"]*)(")',
    flags=re.IGNORECASE,
)
FONT_SCHEME_RE = re.compile(
    r'(<a:fontScheme\b[^>]*\bname=")([^"]*)(")',
    flags=re.IGNORECASE,
)


def rewrite_xml(data: bytes, font: str) -> bytes:
    text = data.decode("utf-8")
    text = FONT_TAG_RE.sub(lambda m: f"{m.group(1)}{font}{m.group(3)}", text)
    text = FONT_SCHEME_RE.sub(lambda m: f"{m.group(1)}{font}{m.group(3)}", text)
    return text.encode("utf-8")


def rewrite_pptx(src: Path, out: Path, font: str) -> None:
    with zipfile.ZipFile(src, "r") as zin, zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zout:
        for info in zin.infolist():
            data = zin.read(info.filename)
            if info.filename.endswith(".xml"):
                try:
                    data = rewrite_xml(data, font)
                except UnicodeDecodeError:
                    pass
            zout.writestr(info, data)


def normalize_with_python_pptx(src: Path, out: Path) -> bool:
    try:
        from pptx import Presentation  # type: ignore
    except Exception:
        return False
    prs = Presentation(str(src))
    prs.save(str(out))
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Input PPTX")
    parser.add_argument("--out", type=Path, help="Output PPTX")
    parser.add_argument("--font", default="Microsoft YaHei", help="Office-safe font name")
    parser.add_argument(
        "--no-normalize",
        action="store_true",
        help="Skip python-pptx open/save package normalization",
    )
    args = parser.parse_args()

    src = args.input.expanduser().resolve()
    if not src.exists():
        print(f"Input not found: {src}", file=sys.stderr)
        return 2
    out = args.out.expanduser().resolve() if args.out else src.with_name(f"{src.stem}_fixed.pptx")
    out.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="ppt-fontfix-") as tmp:
        intermediate = Path(tmp) / "fontfix.pptx"
        rewrite_pptx(src, intermediate, args.font)
        if args.no_normalize:
            shutil.copyfile(intermediate, out)
            normalized = False
        else:
            normalized = normalize_with_python_pptx(intermediate, out)
            if not normalized:
                shutil.copyfile(intermediate, out)

    print(f"wrote={out}")
    print(f"font={args.font}")
    print(f"normalized={str(normalized).lower()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
