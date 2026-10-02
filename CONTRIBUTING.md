# CONTRIBUTING TO THE CLUB 1 // UNIFIED OBSIDIAN VAULT

Thank you for contributing intelligence to **THE CLUB 1**. We operate under strict ground-truth standards: **zero marketing fluff, zero buzzwords, absolute technical rigor**.

---

## 🏛️ PR Clearance & Merge Authority

All pull requests are reviewed under the supervision of **The Triumvirate**:
- `@anshruhela07-bit` (Founder / Chief Architect)
- `@ZeroGravity004` (V.I.S.I.O.N)
- `@Ultron09` (ultron09)

Only one of these three accounts possesses final merge clearance. External PRs are welcome, but will be held to the highest standard of proof of work.

---

## 📝 Markdown & Obsidian Standards

1. **Wikilinks:** Use native Obsidian wikilinks (`[[Note Name]]` or `[[Note Name|Display Text]]`). Do not use raw web URLs for internal vault notes.
2. **Frontmatter:** Every note must include standard YAML frontmatter:
   ```yaml
   ---
   title: "..."
   aliases: ["..."]
   tags: ["#persona", "#vertical", etc.]
   status: "active | draft"
   clearance: "Public | Tier-1 | Tier-0"
   ---
   ```
3. **Templates:** Use templates located in [`Templates/`](Templates/) when creating new persona dossiers, verticals, or outreach playbooks.
4. **Attachments:** Place any accompanying diagrams or images in [`attachments/`](attachments/).

---

## 🚀 Branch & PR Protocol

1. Create a descriptive branch:
   - `persona/<name>`
   - `vertical/<name>`
   - `playbook/<name>`
   - `fix/<issue>`
2. Follow the [Pull Request Template](.github/pull_request_template.md).
3. Automated CI will verify that markdown files are non-empty and formatted properly.
4. Request review from `@anshruhela07-bit`, `@ZeroGravity004`, or `@Ultron09`.
