---
title: "PLAYBOOK // HACKER NEWS SHOW HN ARCHITECTURE"
aliases: ["Show HN Playbook", "Hacker News Outreach"]
tags: ["#playbook", "#hackernews", "#systems"]
persona: "System & Low-Level Hackers"
status: "active"
---

# 📰 PLAYBOOK // HACKER NEWS "SHOW HN" ARCHITECTURE

---

## Objective
Capture the attention of hardcore [[01.03 System & Low-Level Hackers]] by publishing uncompromising, zero-bullshit open-source systems projects that reach the HN front page.

---

## Step 1: The Anatomy of a Successful "Show HN"
- **Headline Formula:** `Show HN: [Tool Name] – [Ultra-concise technical description in <10 words]`
  - *Example:* `Show HN: SovereignKV – Zero-copy embedded key-value store in 800 lines of Rust`
- **First Comment by Submitter:**
  - Must be posted within 60 seconds of submission.
  - Structure:
    1. **Why we built this:** Frustration with existing bloated alternatives.
    2. **Architecture:** Clear ASCII diagram of memory layout and thread model.
    3. **Tradeoffs:** Be brutally honest about what this tool does NOT do (e.g. "We don't support distributed consensus; single-node only").
    4. **Direct GitHub link:** No landing pages, no email walls, no Google Analytics scripts.

---

## Step 2: Architecture Diagram Formatting
Systems hackers respect clean ASCII / text architectural blueprints:

```
[ Incoming Network Packets ]
              │ (Kernel Bypass / DPDK)
              ▼
    [ Ring Buffer Queue ] (Lock-free, cache-aligned)
              │
    ┌─────────┴─────────┐
    ▼                   ▼
[ Worker Core 0 ]   [ Worker Core 1 ]
    │                   │
    └─────────┬─────────┘
              ▼
    [ Direct Memory Storage ] (Zero GC overhead)
```

---

## Step 3: Managing the Comment Thread
- Answer every technical critique with detailed, humble, and mathematically precise responses.
- If someone points out a flaw or edge-case race condition, thank them immediately, acknowledge the tradeoff, and invite them to submit an issue or PR.
- Cultivate relationships with high-karma technical commenters who consistently ask sharp questions.
