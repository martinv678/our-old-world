#!/usr/bin/env python3
"""Prepare the repository's Markdown for the MkDocs website.

MkDocs can't use the repository root as its docs folder, so this copies the
content into build/docs/ and generates the site navigation in build/nav.yml
(read by mkdocs.yml through INHERIT). README.md becomes the home page.

Usage:
    python3 scripts/build_site.py      # then: mkdocs serve   (or mkdocs build)
"""

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"
DOCS = BUILD / "docs"
NAV = BUILD / "nav.yml"
COPY = ["GLOSSARY.md", "TIMELINE.md", "FIRES.md", "ALTERNATIVE-VIEW.md", "MEDIA.md", "media", "places", "links", "assets"]
COUNTRY_NAMES = {"uk": "UK", "usa": "USA"}

# Link targets pointing at README.md (in any folder depth) -> index.md
README_LINK = re.compile(r"(\]\((?:\.\./)*)README\.md")


def yaml_str(text: str) -> str:
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def title_of(path: Path) -> str:
    match = re.search(r"^# (.+)$", path.read_text(encoding="utf-8"), re.MULTILINE)
    return match.group(1).strip() if match else path.stem.replace("-", " ").title()


def main() -> int:
    if BUILD.exists():
        shutil.rmtree(BUILD)
    DOCS.mkdir(parents=True)

    shutil.copy(ROOT / "README.md", DOCS / "index.md")
    for name in COPY:
        src = ROOT / name
        if src.is_dir():
            shutil.copytree(src, DOCS / name)
        elif src.exists():
            shutil.copy(src, DOCS / name)

    for md in DOCS.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        new = README_LINK.sub(r"\1index.md", text)
        if new != text:
            md.write_text(new, encoding="utf-8")

    lines = ["nav:", '  - Home: index.md', '  - The alternative view: ALTERNATIVE-VIEW.md', '  - Timeline: TIMELINE.md', '  - Fires: FIRES.md', '  - Glossary: GLOSSARY.md', '  - Media: MEDIA.md', "  - Buildings:"]
    for country in sorted(p for p in (DOCS / "places").iterdir() if p.is_dir()):
        entries = [d / f"{d.name}.md" for d in sorted(country.iterdir()) if (d / f"{d.name}.md").exists()]
        if not entries:
            continue
        name = COUNTRY_NAMES.get(country.name, country.name.replace("-", " ").title())
        lines.append(f"      - {yaml_str(name)}:")
        for md in sorted(entries, key=lambda p: title_of(p).lower()):
            rel = md.relative_to(DOCS).as_posix()
            lines.append(f"          - {yaml_str(title_of(md))}: {rel}")
    research = [("Research list", "research-list.md"), ("Image shortlist", "image-shortlist.md"),
                ("Points of interest", "poi.md")]
    research = [(t, f) for t, f in research if (DOCS / "links" / f).exists()]
    if research:
        lines.append("  - Research:")
        lines += [f"      - {yaml_str(t)}: links/{f}" for t, f in research]
    NAV.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Site source ready in {DOCS.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
