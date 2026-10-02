---
title: "MOC // ACTIVE PROJECTS & INITIATIVES"
aliases: ["Active Projects", "Projects", "Initiatives"]
tags: ["#meta", "#project", "#moc"]
clearance: "Tier-1"
status: "active"
---

# 🚀 MOC // ACTIVE PROJECTS & INITIATIVES
### *Live Ventures, Collision Enterprises & Sovereign Builds*

---

## Project Status Board

| Status | Count |
| :--- | :--- |
| 📐 Planning | `$= dv.pages('#project').where(p => p.status === 'planning').length` |
| 🔨 Building | `$= dv.pages('#project').where(p => p.status === 'building').length` |
| 🧪 Testing | `$= dv.pages('#project').where(p => p.status === 'testing').length` |
| ✅ Deployed | `$= dv.pages('#project').where(p => p.status === 'deployed').length` |
| 📦 Archived | `$= dv.pages('#project').where(p => p.status === 'archived').length` |

---

## All Projects

```dataview
TABLE
  project_lead AS "Lead",
  status AS "Status",
  priority AS "Priority",
  date_initiated AS "Initiated",
  target_date AS "Target",
  verticals AS "Verticals"
FROM #project
WHERE status != "archived"
SORT priority ASC, date_initiated DESC
```

---

## Collision-Born Projects

```dataview
LIST
FROM #project
WHERE contains(tags, "#collision")
SORT date_initiated DESC
```

---

## 🔗 Related Notes
- [[00.07 Command Center]]
- [[Cross-Disciplinary Collision Engine]]
- [[MOC - Cross-Domain Verticals]]
