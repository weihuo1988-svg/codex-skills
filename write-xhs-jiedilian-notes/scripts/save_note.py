#!/usr/bin/env python3
"""Archive a confirmed Xiaohongshu 姐弟恋 note package."""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path


def read_text(path: str) -> str:
    return Path(path).read_text(encoding="utf-8").strip()


def parse_tags(raw: str) -> list[str]:
    tokens: list[str] = []
    for line in raw.replace(",", " ").splitlines():
        tokens.extend(part.strip() for part in line.split(" ") if part.strip())
    normalized = []
    for token in tokens:
        normalized.append(token if token.startswith("#") else f"#{token}")
    return normalized


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def yaml_list(values: list[str]) -> str:
    if not values:
        return "[]"
    return "\n".join(f"  - {yaml_string(value)}" for value in values)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True, help="Target folder for confirmed notes")
    parser.add_argument("--title", required=True, help="Confirmed note title")
    parser.add_argument("--body-file", required=True, help="UTF-8 markdown/plaintext body file")
    parser.add_argument("--tags-file", required=True, help="UTF-8 tags file")
    parser.add_argument("--image", help="Generated cover image path")
    parser.add_argument("--image-prompt-file", help="Image prompt file when no image file exists yet")
    parser.add_argument("--source-screenshot", action="append", default=[], help="Original screenshot path; may repeat")
    parser.add_argument("--style-notes-file", help="Optional source-structure summary file")
    parser.add_argument("--slug", default="xhs-jiedilian-note", help="ASCII suffix for the archive folder")
    parser.add_argument("--status", default="confirmed", help="Archive status")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if not args.image and not args.image_prompt_file:
        raise SystemExit("Provide --image or --image-prompt-file so the note has one image asset or prompt.")

    output_dir = Path(args.output_dir).expanduser()
    output_dir.mkdir(parents=True, exist_ok=True)
    if not output_dir.is_dir():
        raise SystemExit(f"Output path is not a directory: {output_dir}")

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    archive_dir = output_dir / f"{timestamp}-{args.slug}"
    archive_dir.mkdir()

    body = read_text(args.body_file)
    tags = parse_tags(read_text(args.tags_file))
    style_notes = read_text(args.style_notes_file) if args.style_notes_file else ""

    image_ref = ""
    if args.image:
        image_path = Path(args.image).expanduser()
        if not image_path.is_file():
            raise SystemExit(f"Image file does not exist: {image_path}")
        image_name = f"cover{image_path.suffix.lower() or '.png'}"
        shutil.copy2(image_path, archive_dir / image_name)
        image_ref = image_name

    image_prompt = ""
    if args.image_prompt_file:
        image_prompt = read_text(args.image_prompt_file)
        (archive_dir / "image_prompt.md").write_text(image_prompt + "\n", encoding="utf-8")
        if not image_ref:
            image_ref = "image_prompt.md"

    created_at = datetime.now().isoformat(timespec="seconds")
    source_screenshots = [str(Path(path).expanduser()) for path in args.source_screenshot]

    frontmatter = [
        "---",
        f"title: {yaml_string(args.title)}",
        f"created_at: {yaml_string(created_at)}",
        f"status: {yaml_string(args.status)}",
        f"image: {yaml_string(image_ref)}",
        "tags:",
        yaml_list(tags),
        "source_screenshots:",
        yaml_list(source_screenshots),
        "---",
        "",
    ]

    lines = frontmatter
    lines.append(f"# {args.title}")
    lines.append("")
    if args.image and image_ref:
        lines.append(f"![cover](./{image_ref})")
        lines.append("")
    if image_prompt:
        lines.append("## 图片提示词")
        lines.append("")
        lines.append(image_prompt)
        lines.append("")
    lines.append("## 正文")
    lines.append("")
    lines.append(body)
    lines.append("")
    lines.append("## 标签")
    lines.append("")
    lines.append(" ".join(tags))
    lines.append("")
    if style_notes:
        lines.append("## 参考拆解")
        lines.append("")
        lines.append(style_notes)
        lines.append("")

    (archive_dir / "note.md").write_text("\n".join(lines), encoding="utf-8")
    print(archive_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
