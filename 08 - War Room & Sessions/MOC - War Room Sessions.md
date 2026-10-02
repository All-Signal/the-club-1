---
title: "MOC // WAR ROOM & SESSION LOGS"
aliases: ["War Room", "Sessions", "Meeting Log"]
tags: ["#meta", "#session", "#moc"]
clearance: "Tier-1"
status: "active"
---

# ⚔️ MOC // WAR ROOM & SESSION LOGS
### *Triumvirate Deliberations, Strategic Decisions & Operational Directives*

---

## Session History

```dataview
TABLE
  session_date AS "Date",
  attendees AS "Attendees",
  agenda AS "Agenda",
  status AS "Status"
FROM #session
SORT session_date DESC
```

---

## Recent Decisions

```dataview
TABLE
  session_date AS "Session",
  decisions AS "Decisions"
FROM #session
WHERE decisions
SORT session_date DESC
LIMIT 10
```

---

## 🔗 Related Notes
- [[00.07 Command Center]]
- [[00.02 Governance - The Triumvirate]]
