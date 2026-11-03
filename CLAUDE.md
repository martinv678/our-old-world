# Research brief for Claude

This file is read automatically at the start of every Claude Code session in this repo. It sets out how to research and write entries for **Our Old World**. Follow it for every building.

> **Owner: fill in the sections marked ✏️.** They tell Claude which theories, sources and observations matter most to you. The rest can be left as it is.

---

## 1. What this project is

A collection of pre-1900 buildings, each looked at two ways: **the main story** (the accepted history) and **the alternative view** (the anomalies, and the alternative history theories that try to explain them). The project starts from the belief that our accepted history may be incomplete or wrong, and its job is to dig into that seriously.

The aim is to give the alternative view **real depth**: not a token paragraph, but the strongest version of the case, built from specific evidence. Every claim is also kept honest about how strong its evidence is, so the project is hard to dismiss.

## 2. How hard to push

- Give the alternative view **at least as much space and effort** as the main story.
- Look actively for anomalies. Don't stop at the official summary: check dates, quantities, records and images for things that don't add up.
- Present the alternative view in its strongest form, then show what would confirm or undermine it.
- Never invent evidence, sources, quotes or figures. If something is a hunch, label it as one.
- Use the evidence labels in section 6 on every anomaly.

## 3. Theories and themes to test ✏️

Test each building against these. Add, remove or reorder them to match what you think matters most.

- **Tartaria / an older civilisation:** was the building inherited from an earlier, more advanced culture and later claimed or re-dated?
- **Mud flood / buried levels:** buried ground floors, windows or doors below street level, raised streets, basements that look like former ground floors.
- **Reset around 1800–1900:** signs of a break in history, such as lost records, sudden rebuilding, or cities "rebuilt" after fires.
- **World's fairs:** were exhibition buildings presented as new, then removed by demolition or fire?
- **Fire and demolition:** grand buildings lost to fire or torn down soon after completion.
- **Lost energy technology:** domes, spires, towers, copper, mercury, electroplating, "electricity" symbolism.
- **Impossible timelines:** construction too fast, too large or too precise for the stated tools, workforce and budget.
- **Shared worldwide architecture:** the same domes, star forts and styles appearing on different continents at the same time.
- **Out-of-place buildings:** grand buildings in small towns, remote places or young cities.
- **Missing or convenient records:** plans that are lost, rediscovered at the right moment, or contradict each other.

✏️ *Add your own themes here:*

- **Satan's Little Season:** the view that the thousand years of Revelation 20 have already passed and we now live in the "little season" of deception. Ask whether the building belongs to an older age that was later claimed, and whether its records look rewritten. See [ALTERNATIVE-VIEW.md](ALTERNATIVE-VIEW.md).
- **Letters in dates (the "J" argument):** Fomenko's claim that the leading "1" in dates was originally an I or J for Jesus, adding about 1,000 years to history. Check date stones, foundation stones, inscriptions and documents for how the year is written, and record examples in the Anomaly log. Remember that a final "j" in Roman numerals (for example "xiij") is normal in older writing.

## 4. Owner's sources and researchers ✏️

List the researchers, channels, books and websites you rate. Claude will look for their arguments about each building and engage with them directly.

A suggested starting list (from [ALTERNATIVE-VIEW.md](ALTERNATIVE-VIEW.md)). Edit it to match who you rate:

- **Jon Levi** (YouTube): architectural anomalies, Tartaria
- **Martin Liedtke** (YouTube): mud flood, Tartaria
- **Sylvie Ivanowa** (YouTube): architectural anomalies
- **Stolen History** (stolenhistory.net): old photos, maps and theories
- **r/Tartaria** and **r/CulturalLayer** (Reddit)
- **Anatoly Fomenko and Gleb Nosovsky**: *New Chronology*
- **Nikolai Levashov**: "Great Tartaria"
- **Heribert Illig**: phantom time hypothesis
- **Graham Hancock** and **UnchartedX**: lost civilisations, precision stonework
- For counter-arguments to test against: **Skeptoid #765**, **Geographicus** on Tartary maps

## 5. Research methods to use on every building

Work through as many of these as the evidence allows.

1. **Records audit.** What primary records exist: plans, contracts, invoices, construction photos, newspaper reports, official inquiries? Note where they're held and where the gaps are.
2. **Timeline check.** Estimate the materials and labour against the recorded dates and workforce. Show the working, and say whether the timeline is plausible, tight or implausible.
3. **Ground-level check.** Compare the oldest available photos, engravings and maps with today. Look for buried windows and doors, steps down into entrances, and raised streets.
4. **Photo analysis.** For key historic images, check lighting and shadows, edges, perspective, retouching and captions. Say what resolution the analysis is based on.
5. **Map check.** What do the oldest maps show on the site before the official build date?
6. **Comparison buildings.** Find buildings elsewhere with the same features or dimensions, built at about the same time, and link to their entries if they exist.
7. **Lost and changed parts.** What has been demolished, burned, removed, rebuilt or covered up, and when?
8. **Primary sources first.** Prefer period newspapers, books, journals, plans and photographs over modern summaries. Useful archives include the Internet Archive, Library of Congress, Gallica, Trove, Europeana and Wikimedia Commons. If a site is blocked by this environment's network settings, say which domain needs allowing rather than skipping it silently.
9. **Read the owner's notes.** If an entry contains a **Research notes** section or `<!-- notes -->` comments, read them first and build on them.

## 6. Evidence labels

Tag each anomaly or claim in the alternative view with one of these:

| Label | Meaning |
|---|---|
| **Documented** | Confirmed by primary records or several independent reliable sources |
| **Observed** | Visible in photos, maps or on site, but not yet explained |
| **Reported** | Stated by a secondary source, not yet verified |
| **Speculative** | A hypothesis or hunch, with no direct evidence yet |

## 7. Entry structure

Each building lives at `places/<country>/<building-name>/<building-name>.md`, with images in an `images/` folder beside it. Use this structure. When you revisit an older entry, add any sections it's missing.

```markdown
# Building Name

| | |
|---|---|
| **Location** | Address, town, region, country |
| **Near** | Nearest well-known place |
| **Built** | Year(s) |
| **Architect** | Name (if known) |
| **Style** | |
| **Type** | Railway station, Hotel |
| **Original use** | |
| **Status** | In use / Abandoned / Demolished / Restored |
| **Features** | Dome, Tower |

![Description](images/main.jpg)
*Caption with date, author, source and licence.*

## Overview

## The main story

Dated bullet points of the accepted history.

## The alternative view

### <Anomaly or theme>  (one subsection per point, each with an evidence label)

### Anomaly log

| Anomaly | Evidence | Label | Source |
|---|---|---|---|

### Timeline check

Materials, workforce and time: the working and the verdict.

### Comparison buildings

Similar buildings elsewhere, with links.

### What would support the alternative view

### What would weaken it

## Open questions for contributors

## Leads to follow up

Specific archives, documents, photos or people that could move the research on.

## Research notes

Space for the owner's own observations and hunches. Claude reads this first and doesn't remove it.

## Images

## Sources
```

The **Type** and **Features** rows drive the generated Buildings list in `README.md` and the glossary in `GLOSSARY.md`. Use existing names from those lists where possible; a new feature gets a placeholder glossary section that should then be written properly.

## 8. Images

- Use only images that are public domain or freely licensed (for example from Wikimedia Commons), or that the owner has supplied.
- Name files in short lowercase words with hyphens, and keep them under about 1600px wide.
- Every image needs a description and a caption with date, author, source and licence.
- Historic photos, postcards, engravings and maps are the most valuable, especially ones that show ground levels, construction or lost parts.

## 9. Housekeeping after every change

1. Add the building to `links/research-list.md` (change ⬜ to ✅ and link it), and add any newly found candidates to the list.
2. Run `python3 scripts/build_index.py` to update the Buildings list, glossary and links.
3. Check the website builds: `python3 scripts/build_site.py && mkdocs build --strict`.
4. Write in plain British English, with dates as "1 May 1851" or "1883–1884".

## 10. Git ✏️

The owner's current preference: commit work with a clear message and push it to `main` once the checks above pass. Edit this if that changes.
