#!/usr/bin/env python3
"""Rebuild the generated indexes from each building entry's details table.

For every places/<country>/<building>/<building>.md entry, this reads the
"| **Type** | ... |" and "| **Features** | ... |" rows, then:

  * rebuilds the "Buildings by type" list in README.md
  * rebuilds the index and per-feature building lists in GLOSSARY.md
  * adds a placeholder glossary section for any feature not yet defined
  * rewrites each entry's Type and Features rows as clickable links
  * rebuilds FIRES.md, the list of buildings damaged by fire or bombing,
    from each entry's "| **Fires** | ... |" and "| **War damage** | ... |" rows
  * rebuilds the "Building images" gallery in MEDIA.md from every image in
    each entry's images/ folder, with the caption it has in the entry

Run from anywhere:  python3 scripts/build_index.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
GLOSSARY = ROOT / "GLOSSARY.md"
TIMELINE = ROOT / "TIMELINE.md"
FIRES = ROOT / "FIRES.md"
MEDIA = ROOT / "MEDIA.md"
PLACES = ROOT / "places"

LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")
CATALOGUE_BLOCK = re.compile(r"<!-- catalogue:start -->.*?<!-- catalogue:end -->", re.DOTALL)
INDEX_BLOCK = re.compile(r"<!-- index:start -->.*?<!-- index:end -->", re.DOTALL)
TIMELINE_BLOCK = re.compile(r"<!-- timeline:start -->.*?<!-- timeline:end -->", re.DOTALL)
FIRES_BLOCK = re.compile(r"<!-- fires:start -->.*?<!-- fires:end -->", re.DOTALL)
MEDIA_BLOCK = re.compile(r"<!-- media:start -->.*?<!-- media:end -->", re.DOTALL)
BUILDINGS_BLOCK = re.compile(r"<!-- buildings:start -->.*?<!-- buildings:end -->", re.DOTALL)
SECTION_HEADING = re.compile(r"^## (.+)$", re.MULTILINE)
NOT_FEATURES = {"how the glossary works"}
COUNTRY_NAMES = {"uk": "UK", "usa": "USA"}


def row_pattern(label: str) -> re.Pattern:
    return re.compile(rf"^\|[ \t]*\*\*{label}\*\*[ \t]*\|(.*)\|[ \t]*$", re.MULTILINE)


TYPE_ROW = row_pattern("Type")
FEATURES_ROW = row_pattern("Features")
BUILT_ROW = row_pattern("Built")
STATUS_ROW = row_pattern("Status")
FIRES_ROW = row_pattern("Fires")
WAR_ROW = row_pattern("War damage")


def slug(text: str) -> str:
    """GitHub-style heading anchor."""
    text = text.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def capitalise(text: str) -> str:
    return text[:1].upper() + text[1:]


def cell(pattern: re.Pattern, text: str) -> str:
    match = pattern.search(text)
    return LINK.sub(r"\1", match.group(1)).strip() if match else ""


def tags(pattern: re.Pattern, text: str) -> list[str]:
    return [capitalise(t.strip()) for t in cell(pattern, text).split(",") if t.strip()]


def first_year(built: str):
    """First year mentioned in a Built cell, e.g. 'Early 1600s; ...' -> 1600, 'c. 1857–66' -> 1857."""
    match = re.search(r"\b(1\d{3}|[5-9]\d{2})(?:s)?\b", built)
    return int(match.group(1)) if match else None


def ordinal_century(year: int) -> str:
    n = year // 100 + 1
    suffix = "th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix} century"


def build_timeline(entries) -> str:
    dated = sorted((e for e in entries if e["year"]), key=lambda e: (e["year"], e["title"].lower()))
    undated = [e for e in entries if not e["year"]]
    lines = ["<!-- timeline:start -->"]
    current = None
    for e in dated:
        century = ordinal_century(e["year"])
        if century != current:
            current = century
            lines += ["", f"## {century}", "", "| Year | Building | Country | Built | Type |", "|---|---|---|---|---|"]
        lines.append(f"| {e['year']} | [{e['title']}]({e['rel']}) | {e['country']} | {e['built']} | {', '.join(e['types'])} |")
    if undated:
        lines += ["", "## Date not yet known", ""]
        lines += [f"- [{e['title']}]({e['rel']}) – {e['country']}" for e in undated]
    lines.append("<!-- timeline:end -->")
    return "\n".join(lines)


def build_fires(entries) -> str:
    """Tables of buildings with a Fires row, then those with a War damage row."""
    def table(key: str) -> list[str]:
        rows = [e for e in entries if e[key]]
        rows.sort(key=lambda e: (e["year"] or 9999, e["title"].lower()))
        out = ["| Building | Country | Built | What happened | Status |", "|---|---|---|---|---|"]
        out += [f"| [{e['title']}]({e['rel']}) | {e['country']} | {e['built']} | {e[key]} | {e['status']} |"
                for e in rows]
        return out, len(rows)
    fire_rows, n_fire = table("fires")
    war_rows, n_war = table("war")
    lines = ["<!-- fires:start -->", "", f"## Damaged or destroyed by fire ({n_fire})", ""] + fire_rows
    lines += ["", f"## Damaged by bombing in war ({n_war})", ""] + war_rows
    lines += ["", "<!-- fires:end -->"]
    return "\n".join(lines)


IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"}
# An image line in an entry, optionally followed by an italic caption line.
ENTRY_IMAGE = re.compile(r"^!\[([^\]]*)\]\(images/([^)\s]+)\)[ \t]*(?:\n\*(.+)\*[ \t]*)?$", re.MULTILINE)


def one_line(text: str) -> str:
    return " ".join(LINK.sub(r"\1", text).split())


def build_media(entries) -> str:
    """Gallery of every building's images, by country then building."""
    total = 0
    body = []
    current = None
    for e in sorted(entries, key=by_country_then_title):
        folder = e["path"].parent / "images"
        files = sorted(f for f in folder.iterdir() if f.suffix.lower() in IMAGE_EXTS) if folder.is_dir() else []
        if not files:
            continue
        used = {}
        for alt, name, caption in ENTRY_IMAGE.findall(e["text"]):
            used.setdefault(name, (one_line(alt), one_line(caption)))
        # Images in the order the entry uses them, then any not yet used.
        order = [n for n in used if (folder / n).exists()]
        order += [f.name for f in files if f.name not in used]
        if e["country"] != current:
            current = e["country"]
            body += ["", f"### {current}"]
        body += ["", f"#### [{e['title']}]({e['rel']}) ({len(order)})", "", '<div class="media-grid" markdown>', ""]
        for name in order:
            alt, caption = used.get(name, (name.rsplit(".", 1)[0].replace("-", " "), ""))
            src = (folder / name).relative_to(ROOT).as_posix()
            body.append(f"![{alt}]({src})")
            body.append(f"*{caption or 'Not yet used in the entry.'}*")
            body.append("")
        body.append("</div>")
        total += len(order)
    lines = ["<!-- media:start -->", "", f"{total} images from {sum(1 for l in body if l.startswith('#### '))} buildings."]
    return "\n".join(lines + body + ["", "<!-- media:end -->"])


def load_entries():
    entries = []
    for path in sorted(PLACES.glob("*/*/*.md")):
        if path.stem != path.parent.name:
            continue
        text = path.read_text(encoding="utf-8")
        title_match = re.search(r"^# (.+)$", text, re.MULTILINE)
        folder = path.parent.parent.name
        entries.append({
            "path": path,
            "rel": path.relative_to(ROOT).as_posix(),
            "text": text,
            "title": title_match.group(1).strip() if title_match else path.stem,
            "country": COUNTRY_NAMES.get(folder, folder.replace("-", " ").title()),
            "types": tags(TYPE_ROW, text),
            "features": tags(FEATURES_ROW, text),
            "built": cell(BUILT_ROW, text),
            "year": first_year(cell(BUILT_ROW, text)),
            "status": cell(STATUS_ROW, text).split(";")[0].strip(),
            "fires": cell(FIRES_ROW, text),
            "war": cell(WAR_ROW, text),
        })
    return entries


def group(entries, key: str) -> tuple[dict[str, str], dict[str, list[dict]]]:
    """Return (slug -> display name, slug -> entries) for types or features."""
    names, members = {}, {}
    for e in entries:
        for name in e[key]:
            names.setdefault(slug(name), name)
            members.setdefault(slug(name), []).append(e)
    return names, members


def by_country_then_title(e):
    return (e["country"], e["title"].lower())


# ---------------------------------------------------------------- README


def build_catalogue(entries) -> str:
    names, members = group(entries, "types")
    order = sorted(names, key=lambda k: names[k].lower())
    lines = ["<!-- catalogue:start -->"]
    if order:
        lines.append("**Jump to:** " + " · ".join(
            f"[{names[k]}](#{k}) ({len(members[k])})" for k in order))
    for k in order:
        lines += ["", f"### {names[k]}", "",
                  "| Building | Country | Built | Status |", "|---|---|---|---|"]
        for e in sorted(members[k], key=by_country_then_title):
            lines.append(f"| [{e['title']}]({e['rel']}) | {e['country']} | {e['built']} | {e['status']} |")
    untyped = [e for e in entries if not e["types"]]
    if untyped:
        lines += ["", "### Not yet categorised", "",
                  "| Building | Country | Built | Status |", "|---|---|---|---|"]
        for e in sorted(untyped, key=by_country_then_title):
            lines.append(f"| [{e['title']}]({e['rel']}) | {e['country']} | {e['built']} | {e['status']} |")
    lines.append("<!-- catalogue:end -->")
    return "\n".join(lines)


# -------------------------------------------------------------- GLOSSARY


def glossary_sections(text: str) -> dict[str, str]:
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


def fill_sections(text: str, members: dict[str, list[dict]]) -> str:
    parts = SECTION_HEADING.split(text)
    out = [parts[0]]
    for heading, body in zip(parts[1::2], parts[2::2]):
        buildings = members.get(slug(heading), [])
        if buildings:
            lines = [f"**Buildings ({len(buildings)}):**", ""]
            lines += [f"- [{e['title']}]({e['rel']}) – {e['country']}"
                      for e in sorted(buildings, key=by_country_then_title)]
            block = "\n".join(lines)
        else:
            block = "_No buildings tagged yet._"
        body = BUILDINGS_BLOCK.sub(
            lambda _: f"<!-- buildings:start -->\n{block}\n<!-- buildings:end -->", body)
        out += [f"## {heading}", body]
    return "".join(out)


def build_index(sections: dict[str, str], members: dict[str, list[dict]]) -> str:
    rows = ["| Feature | Buildings |", "|---|---|"]
    for key, name in sorted(sections.items(), key=lambda kv: kv[1].lower()):
        rows.append(f"| [{name}](#{key}) | {len(members.get(key, []))} |")
    return "<!-- index:start -->\n" + "\n".join(rows) + "\n<!-- index:end -->"


# --------------------------------------------------------------- entries


def link_row(text: str, pattern: re.Pattern, label: str, items: list[str],
             target: str, names: dict[str, str]) -> str:
    if not items:
        return text
    links = ", ".join(f"[{names.get(slug(i), i)}]({target}#{slug(i)})" for i in items)
    return pattern.sub(lambda _: f"| **{label}** | {links} |", text, count=1)


def main() -> int:
    entries = load_entries()

    # Glossary
    glossary = GLOSSARY.read_text(encoding="utf-8")
    sections = glossary_sections(glossary)
    feature_names, feature_members = group(entries, "features")
    missing = [feature_names[k] for k in feature_names if k not in sections]
    if missing:
        print("Added placeholder glossary sections for: " + ", ".join(missing))
        glossary = add_missing_sections(glossary, missing)
        sections = glossary_sections(glossary)
    glossary = fill_sections(glossary, feature_members)
    glossary = INDEX_BLOCK.sub(lambda _: build_index(sections, feature_members), glossary)
    GLOSSARY.write_text(glossary, encoding="utf-8")

    # README
    readme = README.read_text(encoding="utf-8")
    if not CATALOGUE_BLOCK.search(readme):
        print("README.md has no <!-- catalogue:start --> / <!-- catalogue:end --> markers.")
        return 1
    readme = CATALOGUE_BLOCK.sub(lambda _: build_catalogue(entries), readme)
    README.write_text(readme, encoding="utf-8")

    # Timeline
    timeline = TIMELINE.read_text(encoding="utf-8")
    TIMELINE.write_text(TIMELINE_BLOCK.sub(lambda _: build_timeline(entries), timeline), encoding="utf-8")

    # Fires
    if FIRES.exists():
        fires = FIRES.read_text(encoding="utf-8")
        FIRES.write_text(FIRES_BLOCK.sub(lambda _: build_fires(entries), fires), encoding="utf-8")

    # Media
    if MEDIA.exists():
        media = MEDIA.read_text(encoding="utf-8")
        MEDIA.write_text(MEDIA_BLOCK.sub(lambda _: build_media(entries), media), encoding="utf-8")

    # Entries
    type_names, _ = group(entries, "types")
    for e in entries:
        up = "../" * (len(e["path"].relative_to(ROOT).parts) - 1)
        text = link_row(e["text"], TYPE_ROW, "Type", e["types"], up + "README.md", type_names)
        text = link_row(text, FEATURES_ROW, "Features", e["features"], up + "GLOSSARY.md", sections)
        if text != e["text"]:
            e["path"].write_text(text, encoding="utf-8")

    for label, key in (("Type", "types"), ("Features", "features")):
        lacking = [e["rel"] for e in entries if not e[key]]
        if lacking:
            print(f"No {label} row in: " + ", ".join(lacking))
    print(f"Updated: {len(entries)} buildings, {len(type_names)} types, {len(sections)} features.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
