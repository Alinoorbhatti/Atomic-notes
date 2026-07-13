---
name: atomic-notes
version: 3
description: |
  Use this skill when the user wants to generate a comprehensive, atomic, deeply
  interconnected Obsidian knowledge base on any topic. The skill runs a 5-phase
  agent swarm: map the topic into 3 MOC buckets + ~24 atomic concepts → research
  each concept with WebSearch + source URLs → write one atomic note per concept
  with Mermaid diagrams and dataview-friendly frontmatter → run a link-critic
  pass that fixes broken/orphan wikilinks AND validates content quality → emit
  a master index, per-bucket MOCs, and a glossary.

  v3 changes from v2: content validation gates that reject placeholder/template
  outputs, mandatory web search enforcement in researchers, content quality
  auditing in the link-critic, enriched connection annotations, glossary
  definition pass-through, source URL validation. Also supports incremental
  updates to existing vaults and human-in-the-loop planning review.

  Triggered by: "make notes on X", "notes projection for X", "cover everything
  about X in my vault", "build notes swarm for X", "project notes on X",
  "atomic notes on X", "/notes-projection", "/atomic-notes".
---

# Atomic Notes (v3)

Generate an **atomic**, **MOC-structured**, **link-audited** Obsidian
knowledge base on any topic using a coordinated 5-phase agent swarm.

The core philosophy: **structure without substance is worthless.** Every note
must contain real, researched knowledge — not template placeholders. The
pipeline is designed to catch and reject hollow outputs at every stage.

This skill produces:

- ~24 **atomic notes** (one concept per file, 200-400 words of real content)
- 3 **MOC buckets** (Foundations / Mechanisms / Applications by default,
  or whatever fits the topic)
- **Dataview-friendly frontmatter** on every note (status, bucket, sources,
  connections — queryable in Obsidian)
- **Mermaid diagrams** embedded in every note (renders natively in Obsidian)
- **Source URLs** preserved in every note (real, verifiable URLs — not placeholders)
- **Link-critic pass** that repairs broken wikilinks, links orphans,
  strengthens weak-link notes, AND validates content quality
- **Per-bucket MOCs** + a master index + a glossary (with real definitions)

---

## Step 0 — Gather Inputs

If the topic and vault path were not provided in the invocation, ask:
1. **Topic** — e.g. "Psychology", "Quantum Mechanics", "Roman History"
2. **Vault path** — absolute path to the Obsidian vault, e.g. `/home/ali/psychology`

Confirm both before proceeding. `mkdir -p` the vault if it doesn't exist.

**Incremental Update Check:** Check if the topic directory `<vault_path>/<topic-slug>` already exists and contains markdown files. If it does, present a prompt asking the user:
*   *Option A*: Perform an **Incremental Update** (add new concepts and links to the existing vault without overwriting custom text).
*   *Option B*: Perform a **Fresh Regeneration** (clear the directory and recreate the entire vault from scratch).

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
- `phase-2-validation` — Content validation gate
- `phase-3-write-batch-1` through `…-N` — one per writer batch
- `phase-3-validation` — Writer output validation gate
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

**Incremental Mapping Logic**: If performing an Incremental Update, the mapper must first scan the existing vault files under `<vault_path>/<topic-slug>`, read their titles, and build a map of existing concepts. The mapper should then only propose *new* atomic concepts, subtopics, and connections that extend or connect to the existing graph, rather than rebuilding the whole graph.

**Human-in-the-Loop Verification**: Before moving to Phase 2 (Research), the parent agent must output the Mapper plan to the user in a clean list format and ask: *"Please review the planned concepts. Let me know if you would like to add, rename, or remove any before we proceed to research."* Block execution until the user responds or confirms.

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
- <Term 1>: <one-line definition — MUST be a real, specific definition>
- <Term 2>: <one-line definition — MUST be a real, specific definition>
[aim for 20+ terms — all atomic concepts PLUS a few
supporting terms that don't get their own file.
IMPORTANT: every definition must be a real, meaningful sentence
that explains the term. Do NOT write generic placeholders like
"A concept definition" or "Related to the topic."]

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

> **WHY THIS PHASE MATTERS**: The researcher is the knowledge engine of the
> entire pipeline. If researchers produce placeholder text, the entire vault
> is worthless — 23 beautifully-formatted empty files. The researcher MUST
> actually call WebSearch 3-5 times and extract real facts, dates, names,
> and explanations. Template-filling without real research is the #1 failure
> mode of this skill.

Each researcher agent prompt:

```
You are a deep research agent. Your job is to ACTUALLY RESEARCH this
topic using web searches. You MUST call the WebSearch/search_web tool
at least 3 times for different aspects of this concept. Do NOT skip
the research step. Do NOT fill in placeholder text.

ATOMIC CONCEPT: <Atomic Concept Name>
TOPIC: <Main Topic>
BUCKET: <Bucket Name>
SUBTOPIC: <parent subtopic>
VAULT PATH: <vault_path>
NOTE FILE PATH: <vault_path>/<topic-slug>/<bucket-slug>/<concept-slug>.md
TODAY'S DATE: <YYYY-MM-DD>

STEP 1 — SEARCH (mandatory, do not skip):
  Run at least 3 web searches. Good search queries:
    - "<Atomic Concept Name>" (direct lookup)
    - "<Atomic Concept Name> <Main Topic>" (contextual)
    - "<Atomic Concept Name> research studies" or "history" or "mechanism"
  Read the results carefully. Extract specific facts, dates, names,
  statistics, and explanations.

  Prefer authoritative sources: Wikipedia, .edu, peer-reviewed papers,
  established encyclopedias. AVOID SEO spam, random blogs, AI-generated
  content farms.

STEP 2 — SYNTHESIZE:
  Using what you found, write the structured output below. Every field
  must contain REAL information from your searches — not placeholders.

STEP 3 — SAVE:
  Save your research to: <vault_path>/<topic-slug>/.research/<concept-slug>.md
  Use the Write tool to save it. Then return the structured output below.

OUTPUT FORMAT (return this text, do not write it to a file):

CONCEPT: <Atomic Concept Name>
SLUG: <concept-slug>
DEFINITION: <2-3 sentence SPECIFIC definition based on your research.
  BAD:  "A concept related to the Pygmalion Effect."
  GOOD: "A distinguished American psychologist (1933-2024) who pioneered
        research on interpersonal expectancy effects and co-discovered
        the Pygmalion Effect through his landmark 1968 study with
        Lenore Jacobson at Oak School in San Francisco.">

KEY_POINTS:
- <Point 1 — must be a SPECIFIC fact or finding>: <2-3 sentence
  explanation with real details from your research>
- <Point 2>: <2-3 sentence explanation>
- <Point 3>: <2-3 sentence explanation>
- <Point 4>: <2-3 sentence explanation>
- <Point 5>: <2-3 sentence explanation>
[4-7 points. EVERY point must contain specific facts, dates, names,
or findings. If a point reads like "Point 1: Explanation." you have
FAILED. Go back and search more.]

SOURCES:
- <REAL url1> | <source title> | accessed <YYYY-MM-DD>
- <REAL url2> | <source title> | accessed <YYYY-MM-DD>
- <REAL url3> | <source title> | accessed <YYYY-MM-DD>
[minimum 3 sources. MUST be real URLs from your web searches.
URLs like "https://example.com" or "https://source1.com" are
UNACCEPTABLE and mean you did not actually search.]

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
<mermaid code here — MUST have at least 4 nodes and show real
relationships specific to THIS concept. A diagram with only 2 nodes
like "A-->B" is UNACCEPTABLE.>
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

Collect all `RESEARCH_DONE` markers before moving to validation. The
persisted `.research/<slug>.md` files serve as the writer's source of
truth — the writer reads the file rather than receiving the structured
output inline.

**Subagent Fallback & Rate-Limit Control**: If a background subagent fails due to model rate limits (429 errors), sandbox permission blocks, or timeouts:
1. Log the failure in the progress report.
2. Fall back to researching that specific concept sequentially in the main thread (using the parent agent's direct `search_web` and write capabilities).
3. Do not halt the entire process due to individual subagent failures.

### Phase 2 Validation Gate (MANDATORY)

After all researchers complete, the parent agent MUST validate every
`.research/<slug>.md` file before proceeding to Phase 3. For each file:

1. **Read the file** and check for these failure signals:
   - Definition contains "A concept related to" or is < 20 words
   - Any KEY_POINT reads "Point N: Explanation." or "Detail N about"
   - Any SOURCE URL contains "example.com", "source1.com", or "placeholder"
   - DIAGRAM has ≤ 2 nodes (e.g. just `A-->B`)
   - Total file is < 300 characters

2. **If any check fails**, the research is invalid. Re-dispatch that
   specific concept's researcher with this supplementary instruction:
   ```
   Your previous research output contained placeholder text instead of
   real findings. You MUST actually use the search_web tool to look up
   "<concept>" and fill in real facts. Do not proceed without searching.
   ```

3. **If re-dispatch also fails**, research the concept yourself using
   `search_web` directly from the parent agent thread and write the
   `.research/<slug>.md` file manually.

4. **Only proceed to Phase 3 once every research file passes validation.**

Log the validation results: "Validated 24 research files: 22 passed,
2 re-researched, 0 failed."

---

## Step 4 — Phase 3: Writers (parallel batches of 5)

Same batching discipline (5 per batch). Each writer reads its concept's
`.research/<slug>.md` from disk and produces the actual note.

Each writer agent prompt:

```
You are an Obsidian note writer. Convert the research file at
<vault_path>/<topic-slug>/.research/<concept-slug>.md into a
production-quality atomic Obsidian note.

CRITICAL RULE: You must use the ACTUAL content from the research file.
Copy the real definition, real key points, real sources, and real diagram
verbatim from the research. Do NOT substitute placeholder text. If the
research file says "Rosenthal spent decades studying...", your note must
say "Rosenthal spent decades studying..." — not "Point 1: Explanation."

OUTPUT FILE: <vault_path>/<topic-slug>/<bucket-slug>/<concept-slug>.md
TODAY'S DATE: <YYYY-MM-DD>

ALL ATOMIC CONCEPT TITLES (for [[wikilink]] consistency — use these EXACT strings):
<paste the full list of atomic concept names from the mapper plan, one per line>

ALL CROSS-DOMAIN FIELDS (for [[wikilink]] consistency):
<paste CROSS_DOMAIN_FIELDS list>

RESEARCH FILE CONTENTS:
<paste the .research/<slug>.md file contents here>

**Incremental Writing Logic**: If performing an Incremental Update and the note file at `<file_path>` already exists:
1. Read the existing note file.
2. Identify and preserve any custom body sections or edits the user has made (do not overwrite user-written content).
3. Update the Dataview frontmatter with the latest metadata, sources, and connections.
4. Merge new connections into the `## Connections` section, keeping any existing manual links.
Otherwise, use the Write tool to create the note at the path above. Use this EXACT frontmatter schema (dataview-friendly):

---
title: <Atomic Concept Title>
topic: <Main Topic>
bucket: <Bucket Name>
tags: [<topic-slug>, <bucket-slug>, <concept-slug>]
aliases: [<alt name if any>]
status: seedling
created: <YYYY-MM-DD>
sources: [<real-url1>, <real-url2>, <real-url3>]
connections: [<Other Concept 1>, <Other Concept 2>, <Other Concept 3>, <Other Concept 4>, <Other Concept 5>]
---

# <Atomic Concept Title>

> <One-sentence definition from the research — the researcher's DEFINITION
  field, verbatim. This MUST be specific to this concept.>

## Overview

<3-5 sentence overview: what this is, why it matters, where it sits
in the topic's structure. Reference the parent [[<Subtopic Name>]]
and the bucket [[<Bucket Name>]] MOC explicitly. Use facts from the
research file's KEY_POINTS to write substantive prose — not generic
filler like "This is an overview.">

## Key Points

- **<Point 1 heading from research>**: <2-3 sentences from research>
- **<Point 2 heading from research>**: <2-3 sentences from research>
- **<Point 3 heading from research>**: <2-3 sentences from research>
- **<Point 4 heading from research>**: <2-3 sentences from research>
- **<Point 5 heading from research>**: <2-3 sentences from research>
[Every point from the researcher's KEY_POINTS, as prose bullets.
Each bullet must contain specific facts — not "Explanation."]

## Diagram

<mermaid>
<the researcher's DIAGRAM block, verbatim — do not modify or simplify>
</mermaid>

## Connections

### Within <Main Topic>
- [[<WIKILINK_TARGET 1>]] — <one-sentence SPECIFIC reason for connection>
- [[<WIKILINK_TARGET 2>]] — <one-sentence SPECIFIC reason for connection>
- [[<WIKILINK_TARGET 3>]] — <one-sentence SPECIFIC reason for connection>
- [[<WIKILINK_TARGET 4>]] — <one-sentence SPECIFIC reason for connection>
- [[<WIKILINK_TARGET 5>]] — <one-sentence SPECIFIC reason for connection>
[MINIMUM 5 outgoing wikilinks — enforced. Each connection reason MUST
explain WHY these two ideas are related in a specific, meaningful way.

BAD:  "[[Self-Fulfilling Prophecy]] — Connection reason."
GOOD: "[[Self-Fulfilling Prophecy]] — Rosenthal's work directly
      formalized Merton's sociological concept into a testable
      psychological framework for classroom settings."

If you write "Connection reason." or "Related concept." you have FAILED.]

### Cross-Domain
- [[<Cross-Domain Field 1>]] — <how this concept connects>
- [[<Cross-Domain Field 2>]] — <how this concept connects>

## Sources

- <Source title> — <real url>
- <Source title> — <real url>
- <Source title> — <real url>
[Every source from the researcher's SOURCES list. These MUST be real
URLs — not example.com or placeholder URLs.]

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
budget is what makes the vault navigable.

**Atomicity check:** if the resulting note is <100 words of body, the
concept was too small to be its own file. In that case, do NOT write
a separate file. Instead, append the content to a `_merged.md` file
at `<vault_path>/<topic-slug>/<bucket-slug>/_merged.md` and report
`MERGED: <atomic-concept> into <parent-subtopic>`. The link-critic
will treat merged content as part of the parent.

### Phase 3 Validation Gate (MANDATORY)

After all writers complete, the parent agent MUST spot-check at least
5 notes (spread across all 3 buckets). For each checked note:

1. **Read the file** and verify:
   - The `>` blockquote definition is specific (not "A concept related to...")
   - Key Points contain real facts (not "Point 1: Explanation.")
   - Sources are real URLs (not example.com)
   - The mermaid diagram has ≥4 nodes
   - Connection reasons are specific (not "Connection reason.")
   - Body word count is ≥150 words

2. **If any note fails**, re-dispatch its writer with the research file
   contents pasted inline and an explicit instruction: "Use the REAL
   content from the research. Do not substitute placeholders."

3. Log results: "Spot-checked 5/24 notes: 5 passed quality gate."

---

## Step 5 — Phase 4: Link-Critic

Dispatch **one** agent (not parallelized — it needs a coherent view of
the whole vault). This phase now performs both link auditing AND content
quality auditing.

```
You are a link-critic and quality auditor for an Obsidian vault. Your
job is to find and fix problems in the link graph AND validate content
quality of a freshly-generated knowledge base.

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

5. CONTENT QUALITY AUDIT. For every atomic note (not MOCs/Index/Glossary):
   Read the file and check for these quality failures:
   - PLACEHOLDER_DEFINITION: The > blockquote contains generic text like
     "A concept related to" or is < 15 words
   - PLACEHOLDER_CONTENT: Any Key Point reads "Point N: Explanation." or
     "Detail N about" or body is < 100 words
   - PLACEHOLDER_SOURCES: Any source URL contains "example.com" or
     "source1.com" or "placeholder"
   - TRIVIAL_DIAGRAM: Mermaid diagram has ≤ 2 nodes
   - GENERIC_CONNECTIONS: Any connection reason is just "Connection reason."
     or "Related concept." or < 5 words

   Classify each note as:
   - QUALITY_PASS: no quality failures detected
   - QUALITY_FAIL: one or more quality failures detected (list which ones)

6. REPORT. Write the audit to
   <vault_path>/<topic-slug>/.link-audit-<YYYY-MM-DD>.md with sections:
   - ## Summary: counts of broken/weak/orphan/healthy + quality pass/fail
   - ## Broken Links: table of (source_file, target, line)
   - ## Orphan Notes: list
   - ## Weak Notes: list with their current outgoing count
   - ## Content Quality Failures: table of (file, failure_type, details)
   - ## Repair Plan: ordered list of edits you will make

7. APPLY REPAIRS. For each issue:
   - BROKEN link:
     1. Try the closest existing title or filename (case-insensitive,
        then prefix match). If a match exists, edit the source file.
     2. If the broken link matches a cross-domain field (listed in the
        plan's CROSS_DOMAIN_FIELDS), create a lightweight stub note at
        <vault_path>/<topic-slug>/_stubs/<domain-slug>.md with frontmatter
        `type: stub` and a one-sentence description.
     3. If no match is found, change [[Broken]] to plain text and add
        `(unresolved link — review manually)`.
   - ORPHAN note: Read the file, pick 2-3 atomic concepts in the same
     bucket, and append links to them in the Connections section.
   - WEAK note: Add 1-2 meaningful links from concepts mentioned in body.
   - QUALITY_FAIL note: Flag in the report but do NOT auto-fix content
     quality issues — those need the parent agent to re-dispatch writers.

8. RE-AUDIT. After applying repairs, re-run the classification.

9. RETURN FORMAT (do not write to a file, return as text):
   LINK AUDIT: <N> notes audited
   BROKEN FIXED: <B>
   ORPHANS LINKED: <O>
   WEAK STRENGTHENED: <W>
   STILL BROKEN: <J> (gave up — review manually)
   QUALITY PASS: <P> of <N> notes
   QUALITY FAIL: <F> notes (see audit report for details)
   AUDIT REPORT: <vault_path>/<topic-slug>/.link-audit-<YYYY-MM-DD>.md
```

The link-critic writes its own audit file to disk and returns the
counts. The final user-facing report (Step 7) quotes these counts.

**If QUALITY_FAIL > 0:** The parent agent should read the audit report
and consider re-dispatching writers for the failing notes before
proceeding to Phase 5.

---

## Step 6 — Phase 5: Indexer

Dispatch **one** agent. The indexer writes 3 files: the master index,
one MOC per bucket, and a glossary. Use the post-link-critic file
list (the link-critic's RE-AUDIT counts the canonical file inventory).

**IMPORTANT for the Glossary:** You must pass the mapper's full
`KEY_CONCEPTS_GLOSSARY` list (with real definitions) to the indexer
agent. The glossary MUST contain the actual definitions from the mapper —
not placeholder text like "A concept definition."

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

GLOSSARY DEFINITIONS (from the mapper — use these VERBATIM):
<paste the full KEY_CONCEPTS_GLOSSARY block here, with real definitions>

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

> <2-3 sentence overview from the mapper's DESCRIPTION — real text,
  not "Overview description.">

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
bucket, show 2-3 entry-point notes first (most general), then the rest.
Include a REAL one-line description for each note — not just "Description.">

### [[<Bucket 1 Name>]]
- [[<Entry-point concept 1>]] — <real one-line description>
- [[<Entry-point concept 2>]] — <real one-line description>
  - [[<Supporting concept A>]] — <real one-line>
  - [[<Supporting concept B>]] — <real one-line>
  - [[<Supporting concept C>]] — <real one-line>
- [[<Other concept X>]] — <real one-line>

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
| [[<Field 1>]] | <real specific reason why it connects> |
| [[<Field 2>]] | <real specific reason why it connects> |

## Key Figures

- **<Name 1>** — <specific contribution>
- **<Name 2>** — <specific contribution>

---
*Generated by atomic-notes v3 on <date> · <N> atomic notes across <M> buckets*

==============================================================
FILE 2-4: <vault_path>/<topic-slug>/_MOC/<bucket-slug>.md
  (one per bucket — 3 files total)
==============================================================

For each bucket, write a MOC that curates a reading order through
the bucket's notes. The MOC is a chain of [[wikilinks]] with
one-sentence "why read this next" annotations — REAL annotations,
not just "Reason." or "Description."

---
title: <Bucket Name> — Map of Content
topic: <Main Topic>
bucket: <Bucket Name>
tags: [<topic-slug>, <bucket-slug>, moc]
created: <YYYY-MM-DD>
---

# <Bucket Name>

> <Bucket description from the mapper plan — real text>

## Start here

- [[<Entry-point concept 1>]] — <real reason why to start here>
- [[<Entry-point concept 2>]] — <real reason why to start here>

## Foundational concepts

- [[<Concept A>]] — <real one-line description>
- [[<Concept B>]] — <real one-line description>

## Deeper dives

- [[<Concept C>]] — <real one-line description>
- [[<Concept D>]] — <real one-line description>

## Applications / case studies

- [[<Concept E>]] — <real one-line description>

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

Alphabetical list of all atomic concepts + supporting terms.

| Term | Definition |
|---|---|
| <Atomic Concept 1> | <the REAL definition from GLOSSARY DEFINITIONS above> |
| <Atomic Concept 2> | <the REAL definition from GLOSSARY DEFINITIONS above> |
| <Supporting Term> | <the REAL definition from GLOSSARY DEFINITIONS above> |
[aim for 20+ entries — all atomic concepts + supporting terms.
EVERY definition must be a real, specific sentence. If you write
"A concept definition" for any row, you have FAILED.]

---
*Generated by atomic-notes v3 on <date>*

After writing all files, return:
INDEX_WRITTEN: <vault_path>/<topic-slug>-Index.md
MOCS_WRITTEN: <comma-separated list of MOC file paths>
GLOSSARY_WRITTEN: <vault_path>/<topic-slug>/_Glossary.md
```

---

## Step 7 — Report to User

After all phases complete, report:

```
Atomic notes v3 complete for: <Main Topic>

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

Content quality: <P>/<N> notes passed quality gate
  <F> notes flagged for review (see audit report)

Navigation:
  <vault_path>/<topic-slug>-Index.md       — master index
  <vault_path>/<topic-slug>/_MOC/          — <M> per-bucket MOCs
  <vault_path>/<topic-slug>/_Glossary.md   — glossary

Sources: <S> unique source URLs across the vault.

Open your vault and start at: <topic-slug>-Index.md
```

---

## Step 8 — Generate Learning Roadmap (if road-mapper skill is available)

After the vault is complete, check if the `road-mapper` skill is available
in the skills list. If it is, invoke it on the completed vault:

```
Generate a learning roadmap for the vault at <vault_path>/<topic-slug>
Topic: <Main Topic>
```

This produces a `_Roadmap.md` with:
- A numbered reading order table
- A color-coded Mermaid flowchart (🟢 beginner → 🟡 intermediate → 🔴 advanced)
- Gateway concept highlighting

If road-mapper is not available, skip this step — the MOCs already
provide a basic reading order.

Append the roadmap path to the user report:
```
Learning roadmap: <vault_path>/<topic-slug>/_Roadmap.md
```

---

## Key Rules (v3)

**Content over structure.** A beautifully-formatted note with placeholder
text is worthless. Every note must contain real, researched knowledge.
The validation gates exist specifically to prevent hollow template output.

**Link budget.** Every atomic note must have ≥5 outgoing
`[[wikilinks]]` in its `## Connections` section. This is what makes
the vault navigable. The link-critic enforces this; writers that
fall short fail review.

**Connection annotations must be specific.** Every `[[wikilink]]` in
the Connections section must have a one-sentence explanation of WHY the
two ideas relate. Generic text like "Connection reason." or "Related
concept." is unacceptable.

**Atomicity.** One concept per file. If a concept is <100 words of
substantive body, merge it into the parent subtopic's `_merged.md`
file and skip writing a separate file.

**Source provenance.** Every atomic note must have ≥3 REAL source URLs in
its `## Sources` section AND in its frontmatter `sources:` array.
URLs containing "example.com" or other placeholder domains are forbidden.

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
  research the concept yourself from the parent thread.
- **Researcher returns placeholders.** Caught by the Phase 2 validation
  gate. Re-dispatch or research manually. Never proceed with placeholder
  research files.
- **Writer produces <100 word note.** Merge into parent
  `_merged.md` per the atomicity rule. Do not write a thin file.
- **Writer produces placeholder text despite valid research.** Caught
  by the Phase 3 validation gate. Re-dispatch the writer with research
  content pasted inline.
- **Link-critic finds >30% links broken.** That's a slug-drift signal —
  the writer phase used different conventions than the mapper.
  Re-dispatch the broken notes' writers with the canonical slug
  list, rather than patching links. Patch only if the drift is
  <10%.
- **Link-critic reports QUALITY_FAIL.** Re-dispatch writers for
  failing notes before proceeding to Phase 5.
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

- **Non-Obsidian targets.** The dataview blocks, Mermaid diagrams,
  and wikilink syntax are all Obsidian-specific. The notes render
  elsewhere, but the navigation layer is built for Obsidian.
- **Single-note requests.** If the user wants just one note on a
  topic, dispatch a single agent directly — no need for the full
  swarm.
