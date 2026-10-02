---
title: "MAP OF CONTENT // DIVERGENT PERSONAS"
aliases: ["Personas MOC", "Divergent Personas"]
tags: ["#persona", "#moc", "#audience"]
target_age: "18-25"
---

# 🧠 MAP OF CONTENT // THE DIVERGENT PERSONA AUDIENCE (AGE 18–25)

> *"To reach this specific group—Standard marketing will fail. They are notoriously allergic to generic corporate outreach, buzzwords, and sales funnels. We deploy the Cicada doctrine."*

This cluster maps the four core archetypes of high-agency divergent minds identified in the Founder's handwritten notes:

| Persona Dossier | Cognitive Archetype | Primary Hunting Grounds | Core Engagement Vector |
| :--- | :--- | :--- | :--- |
| **[[01.01 Frontier AI Builders]]** | Autonomous agents, reasoning architectures, nocturnal experimenters | Hugging Face Spaces, X AI circles, arXiv, Local LLM Discord servers | Lead with benchmarks & raw code; fix their GitHub PRs; discuss inference speed |
| **[[01.02 Quant & Algo Operators]]** | Algorithmic execution, automated liquidity, latency obsessives | Crypto Twitter (CT), QuantConnect, Rust/C++ communities, Bloomberg terminals | Obsess over microseconds & capital efficiency; highlight real arbitrage inefficiencies; share open-source backtesters |
| **[[01.03 System & Low-Level Hackers]]** | Kernel devs, hardware proximity, zero-waste distributed systems | Hacker News, trending C/C++/Rust repos, IRC (Libera), Matrix | Show don't tell; publish clear architectural blueprints; discuss memory tradeoffs & crash handling |
| **[[01.04 Obsessive Polymaths]]** | Multi-disciplinary synthesizers, cross-domain combinators | Substack long-form comments, deep-dive podcasts, niche research forums | Publish high-depth synthesis essays; leave peer-level critiques; pose multi-domain puzzles |

---

## 🔗 Cross-Cutting Architectural Connections
- **The Philosophy:** [[00.03 Anti-Marketing & The Cicada Doctrine]]
- **The Acquisition Playbooks:** [[MOC - Outreach Playbooks]]
- **The 22 Cross-Disciplinary Domains:** [[MOC - Cross-Domain Verticals]]
- **Vetting Protocol:** [[Proof of Work Gauntlet]]


---

## 📊 Dynamic Persona Registry

```dataview
TABLE
  persona AS "Persona",
  target_age AS "Target Age",
  status AS "Status"
FROM #persona
SORT file.name ASC
```

## 🎖️ Members by Persona

```dataview
TABLE
  status AS "Status",
  persona_affinity AS "Affinity",
  date_identified AS "Identified"
FROM #member
SORT persona_affinity ASC
```

## 🔗 Extended Navigation
- [[00.07 Command Center]]
- [[MOC - Member Roster]]
- [[Proof of Work Gauntlet]]
