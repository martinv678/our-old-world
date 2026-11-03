# Our Old World

A collection of pre-1900 buildings looked at from two sides: **the story we are told**, and **the alternative**.

Many of the grand buildings of the 18th and 19th centuries raise questions that the official records don't always answer well. Ornate domes and towers put up in a few years. Huge stone structures in small or remote towns. Ground floors half buried below street level. Buildings that were "built" for one purpose and then abandoned soon after. This repo collects those places, sets out the accepted history, and then looks at what an alternative explanation might be.

The aim is not to tell anyone what to believe. It is to put both versions side by side, with sources, so readers can weigh them up for themselves.

## What this repo covers

- **Pre-1900 buildings only.** Anything built (or said to have been built) before 1900: palaces, casinos, villas, churches, exhibition halls, railway stations, star forts, public buildings and so on.
- **The main story.** The accepted history: who built it, when, why, and what happened to it, backed by sources.
- **The alternative view.** The questions and anomalies that don't fit neatly, and the alternative history theories that try to explain them.

## Themes in the alternative view

These are some of the ideas that come up again and again when looking at old world buildings. Entries may touch on one or more of them.

- **Who really built it?** The theory that some of these buildings came from an earlier, more advanced civilisation (sometimes called *Tartaria* or the "old world") and were later claimed, re-dated or repurposed.
- **Construction timelines.** Buildings recorded as finished in a handful of years with the tools, labour and money of the time. Does the timeline add up?
- **Mud flood and buried floors.** Ground floors and windows below today's street level, raised streets, and buildings that appear to have been dug out.
- **Shared architecture worldwide.** The same domes, columns and proportions turning up on different continents at around the same time.
- **Purpose and abandonment.** Buildings that seem far too grand for their stated use, or that were abandoned or demolished soon after being finished.
- **Missing or thin records.** Gaps in architects' records, construction photos, plans or costs.
- **Old maps, photos and postcards.** Early images that show things the official story doesn't explain.

## Repository structure

```
our-old-world/
├── README.md
├── GLOSSARY.md                     # Features index (domes, towers, rose windows...)
├── mkdocs.yml                      # Website settings
├── assets/                         # Website styles
├── scripts/
│   ├── build_index.py              # Rebuilds the Buildings list and the glossary
│   └── build_site.py               # Prepares the website build
├── links/
│   └── poi.md                      # Points of interest still to be researched
└── places/
    └── <country>/
        └── <building>/
            ├── <building>.md       # The write-up
            └── images/             # Photos, postcards, maps
```

Example: [`places/italy/villa-sultana/villa-sultana.md`](places/italy/villa-sultana/villa-sultana.md)

The town or city goes in the details table at the top of each entry, not in the folder path. Categories such as *railway station* or *castle* go in the entry's **Type** row rather than in folders, because one building can belong to several.

## Buildings

Every building, grouped by type. A building can appear under more than one type (for example a station that is also a hotel). This list is generated automatically from each entry's **Type** row, so there's no need to edit it by hand.

<!-- catalogue:start -->
**Jump to:** [Casino](#casino) (1) · [Castle](#castle) (2) · [Exhibition hall](#exhibition-hall) (1) · [Hotel](#hotel) (1) · [Palace](#palace) (1) · [Railway station](#railway-station) (4) · [Villa](#villa) (2)

### Casino

| Building | Country | Built | Status |
|---|---|---|---|
| [Villa Sultana (Villa "La Sultana")](places/italy/villa-sultana/villa-sultana.md) | Italy | 1883–1884 | Abandoned / derelict |

### Castle

| Building | Country | Built | Status |
|---|---|---|---|
| [Castello di Sammezzano](places/italy/castello-di-sammezzano/castello-di-sammezzano.md) | Italy | Early 1600s; remodelled c. 1853–1889 | Abandoned since 1990 |
| [Rocchetta Mattei](places/italy/rocchetta-mattei/rocchetta-mattei.md) | Italy | From 1850, on the ruins of a medieval fortress; extended until the 1890s | Restored by Fondazione Carisbo |

### Exhibition hall

| Building | Country | Built | Status |
|---|---|---|---|
| [The Crystal Palace](places/uk/crystal-palace/crystal-palace.md) | UK | 1850–1851; dismantled and rebuilt larger at Sydenham 1852–1854 | Destroyed by fire 1936 |

### Hotel

| Building | Country | Built | Status |
|---|---|---|---|
| [St Pancras Station and Midland Grand Hotel](places/uk/st-pancras/st-pancras.md) | UK | Train shed 1865–1868; hotel 1868–1876 | In use as St Pancras International station and the St Pancras Renaissance Hotel |

### Palace

| Building | Country | Built | Status |
|---|---|---|---|
| [Royal Pavilion, Brighton](places/uk/royal-pavilion-brighton/royal-pavilion-brighton.md) | UK | 1787 (Marine Pavilion); rebuilt and extended c. 1815–1823 | Museum, run by Brighton & Hove Museums |

### Railway station

| Building | Country | Built | Status |
|---|---|---|---|
| [Anhalter Bahnhof](places/germany/anhalter-bahnhof/anhalter-bahnhof.md) | Germany | 1876–1880, replacing a station of 1841 | Demolished 1959–1960 |
| [Dresden Hauptbahnhof](places/germany/dresden-hauptbahnhof/dresden-hauptbahnhof.md) | Germany | 1892–1898 | In use |
| [Frankfurt (Main) Hauptbahnhof](places/germany/frankfurt-hauptbahnhof/frankfurt-hauptbahnhof.md) | Germany | 1883–1888 | In use |
| [St Pancras Station and Midland Grand Hotel](places/uk/st-pancras/st-pancras.md) | UK | Train shed 1865–1868; hotel 1868–1876 | In use as St Pancras International station and the St Pancras Renaissance Hotel |

### Villa

| Building | Country | Built | Status |
|---|---|---|---|
| [Villa Crespi](places/italy/villa-crespi/villa-crespi.md) | Italy | From 1879 | In use as a hotel and restaurant |
| [Villa Sultana (Villa "La Sultana")](places/italy/villa-sultana/villa-sultana.md) | Italy | 1883–1884 | Abandoned / derelict |
<!-- catalogue:end -->

Places still to be looked at are listed in [`links/poi.md`](links/poi.md).

## Glossary of features

Want to see every building with a dome, a tower or a rose window? The [glossary](GLOSSARY.md) lists architectural features, explains why each one interests the alternative view, and links to every building that has it.

## Adding a building

1. Check the building was built, or is said to have been built, **before 1900**.
2. Create a folder at `places/<country>/<building-name>/` using lowercase and hyphens (for example `places/uk/crystal-palace/`).
3. Add a `<building-name>.md` file using the template below.
4. Put any images in an `images/` folder next to it, and check the licence before uploading. Use short lowercase file names with hyphens, such as `postcard-1900.jpg`, and keep images under about 1600px wide. Show them on the page with a description and a credit line underneath:

   ```markdown
   ![Short description of the image](images/postcard-1900.jpg)
   *Caption: what it shows, date, source and licence.*
   ```

   Put one main image under the details table and the rest in an `## Images` section before Sources (see [Villa Sultana](places/italy/villa-sultana/villa-sultana.md) for an example). On the website, readers can click any image to enlarge it.
5. Fill in the **Type** row with one or more categories, separated by commas, such as `Railway station, Hotel`. Reuse the names in the [Buildings](#buildings) list where you can.
6. Fill in the **Features** row using names from the [glossary](GLOSSARY.md). New features are fine too: the script will add a placeholder for them.
7. Run `python3 scripts/build_index.py` to update the Buildings list, the glossary and the links. If you skip this, it runs automatically on GitHub when the change reaches `main`.

### Entry template

```markdown
# Building Name

| | |
|---|---|
| **Location** | Address, town, region, country |
| **Built** | Year(s) |
| **Architect** | Name (if known) |
| **Style** | |
| **Type** | Railway station, Hotel |
| **Original use** | |
| **Status** | In use / Abandoned / Demolished / Restored |
| **Features** | Dome, Tower, Rose window |

## Overview

A short description of the building and where it is.

## The main story

The accepted history, with dates. Who built it, why, how it was funded,
and what happened to it afterwards.

## The alternative view

What doesn't add up? For example:

- Construction time, cost or labour that seems unlikely
- Buried floors, raised ground or signs of a mud flood
- Architecture matching buildings elsewhere in the world
- Gaps or contradictions in the records
- Old photos, maps or postcards that raise questions

Then set out the alternative explanation and what would support it.

## Open questions

Things that still need checking or that contributors could help with.

## Sources

Links for both the main story and the alternative view.
```

## Website

The repo is also published as a website with search, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and hosted on GitHub Pages at <https://martinv678.github.io/our-old-world/>. It rebuilds automatically every time a change reaches `main`.

To preview it on your own computer:

```bash
pip install -r requirements-site.txt
python3 scripts/build_index.py && python3 scripts/build_site.py && mkdocs serve
```

Then open <http://127.0.0.1:8000>.

## Guidelines

- **Cite sources for both sides.** Link to the official records as well as the alternative research, so readers can follow the trail.
- **Keep the two clearly separate.** The main story section should say what the records say. Theories and questions belong in the alternative view.
- **Note where sources disagree.** Conflicting dates or details are often where the interesting questions start.
- **Respect image licences.** Only add images you have the right to use, and credit them where possible.
- **Be respectful.** Challenge ideas, not people.

## Disclaimer

This is an independent research project that questions accepted history. The alternative views here are theories and open questions, not established fact. Readers are encouraged to check the sources and make up their own minds.
