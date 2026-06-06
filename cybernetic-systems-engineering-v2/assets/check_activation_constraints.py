#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT_DIR = Path(__file__).resolve().parents[2]
FILES = {
    "skill": ROOT_DIR / "cybernetic-systems-engineering-v2" / "SKILL.md",
    "router": ROOT_DIR / "cybernetic-systems-engineering-v2" / "router.md",
    "references": ROOT_DIR / "cybernetic-systems-engineering-v2" / "references" / "README.md",
    "readme": ROOT_DIR / "README.md",
}

CHECKS = (
    ("skill", r"激活约束|任务输出约束|协议激活声明", "CSE v2 skill activation constraints missing"),
    ("router", r"激活清单|必须深读", "CSE v2 router deep-read list missing"),
    ("references", r"命中路由后必须深读|首轮输出必须声明激活协议", "CSE v2 references activation guidance missing"),
    ("readme", r"自包的 skillbase|必须继续激活|激活清单", "Repository README activation summary missing"),
)


def require_match(path: Path, pattern: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    if re.search(pattern, text) is None:
        raise SystemExit(
            f"FAIL: {label}\n"
            f"  missing pattern: {pattern}\n"
            f"  file: {path}"
        )


def main() -> int:
    for key, pattern, label in CHECKS:
        require_match(FILES[key], pattern, label)
    print("PASS: activation constraints are present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
