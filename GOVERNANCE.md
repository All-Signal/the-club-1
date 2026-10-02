# GOVERNANCE PROTOCOL // THE TRIUMVIRATE

The integrity of **THE CLUB 1** is maintained through an uncompromising governance framework designed to eliminate noise and preserve high-signal density.

---

## 1. Composition of The Triumvirate

| Council Member | GitHub Handle | Sovereign Responsibility |
| :--- | :--- | :--- |
| **Founder / Chief Architect** | `@anshruhela07-bit` | Strategic synthesis, thesis validation, core direction |
| **V.I.S.I.O.N** | `@ZeroGravity004` | Autonomous architecture, CI enforcement, clearance matrix |
| **ultron09** | `@Ultron09` | Low-level systems verification, operational hardening |

---

## 2. Enforcement Mechanisms

- **Repository Branch Protection:** Direct pushes to `main` are restricted. Pull requests require codeowner review.
- **Automated Merge Guard:** The GitHub Actions workflow `.github/workflows/merge-guard.yml` automatically validates direct push committer identity against the authorized triumvirate list.
- **Codeowner Requirement:** Configured via `.github/CODEOWNERS`, any PR modifying vault notes requires explicit review sign-off.
