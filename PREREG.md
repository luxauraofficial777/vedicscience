# PREREG — SPH-01 Spectral Research & Hardening
**Executor:** Big Pickle (OpenCode) · **Workspace:** `study\OpenCodeBP\` (deviation from directive default folder, owner-directed: two agents run in parallel, each in its own workspace; Gemini uses `hardening_SPH01\`)
**Pre-registered (git commit):** 2026-10-18, before any claim extraction or dataset contact
**Verifier:** independent agent, Phase 5 (not this executor)

---

## 1. Scope frozen at pre-registration

- **Corpus (read-only, SHA-256 pinned in `outputs/CORPUS_MANIFEST.sha256` at extraction time):** Task_01–05, Consolidated_Master_Report_AS_NME.md, articles 02–04 (HTML), THEOREM_DOCKET.md, IDEAS_RESEARCH_BRIEF.md, ASTRA_COMPARATIVE_BRIEF.md, Standard_*_Reference.{md,html}, the two data JSONs, the four verify/sim scripts, 17 schematics in `img\`.
- **Prior audits as seed findings only** (directive §11, 14 items): each is re-verified from source, never assumed.
- **Reference data:** fetched live where marked, else tagged *(not re-fetched)* per R3 and cannot carry a SUPPORTED verdict alone.

## 2. Pre-registered hypotheses (R5: support ⟷ falsify stated in advance)

| ID | Claim under test | Supports if… | Falsifies if… |
| :--- | :--- | :--- | :--- |
| H-Q1 | Sound quanta can drive quantum transitions named in the corpus (tunneling assist, phonon condensation at 21.5 kHz) | a named mechanism concentrates hf energy to the transition scale within the stated drive parameters, and n_th/regime analysis allows quantum behaviour | regime ledger shows n_th ≫ 1 at the stated f and T, and no concentration mechanism is named → UNTESTABLE-AS-WRITTEN or INCONSISTENT |
| H-Q2 | Λ_sl / Ξ_23D are physics (not allegory) | they can be written as well-typed mathematics with stated domains and dimensions that reduce to known theory in a limit | they cannot (after one rewrite attempt) → ALLEGORY tag (directive §12) |
| H-Q3 | A1 (mass from substrate frequencies) adds content beyond Higgs/QCD | a distinguishing observable is named that differs from SM prediction | no distinguishing observable → OPEN-but-empty, flagged in verdict matrix |
| H-CE1 | EM/chemical effects vary across solar-system environments more than gravity does | ratio of discharge-variance to gravity-variance ≫ 1 in the CE3 environment table (computed, not asserted) | ratio ≤ 1, or inputs are unsourced → INCONSISTENT |
| H-CE2 | Electromagnetic "stasis" holds the atmosphere | NRLMSIS-measured composition matches EM-sorting prediction better than homosphere mixing | measured N₂/O₂/Ar uniform with altitude (standard homosphere) → INCONSISTENT |
| H-V1 | The softening chain (G_eff, σ_t) is self-consistent at ε = 1.5×10⁻⁴ | one value of G_eff at that ε across all docs+scripts, with sourced Re[D] | three incompatible values persist / Re[D] unsourced → INCONSISTENT (seed #1) |
| H-V2 | Softening lowers excavation energy | σ²/G invariant under Griffith → if the corpus relies on lowered σ_t to cut fracture energy, that part is INCONSISTENT by the corpus's own equations | — (this one is arithmetic; symmetry: it is CONSISTENT only if the corpus claims a mechanism other than reduced fracture energy) |
| H-V3 | Cavity FDTD result (1,570.80 Pa/m) is reproducible | steady-state run at ≥ Q/π cycles with impedance boundary reproduces within 10% | discrepancy > 10% → INCONSISTENT (seed #6: code gives 1.74 Pa/m) |
| H-VED1 | Vedic sound-term passages co-occur with astra names above baseline | co-occurrence rate in astra passages ≥ 3× non-astra battle baseline (Fisher exact p < 0.01) | ratio < 3 or p ≥ 0.01 → no statistical association; report as null |

**Null-result policy:** every H above will be reported whether it survives or not; no claim is dropped for failing.

## 3. Fixed thresholds and constants

- Energy-concentration screening quantum (directive §4): a 20 kHz phonon = 8.27×10⁻¹¹ eV; chemical-bond anchor 4.0 eV; ratio 4.8×10¹⁰. Any chemistry claim without a named concentration mechanism → UNTESTABLE-AS-WRITTEN.
- Thermal occupation: n_th = 1/(exp(hf/kT)−1) at T = 300 K; classical if n_th ≥ 1 (f ≤ ~6.25 THz), quantum if n_th < 1.
- G_eff resolution: tolerance ±5% across sources; outside → INCONSISTENT.
- FDTD reproduction tolerance: 10% of reported value at steady state.
- Coherence/association: p < 0.01 Fisher exact; effect size ≥ 3×.
- Paschen law: B·(p·d)/(ln(p·d) + c) with air constants A = 112.5 (kPa·mm)⁻¹? — note: constants fetched at execution; if not fetched, table marked *(not re-fetched)*.
- Upper limits quoted as 95% where applicable (E4 precedent).

## 4. Determinism (R6)

- `requirements.txt` pins: python 3.11.15, numpy 1.26.4, scipy 1.17.1, matplotlib 3.11.2, requests 2.33.0.
- All scripts: `numpy.random.default_rng(seed=20261018)` if any randomness (bootstrap in V6 etc.).
- Every derived table/JSON hashed into `outputs/MANIFEST.sha256`; re-run must reproduce byte-identical outputs (line-ending and float-format fixed: `%.6g`, LF).
- Live-fetched data (NRLMSIS not runnable offline): raw HTTP responses cached in `outputs/cache/` with URL+timestamp+SHA-256; analysis runs on the cache, never live.

## 5. Deviations log (live)

| # | Deviation | Reason |
| :--- | :--- | :--- |
| D1 | Output root = `OpenCodeBP\` not `hardening_SPH01\` | owner instruction, parallel-agent isolation (R10) |
| D2 | No matplotlib at start → installed 3.11.2 mid-session | chart deliverable required |
| D3 | Interpretive pass `BP-ONION-CREVICE-01` (onion-layer / breathing-crevice lens) + re-derivation of archived outputs (`onion_crevice_derivation.py`) without new external data contact | owner directive 2026-10-18; E4 pre-registered verdicts and hypothesis table unchanged; new claims tagged HYPOTHESIS/DERIVATION in the synthesis |

## 6. Out of scope (deferred to DEFERRALS.md at first encounter)

- V7 sonochemistry bench test (physical, weeks).
- Anything requiring credentials (GFZ IGETS FTP, ITER IMAS internals).
- Editing original docs (R2) — corrections are versioned `_v2` files only when a Band task produces one.

*End PREREG. Anything not listed here that becomes a hypothesis later gets appended with its own timestamp before its analysis runs.*
