<div align="center">
  <img src="./assets/logo.png" alt="Atomic Notes Logo" width="250" style="border-radius: 20px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1); margin-bottom: 20px;" />

  # <span style="background: -webkit-linear-gradient(45deg, #FF4B2B, #FF416C, #FFB75E); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Atomic Notes</span> ⚛️

  **Generate comprehensive, atomic, and deeply interconnected Obsidian knowledge bases using a coordinated AI Agent Swarm.**

  [![Version](https://img.shields.io/badge/Version-3.0-orange.svg?style=for-the-badge)](#)
  [![Obsidian](https://img.shields.io/badge/Obsidian-Ready-purple.svg?style=for-the-badge&logo=obsidian)](#)
</div>

---

## 🌟 Overview

**Atomic Notes** is an agentic workflow that orchestrates a 5-phase AI swarm to research, map, and write a comprehensive Obsidian knowledge base on any topic. 

Unlike generic "vibe coding" or shallow note generation, Atomic Notes enforces **structure AND substance**. It demands actual web research, specific citations, robust MOC (Map of Content) organization, and an audited internal link graph.

## 🚀 The 5-Phase Swarm Pipeline

1. **🗺️ Mapper Agent**: Outlines the topic into 3 MOC buckets, 6-10 subtopics, and ~24 strictly defined atomic concepts. Supports **Incremental Updates** by scanning existing vaults.
2. **🔍 Researchers (Parallel)**: Dispatched in parallel to perform *real* web searches. Extracts facts, sources, and definitions. Checked by rigorous validation gates.
3. **✍️ Writers (Parallel)**: Transforms raw research into beautifully formatted Obsidian notes. Safely merges updates if a note already exists without overwriting custom prose.
4. **🕵️ Link-Critic**: A centralized auditor that mathematically validates the internal graph using python tools—fixing broken wikilinks, connecting orphans, and flagging poor content.
5. **🗂️ Indexer**: Compiles the final entry-points, including a Master Index, per-bucket MOCs, and a definitive Glossary.

## 🔌 Model Context Protocol (MCP) Support

Atomic Notes fully supports the **Model Context Protocol**. We provide a FastMCP server that exposes our deterministic auditing scripts (`scan_vault`, `validate_links`, `parse_frontmatter`) directly to your AI agents as native, typed tools.

To run the MCP server:
```bash
cd scripts
pip install -r requirements.txt
mcp run mcp_server.py
```
This allows agents to interface with your Obsidian vault programmatically, bypassing hallucination-prone prompt analysis.

## 🛠️ Usage

To trigger the skill, simply ask your agent:

> *"Project atomic notes on Quantum Computing into my vault at `/path/to/vault`"*

The swarm will automatically:
1. Propose a syllabus (and ask for your approval).
2. Spin up parallel subagents to research and write.
3. Repair the link graph.
4. Present you with a fully navigable Obsidian vault.

## ⚠️ Core Philosophy

- **Substance over Structure**: A beautifully formatted note with placeholder text is worthless. Validation gates strictly reject hollow outputs.
- **Strict Atomicity**: One concept per file.
- **Link Integrity**: No dead ends. The knowledge graph is audited before completion.

---
<div align="center">
  <i>Built with discipline. Designed for Obsidian.</i>
</div>
