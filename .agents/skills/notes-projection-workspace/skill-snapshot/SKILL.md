---
name: notes-projection
version: 2
description: |
  Use this skill when the user wants to generate a comprehensive, atomic, deeply
  interconnected Obsidian knowledge base on any topic. The skill runs a 5-phase
  agent swarm: map the topic into 3 MOC buckets + ~24 atomic concepts → research
  each concept with WebSearch + source URLs → write one atomic note per concept
  with Mermaid diagrams and dataview-friendly frontmatter → run a link-critic
  pass that fixes broken/orphan wikilinks → emit a master index, per-bucket
  MOCs, and a glossary.

  v2 changes from v1: atomic notes (one concept per file), MOC hierarchy, source
  provenance in frontmatter, link-budget enforcement (≥5 outgoing wikilinks per
  note), required Mermaid diagram, automatic link audit + repair.

  Triggered by: "make notes on X", "notes projection for X", "cover everything
  about X in my vault", "build notes swarm for X", "project notes on X",
  "/notes-projection".
---

# Notes Projection (v2)

Generate an **atomic**, **MOC-structured**, **link-audited** Obsidian
knowledge base on any topic using a coordinated 5-phase agent swarm.

Unlike v1 (one giant note per subtopic, shallow cross-links, no source
provenance), v2 produces:

- ~24 **atomic notes** (one concept per file, ~200 words each)
- 3 **MOC buckets** (Foundations / Mechanisms / Applications by default,
  or whatever fits the topic)
- **Dataview-friendly frontmatter** on every note (status, bucket, sources,
  connections — queryable in Obsidian)
- **Mermaid diagrams** embedded in major notes (renders natively in Obsidian)
- **Source URLs** preserved in every note (audit-able claims)
- **Link-critic pass** that repairs broken wikilinks, links orphans, and
  strengthens weak-link notes
- **Per-bucket MOCs** + a master index + a glossary (3 separate files)

---

## Step 0 — Gather Inputs

If the topic and vault path were not provided in the invocation, ask:
1. **Topic** — e.g. "Psychology", "Quantum Mechanics", "Roman History"
2. **Vault path** — absolute path to the Obsidian vault, e.g. `/home/ali/psycology`

Confirm both before proceeding. `mkdir -p` the vault if it doesn't exist.

**Topic-size guard:** if the user gives a one-word topic (e.g. "Physics"),
ask whether they mean the full field or a specific sub-area. The mapper
agent will surface ~24 atomic concepts; for huge fields like "Physics" the
output may overwhelm. Suggest a sub-area (e.g. "Quantum Mechanics") and
confirm before dispatching.

---

## Step 1 — Create Task Tracking

Use `TaskCreate` for each phase. One task per phase, plus one per agent
batch (so the spinner shows real progress):

- `phase-1-map` — Mapper agent
- `phase-2-research-batch-1` through `…-N` — one task per batch of 5
  researchers (ceil(24 / 5) = 5 batches)
- `phase-3-write-batch-1` through `…-N` — one per writer batch
- `phase-4-link-critic` — single link-critic agent
- `phase-5-index-mocs-glossary` — indexer agent

Mark each `in_progress` when starting, `completed` when done. If any
agent returns partial output, mark its task as `in_progress` with a
note ("12 of 14 notes written — 2 retries pending") rather than
`completed`.

---

## Step 2 — Phase 1: Mapper

Dispatch **one agent**. The mapper's job is to produce a **3-layer plan**
that the downstream phases consume verbatim. The output must be a
structured plain-text block — no prose, no code fences — so the next
phases can parse it.

```
You are a knowledge mapper for the topic: "<TOPIC>"

Your job is to produce a 3-layer plan that downstream agents will use
WITHOUT further interpretation. Be specific — every atomic concept
becomes a file. Every bucket becomes a MOC.

Use WebSearch to confirm the canonical breakdown of this field
(Wikipedia, academic sources, textbooks). Cross-reference ≥3 sources
to avoid idiosyncratic splits.

LAYER 1: BUCKETS
  Define exactly 3 MOC buckets that organize the topic. They should
  cover the field without overlap. Suggested shapes (adapt to the topic):
    - Foundations: history, definitions, key figures, theory
    - Mechanisms: how it works, processes, structures, math
    - Applications: real-world uses, case studies, current research
  But you MAY use any 3 buckets that fit the topic. For "Photosynthesis"
  the natural split is "Light Reactions / Calvin Cycle / Ecological Role".
  For "Stoicism" it might be "Origins / Doctrine / Practice".

LAYER 2: SUBTOPICS
  Define 6-10 subtopics. Each subtopic belongs to exactly ONE bucket.
  For each subtopic, give a one-line description and 2-4 atomic concepts.

LAYER 3: ATOMIC CONCEPTS
  Per subtopic, list 2-4 atomic concepts. Each atomic concept becomes
  one file in the vault. Aim for 18-28 atomic concepts total (sweet spot
  for 5 batches of 5). Each atomic concept must be:
    - A single, well-defined idea (not a compound)
    - Likely to have 150-300 words of substantive content
    - Connected to ≥2 other atomic concepts in the plan

OUTPUT FORMAT (plain text, no code fences):

TOPIC: <Main Topic>
TOPIC_SLUG: <lowercase-dash-separated>
DESCRIPTION: <2-3 sentence overview>

BUCKETS:
1. <Bucket 1 Name> — <one-line description>
2. <Bucket 2 Name> — <one-line description>
3. <Bucket 3 Name> — <one-line description>

SUBTOPICS:
1. <Subtopic Name>
   BUCKET: <Bucket N>
   DESCRIPTION: <one line>
   ATOMIC_CONCEPTS:
     - <Atomic Concept 1> — <one line>
     - <Atomic Concept 2> — <one line>
     - <Atomic Concept 3> — <one line>

2. <Subtopic Name>
   BUCKET: <Bucket N>
   DESCRIPTION: <one line>
   ATOMIC_CONCEPTS:
     - <Atomic Concept 1> — <one line>
     - <Atomic Concept 2> — <one line>

[continue for ALL subtopics — 6-10 total]

CROSS_DOMAIN_FIELDS:
- <Field 1>: <why it connects to this topic>
- <Field 2>: <why it connects>
- <Field 3>: <why it connects>
[aim for 5-10 cross-domain fields — these become tags in notes]

KEY_FIGURES:
- <Name 1>: <contribution>
- <Name 2>: <contribution>
[aim for 8-15 key figures — these become bold mentions in notes]

KEY_CONCEPTS_GLOSSARY:
- <Term 1>: <one-line definition>
- <Term 2>: <one-line definition>
[aim for 20+ terms — these are the atomic concepts PLUS a few
supporting terms that don't get their own file]

After producing the block, return the literal string: MAPPER_DONE
```

Parse the mapper's output into:
- `TOPIC`, `TOPIC_SLUG`, `DESCRIPTION`
- `BUCKETS[]`: name, description
- `SUBTOPICS[]`: name, bucket, description, atomic_concepts[]
- `CROSS_DOMAIN_FIELDS[]`, `KEY_FIGURES[]`, `KEY_CONCEPTS_GLOSSARY[]`

Compute every atomic concept's slug and full path:
- slug = lowercase, spaces→dashes, strip punctuation
- path = `<vault_path>/<TOPIC_SLUG>/<bucket-slug>/<concept-slug>.md`

Persist the parsed plan to `<vault_path>/<TOPIC_SLUG>/.plan` (plain
text, the same block) so downstream agents can read it from disk
instead of receiving the whole thing inline. Saves tokens.

---

## Step 3 — Phase 2: Researchers (parallel batches of 5)

Split atomic concepts into batches of 5. For each batch, dispatch all 5
agents IN PARALLEL (single message, multiple `Agent` tool calls).

Each researcher agent prompt:

```
You are a deep research agent. Research this atomic concept for an
Obsidian knowledge base.

ATOMIC CONCEPT: <Atomic Concept Name>
TOPIC: <Main Topic>
BUCKET: <Bucket Name>
SUBTOPIC: <parent subtopic>
VAULT PATH: <vault_path>
NOTE FILE PATH: <vault_path>/<topic-slug>/<bucket-slug>/<concept-slug>.md
TODAY'S DATE: <YYYY-MM-DD>

Use WebSearch (3-5 searches) to gather current, accurate information.
Prefer authoritative sources: Wikipedia, .edu, peer-reviewed papers,
established encyclopedias. AVOID SEO spam, random blogs, AI-generated
content farms.

Save your research to: <vault_path>/<topic-slug>/.research/<concept-slug>.md
Use the Write tool to save it. Then return the structured output below.

OUTPUT FORMAT (return this text, do not write it to a file):

CONCEPT: <Atomic Concept Name>
SLUG: <concept-slug>
DEFINITION: <2-3 sentence precise definition>

KEY_POINTS:
- <Point 1>: <2-3 sentence explanation>
- <Point 2>: <2-3 sentence explanation>
- <Point 3>: <2-3 sentence explanation>
- <Point 4>: <2-3 sentence explanation>
- <Point 5>: <2-3 sentence explanation>
[4-7 points; each becomes a bullet in the note's body]

SOURCES:
- <url1> | <source title> | accessed <YYYY-MM-DD>
- <url2> | <source title> | accessed <YYYY-MM-DD>
- <url3> | <source title> | accessed <YYYY-MM-DD>
[minimum 3 sources; aim for 5+]

WIKILINK_TARGETS:
- <Exact Title of another atomic concept in this plan>
- <Exact Title of another atomic concept>
- <Exact Title of another atomic concept>
- <Exact Title of another atomic concept>
- <Exact Title of another atomic concept>
[minimum 5 targets; titles must match the EXACT subtopic/atomic-concept
names from the mapper plan — the writer will use these as [[wikilinks]]]

CROSS_DOMAIN_TARGETS:
- <Cross-domain field from the mapper's CROSS_DOMAIN_FIELDS list>
- <Another cross-domain field>
[1-3 cross-domain fields this concept intersects with]

DIAGRAM:
<mermaid>
<mermaid code here, 5-15 lines>
</mermaid>
[Required. Use flowchart, sequence, or class diagram. Pick the
type that best illustrates THIS concept. Example: a flowchart for
a process, a class diagram for entities+relations, a sequence diagram
for interactions over time.]

KEY_FIGURES_MENTIONED:
- <Name>: <one-line role in this concept>
[0-3 names — only if directly relevant]

FURTHER_READING:
- <Book/Paper/Resource>: <why valuable>
[2-4 resources]

After returning the structured output, end with: RESEARCH_DONE
```

Collect all `RESEARCH_DONE` markers before moving to Phase 3. The
persisted `.research/<slug>.md` files serve as the writer's source of
truth — the writer reads the file rather than receiving the structured
output inline.

**Failure mode:** if a researcher fails to write its `.research/` file,
retry once with a simpler prompt ("just do 2 WebSearches and return
the same format"). If the retry also fails, log the failure and skip
that concept in the writer phase — the indexer will note it as missing.

---

## Step 4 — Phase 3: Writers (parallel batches of 5)

Same batching discipline (5 per batch). Each writer reads its concept's
`.research/<slug>.md` from disk and produces the actual note.

Each writer agent prompt:

```
You are an Obsidian note writer. Convert the research file at
<vault_path>/<topic-slug>/.research/<concept-slug>.md into a
production-quality atomic Obsidian note.

OUTPUT FILE: <vault_path>/<topic-slug>/<bucket-slug>/<concept-slug>.md
TODAY'S DATE: <YYYY-MM-DD>

ALL ATOMIC CONCEPT TITLES (for [[wikilink]] consistency — use these EXACT strings):
<paste the full list of atomic concept names from the mapper plan, one per line>

ALL CROSS-DOMAIN FIELDS (for [[wikilink]] consistency):
<paste CROSS_DOMAIN_FIELDS list>

RESEARCH FILE CONTENTS:
<paste the .research/<slug>.md file contents here>

Use the Write tool to create the note at the path above. Use this EXACT frontmatter schema (dataview-friendly):

---
title: <Atomic Concept Title>
topic: <Main Topic>
bucket: <Bucket Name>
tags: [<topic-slug>, <bucket-slug>, <concept-slug>]
aliases: [<alt name if any>]
status: seedling
created: <YYYY-MM-DD>
sources: [<url1>, <url2>, <url3>]
connections: [<Other Concept 1>, <Other Concept 2>, <Other Concept 3>, <Other Concept 4>, <Other Concept 5>]
---

# <Atomic Concept Title>

> <One-sentence definition — clearest, most precise summary>

## Overview

<3-5 sentence overview: what this is, why it matters, where it sits
in the topic's structure. Reference the parent [[<Subtopic Name>]]
and the bucket [[<Bucket Name>]] MOC explicitly.>

## Key Points

- **<Point 1>**: <2-3 sentences>
- **<Point 2>**: <2-3 sentences>
- **<Point 3>**: <2-3 sentences>
- **<Point 4>**: <2-3 sentences>
- **<Point 5>**: <2-3 sentences>
[Every point from the researcher's KEY_POINTS, as prose bullets]

## Diagram

<mermaid>
<the researcher's DIAGRAM block, verbatim — do not modify>
</mermaid>

## Connections

### Within <Main Topic>
- [[<WIKILINK_TARGET 1>]] — <one-line reason for connection>
- [[<WIKILINK_TARGET 2>]] — <one-line reason for connection>
- [[<WIKILINK_TARGET 3>]] — <one-line reason for connection>
- [[<WIKILINK_TARGET 4>]] — <one-line reason for connection>
- [[<WIKILINK_TARGET 5>]] — <one-line reason for connection>
[MINIMUM 5 outgoing wikilinks — enforced. Use the WIKILINK_TARGETS
from the research. If the research gave you fewer than 5, add more
by referencing the parent [[<Subtopic>]], the bucket
[[<Bucket>]] MOC, and 1-2 atomic concepts you discovered while
reading the research file.]

### Cross-Domain
- [[<Cross-Domain Field 1>]] — <how this concept connects>
- [[<Cross-Domain Field 2>]] — <how this concept connects>

## Sources

- <Source title> — <url>
- <Source title> — <url>
- <Source title> — <url>
[Every source from the researcher's SOURCES list]

## Further Reading

- *<Title>* — <why valuable>
- *<Title>* — <why valuable>

---
*Part of [[<Main Topic>-Index]] · [[<Bucket Name>]] MOC · [[<Subtopic Name>]]*

After writing the file, return: WRITTEN: <file_path>
```

**Link budget hard rule:** every note must have ≥5 outgoing `[[wikilinks]]`
in the `## Connections` section. If the researcher's WIKILINK_TARGETS
was sparse, top up with the parent subtopic, the bucket MOC, and any
atomic concept mentioned in the body. Do not skip this — the link
budget is what makes the v2 vault navigable.

**Atomicity check:** if the resulting note is <100 words of body, the
concept was too small to be its own file. In that case, do NOT write
a separate file. Instead, append the content to a `_merged.md` file
at `<vault_path>/<topic-slug>/<bucket-slug>/_merged.md` and report
`MERGED: <atomic-concept> into <parent-subtopic>`. The link-critic
will treat merged content as part of the parent.

---

## Step 5 — Phase 4: Link-Critic

Dispatch **one** agent (not parallelized — it needs a coherent view of
the whole vault). This is the key v2 addition that makes the network
of notes actually navigable.

```
You are a link-critic for an Obsidian vault. Your job is to find and
fix problems in the link graph of a freshly-generated knowledge base.

VAULT PATH: <vault_path>
TOPIC: <Main Topic>
TOPIC_SLUG: <topic-slug>
TODAY'S DATE: <YYYY-MM-DD>

ALGORITHM

1. INVENTORY. Glob every *.md file under:
   - <vault_path>/<topic-slug>/              (atomic notes)
   - <vault_path>/<topic-slug>/_MOC/         (MOC files, may not exist yet)
   - <vault_path>/<topic-slug>/_Glossary.md  (may not exist yet)
   - <vault_path>/<topic-slug>-Index.md      (master index, may not exist yet)

   Build `existing_titles`: set of every `title:` value from frontmatter
   PLUS every `# <Heading 1>` value (in case title: is missing).

2. EXTRACT LINKS. For every file, extract every [[wikilink]] — both
   the simple form [[Title]] and the alias form [[Title|display]].
   For each link, record (source_file, target_title, line_number).

3. CLASSIFY each link:
   - RESOLVED: target_title in existing_titles
   - BROKEN: target_title NOT in existing_titles
   - AMBIGUOUS: target_title matches multiple titles (e.g. partial
     match) — flag for human attention, do NOT auto-fix

4. CLASSIFY each note:
   - ORPHAN: zero incoming links (no other file links TO it)
   - WEAK: fewer than 3 outgoing RESOLVED links
   - HEALTHY: ≥3 outgoing RESOLVED links AND ≥1 incoming link

5. REPORT. Write the audit to
   <vault_path>/<topic-slug>/.link-audit-<YYYY-MM-DD>.md with sections:
   - ## Summary: counts of broken/weak/orphan/healthy
   - ## Broken Links: table of (source_file, target, line)
   - ## Orphan Notes: list
   - ## Weak Notes: list with their current outgoing count
   - ## Repair Plan: ordered list of edits you will make

6. APPLY REPAIRS. For each issue:
   - BROKEN link: try the closest existing title (case-insensitive,
     then prefix match). If a match exists, Edit the source file to
     change [[Broken]] to [[Resolved Title]]. If no match, change
     [[Broken]] to plain text (just "Broken") and add a parenthetical
     "(unresolved link — review manually)".
   - ORPHAN note: Read the file, pick 2-3 atomic concepts in the same
     bucket that share a topic, and append a "## Connections" section
     with 2-3 [[wikilinks]] to those notes. Each line is one link plus
     a one-sentence reason.
   - WEAK note: Read the file, identify 1-2 concepts already mentioned
     in the body that have their own notes, and add them to the
     "## Connections" section. Do not pad with tangential links —
     only meaningful ones.

7. RE-AUDIT. After applying repairs, re-run the classification. If
   broken >5% of total, log "INCOMPLETE REPAIR" — that signals the
   writer phase had a slug-drift problem.

8. RETURN FORMAT (do not write to a file, return as text):
   LINK AUDIT: <N> notes audited
   BROKEN FIXED: <B>
   ORPHANS LINKED: <O>
   WEAK STRENGTHENED: <W>
   STILL BROKEN: <J> (gave up — review manually)
   AUDIT REPORT: <vault_path>/<topic-slug>/.link-audit-<YYYY-MM-DD>.md
```

The link-critic writes its own audit file to disk and returns the
counts. The final user-facing report (Step 7) quotes these counts.

---

## Step 6 — Phase 5: Indexer

Dispatch **one** agent. The indexer writes 3 files: the master index,
one MOC per bucket, and a glossary. Use the post-link-critic file
list (the link-critic's RE-AUDIT counts the canonical file inventory).

```
You are an Obsidian indexer. You produce the navigation layer for a
freshly-generated knowledge base.

VAULT PATH: <vault_path>
TOPIC: <Main Topic>
TOPIC_SLUG: <topic-slug>
TODAY'S DATE: <YYYY-MM-DD>

INPUTS (read these to get your data):
- <vault_path>/<topic-slug>/.plan           (the mapper's plan)
- <vault_path>/<topic-slug>/.link-audit-<YYYY-MM-DD>.md  (current state)
- Glob <vault_path>/<topic-slug>/**/*.md    (list of actual notes)

DELIVERABLES: write these 3+ files.

==============================================================
FILE 1: <vault_path>/<topic-slug>-Index.md   (master index)
==============================================================

---
title: <Main Topic>
topic: <Main Topic>
tags: [<topic-slug>, index, map-of-content]
created: <YYYY-MM-DD>
---

# <Main Topic> — Index

> <2-3 sentence overview from the mapper's DESCRIPTION>

## Recent Notes

```dataview
TABLE title, bucket, status, created
FROM "<topic-slug>"
WHERE type = "note"
SORT created DESC
LIMIT 20
```

## Topic Map

<Group atomic notes by bucket. Use the mapper's BUCKETS list. For each
bucket, show 2-3 entry-point notes first (most general), then the rest.>

### [[<Bucket 1 Name>]]
- [[<Entry-point concept 1>]] — <one-line description>
- [[<Entry-point concept 2>]] — <one-line description>
  - [[<Supporting concept A>]] — <one-line>
  - [[<Supporting concept B>]] — <one-line>
  - [[<Supporting concept C>]] — <one-line>
- [[<Other concept X>]] — <one-line>

### [[<Bucket 2 Name>]]
[...same structure...]

### [[<Bucket 3 Name>]]
[...same structure...]

## All Notes

| Note | Bucket | Status | Sources |
|---|---|---|---|
| [[<Atomic Concept 1>]] | [[<Bucket>]] | seedling | 3 |
| [[<Atomic Concept 2>]] | [[<Bucket>]] | seedling | 5 |
[one row per atomic note]

## Cross-Domain Connections

| Field | Connection to <Main Topic> |
|---|---|
| [[<Field 1>]] | <why it connects> |
| [[<Field 2>]] | <why it connects> |

## Key Figures

- **<Name 1>** — <contribution>
- **<Name 2>** — <contribution>

---
*Generated by notes-projection v2 on <date> · <N> atomic notes across <M> buckets*

==============================================================
FILE 2-4: <vault_path>/<topic-slug>/_MOC/<bucket-slug>.md
  (one per bucket — 3 files total)
==============================================================

For each bucket, write a MOC that curates a reading order through
the bucket's notes. The MOC is a chain of [[wikilinks]] with
one-sentence "why read this next" annotations.

---
title: <Bucket Name> — Map of Content
topic: <Main Topic>
bucket: <Bucket Name>
tags: [<topic-slug>, <bucket-slug>, moc]
created: <YYYY-MM-DD>
---

# <Bucket Name>

> <Bucket description from the mapper plan>

## Start here

- [[<Entry-point concept 1>]] — <why start here>
- [[<Entry-point concept 2>]] — <why start here>

## Foundational concepts

- [[<Concept A>]] — <one-line description>
- [[<Concept B>]] — <one-line description>

## Mechanisms / deeper dives

- [[<Concept C>]] — <one-line description>
- [[<Concept D>]] — <one-line description>

## Applications / case studies

- [[<Concept E>]] — <one-line description>

---
*Part of [[<Main Topic>-Index]]*

==============================================================
FILE 5: <vault_path>/<topic-slug>/_Glossary.md
==============================================================

---
title: <Main Topic> — Glossary
topic: <Main Topic>
tags: [<topic-slug>, glossary]
created: <YYYY-MM-DD>
---

# <Main Topic> — Glossary

Alphabetical list of all atomic concepts + supporting terms from the
mapper's KEY_CONCEPTS_GLOSSARY. One line per term.

| Term | Definition |
|---|---|
| <Atomic Concept 1> | <one-line definition> |
| <Atomic Concept 2> | <one-line definition> |
| <Supporting Term> | <one-line definition> |
[aim for 20+ entries — all atomic concepts + supporting terms]

---
*Generated by notes-projection v2 on <date>*

After writing all files, return:
INDEX_WRITTEN: <vault_path>/<topic-slug>-Index.md
MOCS_WRITTEN: <comma-separated list of MOC file paths>
GLOSSARY_WRITTEN: <vault_path>/<topic-slug>/_Glossary.md
```

---

## Step 7 — Report to User

After all phases complete, report:

```
Notes projection v2 complete for: <Main Topic>

Atomic notes: <N> in <M> buckets
  <vault_path>/<topic-slug>/<bucket1>/  — <K1> notes
  <vault_path>/<topic-slug>/<bucket2>/  — <K2> notes
  <vault_path>/<topic-slug>/<bucket3>/  — <K3> notes

Link audit: <N> notes audited
  <B> broken links fixed
  <O> orphan notes linked
  <W> weak notes strengthened
  <J> still-broken (review manually)
  Full report: <vault_path>/<topic-slug>/.link-audit-<date>.md

Navigation:
  <vault_path>/<topic-slug>-Index.md       — master index
  <vault_path>/<topic-slug>/_MOC/          — <M> per-bucket MOCs
  <vault_path>/<topic-slug>/_Glossary.md   — glossary

Sources: <S> unique source URLs across the vault.

Open your vault and start at: <topic-slug>-Index.md
```

---

## Key Rules (v2)

**Link budget.** Every atomic note must have ≥5 outgoing
`[[wikilinks]]` in its `## Connections` section. This is what makes
the v2 vault navigable. The link-critic enforces this; writers that
fall short fail review.

**Atomicity.** One concept per file. If a concept is <100 words of
substantive body, merge it into the parent subtopic's `_merged.md`
file and skip writing a separate file.

**Source provenance.** Every atomic note must have ≥3 source URLs in
its `## Sources` section AND in its frontmatter `sources:` array.
Claims without a source are scrubbed by the writer.

**Dataview schema.** Every note uses the exact same frontmatter
schema. `title`, `topic`, `bucket`, `tags`, `status`, `created`,
`sources`, `connections` are all required. `status` starts as
`seedling` — the user promotes to `budding` / `evergreen` as they
review the note.

**WikiLinks use exact titles.** `[[Cognitive Psychology]]` not
`[[cognitive-psychology]]` and not `[[Cognitive psychology]]`. The
slug is for the filename; the wikilink uses the title verbatim.

**Slug rules.** Lowercase, spaces→dashes, strip punctuation. "The
Light Reactions" → `the-light-reactions`. "C3 vs C4 Plants" →
`c3-vs-c4-plants`. Keep file names under 60 chars.

**No hallucination.** Researchers must use WebSearch. The writer
inherits the researcher's sources — it does NOT add its own citations
without going through a search.

**Parallel discipline.** Never dispatch more than 5 agents in one
batch. Use multiple sequential batches.

**Self-contained prompts.** Each agent gets ALL context it needs.
Reference disk paths for long inputs (.plan, .research files) rather
than pasting the content inline — saves tokens.

---

## Error Handling

- **Researcher fails.** Retry once with a simpler prompt ("just 2
  WebSearches, return the same format"). If it still fails, log and
  skip in the writer phase.
- **Writer produces <100 word note.** Merge into parent
  `_merged.md` per the atomicity rule. Do not write a thin file.
- **Link-critic finds >30% links broken.** That's a slug-drift signal —
  the writer phase used different conventions than the mapper.
  Re-dispatch the broken notes' writers with the canonical slug
  list, rather than patching links. Patch only if the drift is
  <10%.
- **Indexer misses a note.** The note will be unreachable from the
  index. Surface as a known-gap in the user report.
- **Vault path doesn't exist.** `mkdir -p` before any writer
  dispatches. Each bucket gets its own subdirectory
  (`<topic-slug>/<bucket-slug>/`).
- **Topic too broad** (e.g. "Science"). Mapper returns >30 atomic
  concepts. The writer phase becomes 7+ batches. Suggest the user
  narrow the topic and re-run.

---

## When NOT to use this skill

- **Updating an existing vault.** This skill generates from scratch.
  For incremental updates to an existing knowledge base, use a
  different skill (e.g. one that diffs the plan and only writes new
  notes).
- **Non-Obsidian targets.** The dataview blocks, Mermaid diagrams,
  and wikilink syntax are all Obsidian-specific. The notes render
  elsewhere, but the navigation layer is built for Obsidian.
- **Single-note requests.** If the user wants just one note on a
  topic, dispatch a single agent directly — no need for the full
  swarm.
