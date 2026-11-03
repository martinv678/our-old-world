#!/usr/bin/env python3
"""Build the building lists in GLOSSARY.md from each entry's Features row.

For every places/<country>/<building>/<building>.md entry, this reads the
"| **Features** | ... |" row of the details table, then:

  * rewrites that row so each feature links to its glossary section
  * fills in the list of buildings under each feature in GLOSSARY.md
  * rebuilds the index at the top of GLOSSARY.md
  * adds a placeholder section for any feature not yet in the glossary

Run from anywhere:  python3 scripts/build_glossary.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GLOSSARY = ROOT / "GLOSSARY.md"
PLACES = ROOT / "places"

FEATURES_ROW = re.compile(r"^\|\s*\*\*Features\*\*\s*\|(.*)\|\s*$", re.MULTILINE)
LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")
INDEX_BLOCK = re.compile(r"<!-- index:start -->.*?<!-- index:end -->", re.DOTALL)
BUILDINGS_BLOCK = re.compile(r"<!-- buildings:start -->.*?<!-- buildings:end -->", re.DOTALL)
SECTION_HEADING = re.compile(r"^## (.+)$", re.MULTILINE)
NOT_FEATURES = {"how the glossary works"}


def slug(text: str) -> str:
    """GitHub-style heading anchor."""
    text = text.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def parse_features(cell: str) -> list[str]:
    cell = LINK.sub(r"\1", cell)
    return [f.strip() for f in cell.split(",") if f.strip()]


def load_entries():
    entries = []
    for path in sorted(PLACES.glob("*/*/*.md")):
        if path.stem != path.parent.name:
            continue
        text = path.read_text(encoding="utf-8")
        title_match = re.search(r"^# (.+)$", text, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else path.stem
        country = path.parent.parent.name.replace("-", " ").title()
        if country.lower() in {"uk", "usa"}:
            country = country.upper()
        match = FEATURES_ROW.search(text)
        features = parse_features(match.group(1)) if match else []
        entries.append({"path": path, "text": text, "title": title,
                        "country": country, "features": features})
    return entries


def glossary_sections(text: str) -> dict[str, str]:
    """Map feature slug -> heading text for each feature section."""
    return {slug(h): h.strip() for h in SECTION_HEADING.findall(text)
            if h.strip().lower() not in NOT_FEATURES}


def add_missing_sections(text: str, missing: list[str]) -> str:
    stubs = "".join(
        f"## {name}\n\n_Description needed._\n\n**Why it matters:** _To be added._\n\n"
        "<!-- buildings:start -->\n<!-- buildings:end -->\n\n"
        for name in missing
    )
    marker = "---\n\n## How the glossary works"
    if marker in text:
        return text.replace(marker, stubs + marker, 1)
    return text.rstrip() + "\n\n" + stubs


def fill_sections(text: str, by_feature: dict[str, list[dict]]) -> str:
    parts = SECTION_HEADING.split(text)
    # parts = [preamble, heading1, body1, heading2, body2, ...]
    out = [parts[0]]
    for heading, body in zip(parts[1::2], parts[2::2]):
        buildings = by_feature.get(slug(heading), [])
        if buildings:
            lines = [f"**Buildings ({len(buildings)}):**", ""]
            for e in sorted(buildings, key=lambda e: (e["country"], e["title"])):
                rel = e["path"].relative_to(ROOT).as_posix()
                lines.append(f"- [{e['title']}]({rel}) – {e['country']}")
            block = "\n".join(lines)
        else:
            block = "_No buildings tagged yet._"
        body = BUILDINGS_BLOCK.sub(
            f"<!-- buildings:start -->\n{block}\n<!-- buildings:end -->", body)
        out += [f"## {heading}", body]
    return "".join(out)


def build_index(sections: dict[str, str], by_feature: dict[str, list[dict]]) -> str:
    rows = ["| Feature | Buildings |", "|---|---|"]
    for key, name in sorted(sections.items(), key=lambda kv: kv[1].lower()):
        rows.append(f"| [{name}](#{key}) | {len(by_feature.get(key, []))} |")
    return "<!-- index:start -->\n" + "\n".join(rows) + "\n<!-- index:end -->"


def link_entry_features(entry, sections: dict[str, str]) -> str:
    depth = len(entry["path"].relative_to(ROOT).parts) - 1
    glossary_rel = "../" * depth + "GLOSSARY.md"
    links = [f"[{sections[slug(f)]}]({glossary_rel}#{slug(f)})" for f in entry["features"]]
    row = f"| **Features** | {', '.join(links)} |"
    return FEATURES_ROW.sub(lambda _: row, entry["text"], count=1)


def main() -> int:
    entries = load_entries()
    text = GLOSSARY.read_text(encoding="utf-8")
    sections = glossary_sections(text)

    missing, seen = [], set()
    for e in entries:
        for f in e["features"]:
            if slug(f) not in sections and slug(f) not in seen:
                missing.append(f[0].upper() + f[1:])
                seen.add(slug(f))
    if missing:
        print("Added placeholder glossary sections for: " + ", ".join(missing))
        text = add_missing_sections(text, missing)
        sections = glossary_sections(text)

    by_feature: dict[str, list[dict]] = {}
    for e in entries:
        for f in e["features"]:
            by_feature.setdefault(slug(f), []).append(e)

    text = fill_sections(text, by_feature)
    text = INDEX_BLOCK.sub(lambda _: build_index(sections, by_feature), text)
    GLOSSARY.write_text(text, encoding="utf-8")

    untagged = []
    for e in entries:
        if not e["features"]:
            untagged.append(e["path"].relative_to(ROOT).as_posix())
            continue
        new_text = link_entry_features(e, sections)
        if new_text != e["text"]:
            e["path"].write_text(new_text, encoding="utf-8")

    if untagged:
        print("No Features row in: " + ", ".join(untagged))
    print(f"Glossary updated: {len(sections)} features, {len(entries)} buildings.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
