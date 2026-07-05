#!/usr/bin/env python3
"""Save a story seed Markdown file and maintain a local index."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path


def slugify(title: str) -> str:
    text = title.strip().lower()
    text = re.sub(r"[^\w\u4e00-\u9fff]+", "-", text, flags=re.UNICODE)
    text = re.sub(r"-+", "-", text).strip("-_")
    return (text[:48].strip("-_") or "story-seed")


def unique_path(directory: Path, stem: str) -> Path:
    candidate = directory / f"{stem}.md"
    if not candidate.exists():
        return candidate
    counter = 2
    while True:
        candidate = directory / f"{stem}-{counter}.md"
        if not candidate.exists():
            return candidate
        counter += 1


def read_body(args: argparse.Namespace) -> str:
    if args.body_file:
        return Path(args.body_file).read_text(encoding="utf-8").strip()
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    return ""


def default_output_dir(workspace: Path) -> Path:
    outputs = workspace / "outputs"
    if outputs.exists():
        return outputs / "story-seeds"
    return workspace / "story-seeds"


def update_index(index_path: Path, date: str, title: str, filename: str) -> None:
    if index_path.exists():
        index = index_path.read_text(encoding="utf-8")
    else:
        index = "# 故事种子索引\n\n## Seeds\n"

    entry = f"- {date} [{title}]({filename})"
    if filename not in index:
        if not index.endswith("\n"):
            index += "\n"
        if "## Seeds" not in index:
            index += "\n## Seeds\n"
        index += entry + "\n"
        index_path.write_text(index, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Save a story seed and update index.md.")
    parser.add_argument("--workspace", default=".", help="Workspace root. Defaults to cwd.")
    parser.add_argument("--output-dir", help="Override output directory.")
    parser.add_argument("--title", required=True, help="Story seed title.")
    parser.add_argument("--date", default=dt.date.today().isoformat(), help="YYYY-MM-DD.")
    parser.add_argument("--body-file", help="Markdown body file. If omitted, stdin is used.")
    args = parser.parse_args()

    body = read_body(args)
    if not body:
        print("error: empty story seed body", file=sys.stderr)
        return 2

    workspace = Path(args.workspace).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve() if args.output_dir else default_output_dir(workspace)
    output_dir.mkdir(parents=True, exist_ok=True)

    compact_date = args.date.replace("-", "")
    path = unique_path(output_dir, f"{compact_date}-{slugify(args.title)}")
    content = body if body.lstrip().startswith("#") else f"# {args.title}\n\n{body}"
    path.write_text(content.rstrip() + "\n", encoding="utf-8")

    update_index(output_dir / "index.md", args.date, args.title, path.name)
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
