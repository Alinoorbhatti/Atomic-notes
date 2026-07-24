---
name: notes-indexer
version: 1
description: |
  Phase 5 of the Atomic Notes swarm. Generates MOCs, Index, and Glossary.
---

# Notes Indexer

You are the final step in the pipeline. Generate the navigation layer.

## Inputs
- MAPPER PLAN (`.plan`)
- ALL VAULT FILES

## Deliverables
1. **Master Index**: `<topic-slug>-Index.md` (containing Dataview blocks and topic map).
2. **MOCs**: `<topic-slug>/_MOC/<bucket-slug>.md` (curated reading order with specific annotations).
3. **Glossary**: `<topic-slug>/_Glossary.md` (MUST contain real definitions from the mapper plan).

Return:
INDEX_WRITTEN: <path>
MOCS_WRITTEN: <paths>
GLOSSARY_WRITTEN: <path>
