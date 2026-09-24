---
id: core-federation
type: federation
category: agents
created_at: 2026-09-16T09:45:00+05:30
tags:
  - agents
  - mcp
  - federation
---

# 🤖 AI Agent Federation

All external and local AI systems synchronize their long-term memory through the unified cognitive core:

- **ULTRON (Antigravity CLI / Gemini 3.8)**: Primary system orchestrator and deep agentic operator.
- **Claude / Cursor / Copilot**: Codebase editors and interactive desktop agents.
- **Local Ollama / Open-WebUI**: Fully air-gapped private models running on host.
- **Protocol**: [[Model_Context_Protocol]] (MCP) memory endpoints & JSON-RPC bus.

## Coherence Rules
- All agents read and write to the same Markdown ground truth in [[Obsidian_Vault]].
- No agent overwrites contradictory facts without recording temporal invalidation edges ([[Bi-Temporal_Knowledge_Graphs]]).
