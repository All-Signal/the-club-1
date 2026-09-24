---
id: concept-mcp
type: concept
category: protocol
created_at: 2026-09-16T09:45:00+05:30
tags:
  - mcp
  - protocols
  - interoperability
---

# 🔌 Model Context Protocol (MCP)

## The Unified Nerve Center
Model Context Protocol (MCP) is the universal open standard allowing AI agents to connect to local tools, databases, and context servers.

## ULTRON Memory MCP Server
The ULTRON unified memory daemon exposes an MCP server providing standard tools:
- `recall_memory(query, limit)`: Semantic + keyword recall across notes.
- `store_memory(category, title, content, links, tags)`: Creates markdown note and updates vector/graph indexes.
- `get_core_memory()`: Returns active operator profile and system status.
- `synthesize_canvas(topic, nodes, edges)`: Creates interactive visual canvases in [[Obsidian_Vault]].
