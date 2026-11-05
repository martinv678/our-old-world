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
- **Materials and delivery.** Millions of bricks and tons of stone and iron, made and carried by horse, barge and early railway, for many great buildings going up at once. Could the country really have supplied it all?
- **Missing construction photographs.** Buildings in older styles with no photographs of them being built. Do the gaps follow the style, suggesting the buildings are older than the records say?
- **Sound and cymatics.** Rose windows that match the patterns sound makes, and organs and bells that turn buildings into instruments. Did the builders design them for sound?
- **Skill and precision.** Complex stone, brick and iron work needing large numbers of master craftsmen who got it right first time. Were there enough of them, and were there mistakes?
- **Mud flood and buried floors.** Ground floors and windows below today's street level, raised streets, and buildings that appear to have been dug out.
- **Shared architecture worldwide.** The same domes, columns and proportions turning up on different continents at around the same time.
- **Purpose and abandonment.** Buildings that seem far too grand for their stated use, or that were abandoned or demolished soon after being finished.
- **Missing or thin records.** Gaps in architects' records, construction photos, plans or costs.
- **Old maps, photos and postcards.** Early images that show things the official story doesn't explain.

For where these ideas come from, how they apply to the buildings here, and **people to watch and read**, see [The alternative view](ALTERNATIVE-VIEW.md).

## Repository structure

```
our-old-world/
├── README.md
├── CLAUDE.md                       # Research brief: how entries are researched and written
├── GLOSSARY.md                     # Features index (domes, towers, rose windows...)
├── TIMELINE.md                     # Buildings in date order (generated)
├── FIRES.md                        # Buildings damaged by fire or bombing (generated)
├── ALTERNATIVE-VIEW.md             # The theories explained, and people to watch
├── mkdocs.yml                      # Website settings
├── assets/                         # Website styles
├── scripts/
│   ├── build_index.py              # Rebuilds the Buildings list and the glossary
│   └── build_site.py               # Prepares the website build
├── links/
│   ├── research-list.md            # Buildings to add, with progress ticks
│   ├── image-shortlist.md          # Freely licensed images to add
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
**Jump to:** [Bridge](#bridge) (1) · [Casino](#casino) (1) · [Castle](#castle) (2) · [Cathedral](#cathedral) (2) · [Concert hall](#concert-hall) (2) · [Exhibition hall](#exhibition-hall) (5) · [Glasshouse](#glasshouse) (1) · [Government building](#government-building) (1) · [Historic district](#historic-district) (1) · [Hotel](#hotel) (1) · [Law court](#law-court) (2) · [Monument](#monument) (1) · [Museum](#museum) (2) · [Palace](#palace) (1) · [Planned town](#planned-town) (1) · [Railway station](#railway-station) (4) · [Shopping arcade](#shopping-arcade) (1) · [Star fort](#star-fort) (2) · [Street level](#street-level) (1) · [Theatre](#theatre) (1) · [Town hall](#town-hall) (2) · [Villa](#villa) (2)

### Bridge

| Building | Country | Built | Status |
|---|---|---|---|
| [Tower Bridge](places/uk/tower-bridge/tower-bridge.md) | UK | 1886–1894 | In use. Grade I listed. Walkways and engine rooms open as an exhibition |

### Casino

| Building | Country | Built | Status |
|---|---|---|---|
| [Villa Sultana (Villa "La Sultana")](places/italy/villa-sultana/villa-sultana.md) | Italy | 1883–1884 | Abandoned / derelict |

### Castle

| Building | Country | Built | Status |
|---|---|---|---|
| [Castello di Sammezzano](places/italy/castello-di-sammezzano/castello-di-sammezzano.md) | Italy | Early 1600s; remodelled c. 1853–1889 | Abandoned since 1990 |
| [Rocchetta Mattei](places/italy/rocchetta-mattei/rocchetta-mattei.md) | Italy | From 1850, on the ruins of a medieval fortress; extended until the 1890s | Restored by Fondazione Carisbo |

### Cathedral

| Building | Country | Built | Status |
|---|---|---|---|
| [Cologne Cathedral](places/germany/cologne-cathedral/cologne-cathedral.md) | Germany | Begun 1248; work stopped 1473; resumed 1842; completed 1880 | In use |
| [Saint Isaac's Cathedral](places/russia/saint-isaacs-cathedral/saint-isaacs-cathedral.md) | Russia | 1818–1858 | Museum, with church services held |

### Concert hall

| Building | Country | Built | Status |
|---|---|---|---|
| [Royal Albert Hall](places/uk/royal-albert-hall/royal-albert-hall.md) | UK | 1867–1871 | In use as a concert hall. Grade I listed. Renovated 1996–2004 |
| [St George's Hall, Liverpool](places/uk/st-georges-hall-liverpool/st-georges-hall-liverpool.md) | UK | 1841–1854 (foundation stone 1838; small concert room finished 1856) | In use as a venue. Grade I listed. Courts closed 1984 |

### Exhibition hall

| Building | Country | Built | Status |
|---|---|---|---|
| [Royal Exhibition Building](places/australia/royal-exhibition-building/royal-exhibition-building.md) | Australia | 1879–1880 | In use as an exhibition venue |
| [Palais du Trocadéro](places/france/palais-du-trocadero/palais-du-trocadero.md) | France | 1876–1878 | Largely demolished 1935–1937 |
| [Alexandra Palace](places/uk/alexandra-palace/alexandra-palace.md) | UK | First palace c. 1865–1873 (burned 1873); rebuilt 1873–1875 | In use as an events venue. Burned 1873, rebuilt 1875 |
| [The Crystal Palace](places/uk/crystal-palace/crystal-palace.md) | UK | 1850–1851; dismantled and rebuilt larger at Sydenham 1852–1854 | Destroyed by fire 1936 |
| [Palace of Fine Arts, Chicago](places/usa/palace-of-fine-arts-chicago/palace-of-fine-arts-chicago.md) | USA | 1891–1893; rebuilt in stone c. 1929–1933 | In use as the Griffin Museum of Science and Industry |

### Glasshouse

| Building | Country | Built | Status |
|---|---|---|---|
| [Palm House, Kew Gardens](places/uk/palm-house-kew/palm-house-kew.md) | UK | 1844–1848 | In use. Grade I listed, within the Kew World Heritage Site. Restored 1955–57 and 1985–88 |

### Government building

| Building | Country | Built | Status |
|---|---|---|---|
| [Palace of Westminster and Elizabeth Tower](places/uk/palace-of-westminster/palace-of-westminster.md) | UK | Rebuilt c. 1840–1870 after the fire of 1834; clock tower completed c. 1859 | In use |

### Historic district

| Building | Country | Built | Status |
|---|---|---|---|
| [Seattle Underground](places/usa/seattle-underground/seattle-underground.md) | USA | Streets and buildings mostly 1889–1890s; streets raised in the years after 1889 | Partly accessible on guided tours |

### Hotel

| Building | Country | Built | Status |
|---|---|---|---|
| [St Pancras Station and Midland Grand Hotel](places/uk/st-pancras/st-pancras.md) | UK | Train shed 1865–1868; hotel 1868–1876 | In use as St Pancras International station and the St Pancras Renaissance Hotel |

### Law court

| Building | Country | Built | Status |
|---|---|---|---|
| [Royal Courts of Justice](places/uk/royal-courts-of-justice/royal-courts-of-justice.md) | UK | 1873–1882 | In use as law courts. Grade I listed |
| [St George's Hall, Liverpool](places/uk/st-georges-hall-liverpool/st-georges-hall-liverpool.md) | UK | 1841–1854 (foundation stone 1838; small concert room finished 1856) | In use as a venue. Grade I listed. Courts closed 1984 |

### Monument

| Building | Country | Built | Status |
|---|---|---|---|
| [Scott Monument](places/uk/scott-monument/scott-monument.md) | UK | 1840–1844 (inaugurated 1846) | Standing |

### Museum

| Building | Country | Built | Status |
|---|---|---|---|
| [Natural History Museum](places/uk/natural-history-museum/natural-history-museum.md) | UK | 1873–1881 | In use as a museum. Listed building |
| [Palace of Fine Arts, Chicago](places/usa/palace-of-fine-arts-chicago/palace-of-fine-arts-chicago.md) | USA | 1891–1893; rebuilt in stone c. 1929–1933 | In use as the Griffin Museum of Science and Industry |

### Palace

| Building | Country | Built | Status |
|---|---|---|---|
| [Royal Pavilion, Brighton](places/uk/royal-pavilion-brighton/royal-pavilion-brighton.md) | UK | 1787 (Marine Pavilion); rebuilt and extended c. 1815–1823 | Museum, run by Brighton & Hove Museums |

### Planned town

| Building | Country | Built | Status |
|---|---|---|---|
| [Palmanova](places/italy/palmanova/palmanova.md) | Italy | Founded 7 October 1593; outer ring added in the early 19th century | Inhabited town |

### Railway station

| Building | Country | Built | Status |
|---|---|---|---|
| [Anhalter Bahnhof](places/germany/anhalter-bahnhof/anhalter-bahnhof.md) | Germany | 1876–1880, replacing a station of 1841 | Demolished 1959–1960 |
| [Dresden Hauptbahnhof](places/germany/dresden-hauptbahnhof/dresden-hauptbahnhof.md) | Germany | 1892–1898 | In use |
| [Frankfurt (Main) Hauptbahnhof](places/germany/frankfurt-hauptbahnhof/frankfurt-hauptbahnhof.md) | Germany | 1883–1888 | In use |
| [St Pancras Station and Midland Grand Hotel](places/uk/st-pancras/st-pancras.md) | UK | Train shed 1865–1868; hotel 1868–1876 | In use as St Pancras International station and the St Pancras Renaissance Hotel |

### Shopping arcade

| Building | Country | Built | Status |
|---|---|---|---|
| [Galleria Vittorio Emanuele II](places/italy/galleria-vittorio-emanuele-ii/galleria-vittorio-emanuele-ii.md) | Italy | 1865–1877 | In use as a luxury shopping arcade |

### Star fort

| Building | Country | Built | Status |
|---|---|---|---|
| [Palmanova](places/italy/palmanova/palmanova.md) | Italy | Founded 7 October 1593; outer ring added in the early 19th century | Inhabited town |
| [Goryōkaku](places/japan/goryokaku/goryokaku.md) | Japan | c. 1857–1866 (sources differ) | Public park |

### Street level

| Building | Country | Built | Status |
|---|---|---|---|
| [Seattle Underground](places/usa/seattle-underground/seattle-underground.md) | USA | Streets and buildings mostly 1889–1890s; streets raised in the years after 1889 | Partly accessible on guided tours |

### Theatre

| Building | Country | Built | Status |
|---|---|---|---|
| [Lyceum Theatre, Newport](places/uk/lyceum-theatre-newport/lyceum-theatre-newport.md) | UK | c. 1867 as the Victoria Assembly Rooms; gutted by fire 1896; rebuilt inside as the Lyceum Theatre 1896–1897 | Demolished 1961. The site was used for an ABC cinema (1968) and is now a Travelodge and car park |

### Town hall

| Building | Country | Built | Status |
|---|---|---|---|
| [Leeds Town Hall](places/uk/leeds-town-hall/leeds-town-hall.md) | UK | 1853–1858 (tower added to the design in 1856; altered 1877) | In use as a concert and events venue. Grade I listed |
| [Manchester Town Hall](places/uk/manchester-town-hall/manchester-town-hall.md) | UK | 1868–1877 | Grade I listed. Closed since 2018 for restoration |

### Villa

| Building | Country | Built | Status |
|---|---|---|---|
| [Villa Crespi](places/italy/villa-crespi/villa-crespi.md) | Italy | From 1879 | In use as a hotel and restaurant |
| [Villa Sultana (Villa "La Sultana")](places/italy/villa-sultana/villa-sultana.md) | Italy | 1883–1884 | Abandoned / derelict |
<!-- catalogue:end -->

The [research list](links/research-list.md) has over 100 more pre-1900 buildings waiting to be added, with a tick next to each one that's done. Other leads are in [`links/poi.md`](links/poi.md).

## Timeline

Want to see the buildings in date order? The [timeline](TIMELINE.md) lists every building by when it was built, grouped by century, from medieval Cologne Cathedral to the 1890s.

## Fires

Want to see every building that burned? The [fires page](FIRES.md) lists every building in the project damaged or destroyed by fire, and those damaged by bombing in war, with what happened and links to each entry.

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

One subsection per anomaly or theme, each tagged Documented, Observed,
Reported or Speculative. For example: construction too fast, buried floors,
architecture matching buildings elsewhere, gaps in the records, or old
photos and maps that raise questions.

### Anomaly log

| Anomaly | Evidence | Label | Source |
|---|---|---|---|

### Timeline check

Materials, workforce and time against the official dates.

### Comparison buildings

Similar buildings elsewhere, with links.

### What would support the alternative view

### What would weaken it

## Open questions for contributors

Things that still need checking or that contributors could help with.

## Leads to follow up

Archives, documents, photos or people that could move the research on.

## Research notes

Your own observations and hunches.

## Images

## Sources

Links for both the main story and the alternative view.
```

The full research brief, including the research methods and evidence labels, is in [`CLAUDE.md`](https://github.com/martinv678/our-old-world/blob/main/CLAUDE.md).

## Website

The repo is also published as a website with search, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and hosted on GitHub Pages at <https://ourold.world/>. It rebuilds automatically every time a change reaches `main`.

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
