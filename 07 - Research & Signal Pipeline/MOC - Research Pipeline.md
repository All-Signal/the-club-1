---
title: "MOC // RESEARCH & SIGNAL PIPELINE"
aliases: ["Research Pipeline", "Signal Pipeline", "Research"]
tags: ["#meta", "#signal", "#moc"]
clearance: "Tier-1"
status: "active"
---

# 📡 MOC // RESEARCH & SIGNAL PIPELINE
### *Frontier Intelligence Capture, Analysis & Cross-Referencing*

---

## Signal Categories

| Category | Count |
| :--- | :--- |
| 📄 Papers & Preprints | `$= dv.pages('#signal').where(p => p.signal_type === 'paper').length` |
| 💻 Repositories & Tools | `$= dv.pages('#signal').where(p => p.signal_type === 'repo').length` |
| 🧵 Threads & Discussions | `$= dv.pages('#signal').where(p => p.signal_type === 'thread').length` |
| 📊 Benchmarks & Data | `$= dv.pages('#signal').where(p => p.signal_type === 'benchmark').length` |
| 🌐 Market & Industry Intel | `$= dv.pages('#signal').where(p => p.signal_type === 'market').length` |

---

## Priority Signals

```dataview
TABLE
  signal_type AS "Type",
  source AS "Source",
  priority AS "Priority",
  status AS "Status",
  date_captured AS "Captured"
FROM #signal
WHERE priority = "critical" OR priority = "high"
SORT date_captured DESC
```

---

## All Captured Signals

```dataview
TABLE
  signal_type AS "Type",
  source AS "Source",
  priority AS "Priority",
  status AS "Status",
  verticals AS "Verticals"
FROM #signal
SORT date_captured DESC
```

---

## 🔗 Related Notes
- [[00.07 Command Center]]
- [[MOC - Cross-Domain Verticals]]
- [[Cross-Disciplinary Collision Engine]]
