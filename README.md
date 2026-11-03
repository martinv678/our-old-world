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
├── scripts/
│   └── build_glossary.py           # Rebuilds the glossary from each entry's Features
├── links/
│   └── poi.md                      # Points of interest still to be researched
└── places/
    └── <country>/
        └── <building>/
            ├── <building>.md       # The write-up
            └── images/             # Photos, postcards, maps
```

Example: [`places/italy/villa-sultana/villa-sultana.md`](places/italy/villa-sultana/villa-sultana.md)

The town or city goes in the details table at the top of each entry and in the Buildings table below, not in the folder path.

## Buildings

| Building | Location | Built | Status |
|---|---|---|---|
| [Villa Sultana](places/italy/villa-sultana/villa-sultana.md) | Ospedaletti (near Sanremo), Italy | 1883–1884 | Abandoned |
| [Castello di Sammezzano](places/italy/castello-di-sammezzano/castello-di-sammezzano.md) | Reggello (near Florence), Italy | 1600s; remodelled c. 1853–1889 | Abandoned |
| [Rocchetta Mattei](places/italy/rocchetta-mattei/rocchetta-mattei.md) | Grizzana Morandi (near Bologna), Italy | 1850–1890s | Restored, open for visits |
| [Villa Crespi](places/italy/villa-crespi/villa-crespi.md) | Orta San Giulio, Italy | From 1879 | Hotel and restaurant |

Places still to be looked at are listed in [`links/poi.md`](links/poi.md).

## Glossary of features

Want to see every building with a dome, a tower or a rose window? The [glossary](GLOSSARY.md) lists architectural features, explains why each one interests the alternative view, and links to every building that has it.

## Adding a building

1. Check the building was built, or is said to have been built, **before 1900**.
2. Create a folder at `places/<country>/<building-name>/` using lowercase and hyphens (for example `places/uk/crystal-palace/`).
3. Add a `<building-name>.md` file using the template below.
4. Put any images in an `images/` folder next to it, and check the licence before uploading.
5. List its features in the **Features** row, using names from the [glossary](GLOSSARY.md). New features are fine too: the script will add a placeholder for them.
6. Add the building to the table above.
7. Run `python3 scripts/build_glossary.py` to update the glossary and links. If you skip this, it runs automatically on GitHub when the change reaches `main`.

### Entry template

```markdown
# Building Name

| | |
|---|---|
| **Location** | Address, town, region, country |
| **Built** | Year(s) |
| **Architect** | Name (if known) |
| **Style** | |
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

## Guidelines

- **Cite sources for both sides.** Link to the official records as well as the alternative research, so readers can follow the trail.
- **Keep the two clearly separate.** The main story section should say what the records say. Theories and questions belong in the alternative view.
- **Note where sources disagree.** Conflicting dates or details are often where the interesting questions start.
- **Respect image licences.** Only add images you have the right to use, and credit them where possible.
- **Be respectful.** Challenge ideas, not people.

## Disclaimer

This is an independent research project that questions accepted history. The alternative views here are theories and open questions, not established fact. Readers are encouraged to check the sources and make up their own minds.
