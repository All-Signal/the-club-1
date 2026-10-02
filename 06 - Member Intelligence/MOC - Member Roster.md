---
title: "MOC // MEMBER ROSTER & INTELLIGENCE"
aliases: ["Member Roster", "Roster", "Members"]
tags: ["#meta", "#member", "#moc"]
clearance: "Tier-1"
status: "active"
---

# 🎖️ MOC // MEMBER ROSTER & INTELLIGENCE
### *Sovereign Enclave Personnel Tracking & Candidate Pipeline*

---

## Pipeline Overview

| Stage | Count |
| :--- | :--- |
| 🔍 Scouting | `$= dv.pages('#member').where(p => p.status === 'scouting').length` |
| 📋 Under Review | `$= dv.pages('#member').where(p => p.status === 'reviewing').length` |
| ⚔️ In Crucible | `$= dv.pages('#member').where(p => p.status === 'crucible').length` |
| ✅ Admitted | `$= dv.pages('#member').where(p => p.status === 'admitted').length` |
| ❌ Rejected | `$= dv.pages('#member').where(p => p.status === 'rejected').length` |

---

## Full Roster

```dataview
TABLE
  status AS "Status",
  clearance AS "Clearance",
  persona_affinity AS "Persona Affinity",
  domains AS "Domains",
  date_identified AS "Identified"
FROM #member
SORT status ASC, date_identified DESC
```

---

## By Persona Affinity

### Frontier AI Builders
```dataview
LIST
FROM #member
WHERE contains(persona_affinity, "Frontier AI Builders")
SORT date_identified DESC
```

### Quant & Algo Operators
```dataview
LIST
FROM #member
WHERE contains(persona_affinity, "Quant & Algo Operators")
SORT date_identified DESC
```

### System & Low-Level Hackers
```dataview
LIST
FROM #member
WHERE contains(persona_affinity, "System & Low-Level Hackers")
SORT date_identified DESC
```

### Obsessive Polymaths
```dataview
LIST
FROM #member
WHERE contains(persona_affinity, "Obsessive Polymaths")
SORT date_identified DESC
```

---

## 🔗 Related Notes
- [[00.07 Command Center]]
- [[Proof of Work Gauntlet]]
- [[The 30-Minute Crucible]]
- [[00.02 Governance - The Triumvirate]]
