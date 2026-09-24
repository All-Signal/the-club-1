---
id: concept-btkg
type: concept
category: knowledge-graph
created_at: 2026-09-16T09:45:00+05:30
tags:
  - knowledge-graph
  - temporal-data
  - graphiti
---

# 🕸️ Bi-Temporal Knowledge Graphs

## The Challenge of Evolving Facts
In naive vector stores, if a user states:
- *2024*: "I prefer Neovim over VSCode."
- *2026*: "I switched to Foot terminal and Antigravity."

A standard vector query retrieves both, creating hallucinations and conflicting instructions.

## Bi-Temporal Dimensions
A bi-temporal graph associates every edge with two time horizons:
1. **Assertion Time (`valid_at` -> `invalidated_at`)**: When the fact was true in the real world.
2. **System Time (`recorded_at` -> `archived_at`)**: When the knowledge base learned the fact.

## Obsidian Interoperability
In [[Obsidian_Vault]], bi-temporal facts are rendered using YAML frontmatter properties (`valid_from`, `valid_until`) and wikilink relation syntax, enabling historical timeline queries using Dataview.
