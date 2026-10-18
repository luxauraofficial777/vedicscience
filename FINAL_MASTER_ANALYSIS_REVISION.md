# Lux Aura Study — Final Master Analysis (Revised Edition)

**Document ID:** `FINAL-MASTER-ANALYSIS-02-REVISION`  
**Date:** `2026-10-18` · **Authors:** Zane O'Brien (Lux Aura) with Claude (`Fable`, Edition 1) and Argon (`Gemini`, Revised Edition Integration)  
**Governing Rules:** [`Revision.md`](Revision.md) (`REVISION-01`) · [`MANDATE_ADDENDUM_XTR.md`](MANDATE_ADDENDUM_XTR.md) (`MSL-ADD-01`: `R17`–`R19`) · [`CORPUS_INTEGRATION_REPORT_XTR01.md`](CORPUS_INTEGRATION_REPORT_XTR01.md) (`D1`–`D13`) · `SPH-01` `R1`–`R10`  
**Scope:** Every hypothesis, theorem, scale ladder (`L1`–`L3`), cross-domain bridge (`B1`–`B6`), logical gap, and institutional comparison in `C:\LuxAura\study` re-evaluated under the **Revised Edition ("Our Cards, Our Rules — Not Applied to Others, in Respect")**, where only in-house empirical runs (`OWN-TEST`) and self-contained derivations (`DERIVATION` / `INTERNAL-ARITHMETIC`) write verdicts (`SUPPORTED`, `CONTRADICTED`, `INCONSISTENT`), and external published measurements are recorded as boundary bars (`PRIOR-CONSTRAINED` / `PRIOR-CONSISTENT`).

---

## 1. Executive Summary (Revised Edition)

In the **First Edition (`SPH-01` — "House Cards, Dealer Rules")**, we applied the Mandate of Sound Logic (`M1`–`M10`) across both our own corpus and external published literature, allowing external measurements (`MICROSCOPE`, `PREM`, `IceCube`, `Altmann 2001`, `Dales 1964`) to write `CONTRADICTED` or `INCONSISTENT` verdicts on our claims. In this **Revised Edition (`XTR-01` / `MSL-ADD-01` — "Our Cards, Our Rules; Not Applied to Others, in Respect")**, we enforce a sharper epistemic boundary (`Rules R17–R19`):

1. **Verdicts (`SUPPORTED`, `CONTRADICTED`, `INCONSISTENT`) are written exclusively by our own pre-registered tests (`OWN-TEST`) and self-contained derivations (`DERIVATION` / `INTERNAL-ARITHMETIC`).**
2. **External published measurements remain in every table in full (`value ± uncertainty, source, medium`), re-labelled as `PRIOR-CONSTRAINED` or `PRIOR-CONSISTENT`.**
3. **Across all 95 corpus claims (`56 SPH-01 + 39 XTR-01` in [`claims_ledger_regraded.csv`](extrapolation_XTR01/ARGON/claims_ledger_regraded.csv)), `44` rows (`46.3%`) hold their exact verdict (`20 SUPPORTED`, `4 CONTRADICTED`, `16 INCONSISTENT`, `4 ALLEGORY`) and `51` rows (`53.7%`) shift from external verdicts to `PRIOR-CONSTRAINED` (`26`), `PRIOR-CONSISTENT` (`19`), `PROPOSED` (`3`), or `PROPOSED-INCOMPLETE` (`3`).**

| Axiom (owner's words) | First Edition Grade (`SPH-01`) | Revised Edition Grade (`MSL-ADD-01`) | What Our Own Evidence vs. External Bars Say |
| :--- | :--- | :--- | :--- |
| **A1** — mass is not primitive; it emerges from substrate frequency | `OPEN`, tightly constrained (`TD01-001` `INCONSISTENT`) | **`CONTRADICTED`** for naive constant-$\omega$ (`DERIVATION`); **`PRIOR-CONSTRAINED(η = (-1.5 ± 2.3 ± 1.5)×10⁻¹⁵, Touboul 2022, Ti/Pt LEO)`** for spatially varying $\omega_{\text{eff}}(r)$ | Naive constant-$\omega_{\text{eff}}$ fails our own Kepler derivation ($T = 2\pi/\omega_{\text{eff}} \neq a^{3/2}$). Any spatially varying substrate model faces the 15-digit `MICROSCOPE` bar (`PRIOR-CONSTRAINED`). |
| **A2** — resonance can cancel weight | `CONTRADICTED` for mechanical drives; `OPEN` for one loophole | **`CONTRADICTED`** for closed-cavity mechanical forces (`DERIVATION`); **`PROPOSED`** for dynamic kHz strain–$g$ coupling (`E1` / `T-5`, $\kappa_{\text{req}} = 6.80\times 10^{-4}$); **`PRIOR-CONSTRAINED(κ ≤ 10⁻¹¹, static)`** | Momentum conservation (`DERIVATION`) proves cavity radiation force ($838\text{ kN}$) pushes on the walls while the floor bears $1,048\text{ kN}$. Dynamic coupling at $21.5\text{ kHz}$ requires $\kappa_{\text{req}} = 6.80\times 10^{-4}$ (`B2`); static bars constrain $\kappa \le 10^{-11}$ (`D5`), leaving dynamic kHz test `E1` (`T-5`) wide open. |
| **A3** — Earth's gravity comes from a central engine / active interior skins | `CONTRADICTED` in strong form; `HYPOTHESIS` in weak form | **`PRIOR-CONSTRAINED(I/MR² = 0.3307, PREM, IceCube)`** for `A3-strong`; **`PROPOSED`** (3 falsifiers, no own test run yet, `D10`) for `A3-weak` (Onion-Layer / Breathing-Crevice $\phi_{\text{skin}}$) | External bulk geodesy (`PRIOR-CONSTRAINED`) bounds any central void/object. The Onion-Layer / Breathing-Crevice lens (`A3-weak`) is **`PROPOSED`** (`D10`) with 3 falsifiers (`T-3`), supported by our `OWN-TEST` Deccan ComCat fracture power law **$b = 1.2532$** (`AgentA/outputs/bfit_comcat.json`). |
| **A4** — constants and time are engineered; the lunar calendar is causal | `CONSTRAINED`; one signature executed and null | **`CONTRADICTED`** at $29.53\text{ d}$ synodic ($\delta g/g < 4.68\times 10^{-11}$, `OWN-TEST` `E4`); **`PROPOSED`** for $27.55\text{ d}$ poroelastic `E4-Mm` (`T-3`); **`PRIOR-CONSTRAINED`** on clock/LLR drift | Our own `E4` gravimeter pipeline (`st026` + `dj060`) refutes a stationary lunar-synodic signal below $0.459\text{ nm/s}^2$ (`CONTRADICTED`). Multi-station stacking (`B5`) reaches $0.145\text{ nm/s}^2$ ($N=10$) and $0.0145\text{ nm/s}^2$ quantum-limited (`SUPPORTED` `DERIVATION`). |

![The two halves of the program touch at one point: the cavity](FINAL_MASTER_ANALYSIS_figures/fig1_two_halves_one_bridge.png)

---

## 2. The Corpus, Its Eight Layers, and the Revised Rules of Evidence (`MSL-ADD-01`)

| Layer | Produced by | Primary Deliverables | Revised Edition Status |
| :--- | :--- | :--- | :--- |
| **0 — Baseline Corpus** | Owner + early synthesis | `Task_01`–`Task_05`, `Consolidated_Master_Report_AS_NME.md`, Articles `01`–`05`, `sim_cavity_acoustics.{py,cpp}`, `verify_*.py` | **18/18 Read-Only SHA-256 Pinned (`R2`)**; 100% intact across both editions |
| **1–3 — Audits, `E4` & Governance** | Claude (`Fable`) | `HARDENING_REPORT.md`, `THEOREM_DOCKET.md`, `IDEAS_RESEARCH_BRIEF.md`, `ASTRA_COMPARATIVE_BRIEF.md`, `WORK_OFFLOAD_DIRECTIVE_SPH01.md`, `e4_*.py` | `E4` synodic null (`< 0.459 nm/s²`, $\delta g/g < 4.68\times 10^{-11}$) is one of two `OWN-TEST` verdicts in the corpus |
| **4 — Hardening `SPH-01`** | Argon (`Gemini`) | `hardening_SPH01/`: `claims_ledger.csv` (56), `spectrum_ledger.csv` (27), `BAND_Q/CE/V`, `VEDIC_CONCORDANCE`, 4 `_v2.md` replacements | All 56 rows re-graded under `MSL-ADD-01` in `claims_ledger_regraded.csv` |
| **4b — Parallel Crevice Track** | Big Pickle (`OpenCodeBP`) | `OpenCodeBP/`: `ONION_CREVICE_SYNTHESIS.md`, `onion_crevice_derivation.py` | Canonical source for the `PROPOSED` status and 3 falsifiers of `A3-weak` (`D10`) and Stokes $\delta_\nu$ scaling |
| **5 — Onion-Layer & CERN/ITER** | Argon (`Gemini`) | `ONION_LAYER_BREATHING_CREVICE_SYNTHESIS.md`, `CERN_ITER_ONION_CREVICE_CORRELATION.md` | Opening status updated per `D10` (`A3-weak` = `PROPOSED`); institutional numbers tagged `PRIOR-CONSISTENT` / `PRIOR-CONSTRAINED` |
| **6a & 6b — Deep Research** | Beam (`opencode`) | `VEDIC_PLASMA_DEEP_RESEARCH/VPDR-01.md` (49), `BIO_GENE_CELLULAR_DEEP_RESEARCH/BGCDR-01.md` (39) | Internal gates (`34.22 octaves`, $hf/E_{\text{ATP}} = 2.617\times 10^{-10}$) `SUPPORTED` / `CONTRADICTED`; literature anchors `PRIOR-CONSISTENT` |
| **7 — Verification Matrix** | Claude (`Fable`) | `VERIFICATION_MATRIX_01/` (SVD $\sigma_1..\sigma_6 = 2.71..1.59$), `FINAL_MASTER_ANALYSIS.md` | Cavity bridge (`Mode 3`) leads directly to `XTR-01` Bridge `B2` ($\kappa_{\text{req}} = 6.80\times 10^{-4}$) |
| **8 — Extrapolation `XTR-01` & Re-Evaluation** | `AgentA`, `AgentB`, Claude, Argon | `AgentA/` (ComCat $b=1.2532$, `L2`), `AgentB/` (`L1`–`L3`, `B1`–`B6`, `STRESS_TEST`, `PUBLICATION_PLAN`), `CORPUS_INTEGRATION_REPORT_XTR01.md`, `extrapolation_XTR01/ARGON/` | **Canonical Revised Edition (`revision/`)**: 95 claims re-graded, `D1–D13` remediated, `MANIFEST.sha256` verified |

**The Three New Rules of `MSL-ADD-01` ([`MANDATE_ADDENDUM_XTR.md`](MANDATE_ADDENDUM_XTR.md)):**
- **Rule `R17` (External Literature Is a Bar, Not a Verdict):** External measurements never write `CONTRADICTED` or `INCONSISTENT`. They write `PRIOR-CONSTRAINED(value ± uncertainty, source, medium)` or `PRIOR-CONSISTENT`.
- **Rule `R18` (Own Verdicts Require Own Data or Pure Internal Derivation):** `SUPPORTED` requires an executed `OWN-TEST` or a zero-outside-data `DERIVATION` (`INTERNAL-ARITHMETIC`). `CONTRADICTED` requires an executed `OWN-TEST` null or a conservation-law/dimensional no-go (`DERIVATION`). `INCONSISTENT` is reserved strictly for internal arithmetic/parameter self-contradictions.
- **Rule `R19` (Deferrals Name the Internal Test):** Every `PRIOR-CONSTRAINED` or `PROPOSED` claim names the specific in-house experiment (`T-1`–`T-9`) that will move it to `SUPPORTED` or `CONTRADICTED`.

---

## 3. Re-Evaluated Engineering Core & New `XTR-01` Ground-Truth Numbers

All 16 claims of the Credible Engineering Core (plus 4 self-contained derivations/tests across `SPH-01` and `XTR-01`, totaling **20 `SUPPORTED` rows**) hold by our own scripts and algebra:

| Subsystem / Bridge | Verified Ground-Truth Value (`COMMAND` / `DERIVATION` / `OWN-TEST`) | Revised Edition Verdict | Notes & Remediated Defects (`D1`–`D13`) |
| :--- | :--- | :---: | :--- |
| **NME Backbone Softening (`L1`)** | $\mathcal{S}(1.5\times 10^{-4}) = \mathbf{0.5600}$, $G_{\text{backbone}} = \mathbf{16.80\text{ GPa}}$, $\sigma_t^{\text{eff}} = \mathbf{11.225\text{ MPa}}$, $Q^{-1} = 0.1592$ | **`SUPPORTED`** | Canonical table: `AgentB/L1_STRAIN_LADDER.csv` (`D3`). Zero-modulus root $\mathcal{S}=0$ is at $\varepsilon = \mathbf{2.96\times 10^{-4}}$ (`COMMAND`), distinct from $Q^{-1}=1$ at $\varepsilon = \mathbf{9.42\times 10^{-4}}$ (`D6`). |
| **Volumetric Holding Cap & Seam Area** | $\dot{q}_{\text{hold}} = \mathbf{7.256\text{ MW/m}^3}$; $V_{\text{active}}(25\text{ kW}) = \mathbf{3.445\text{ L}}$; $A_{\text{skin}}(100\ \mu\text{m}) = \mathbf{34.45\text{ m}^2}$ | **`SUPPORTED`** | Proves $25\text{ kW}$ conditions a $5.87\text{ m}\times 5.87\text{ m}$ parting seam (`Task_01_v2`, `OpenCodeBP`). |
| **Excavation Energetics & Workforce** | $V = 140,351\text{ m}^3$; $E_{s,\text{NME}} = \mathbf{26.19\text{ MJ/m}^3}$ ($5.73\times$ gain); **$989\text{ masons}$** ($130$ hybrid seam spall) | **`SUPPORTED`** | Fixes v1 $24,725\text{ mason}$ double-count (`M7`); assumed $E_{s,\text{cav}} = 35\text{ MJ/m}^3$ is `PROPOSED-INCOMPLETE` (`T02-004` $\to$ `T-2`). |
| **Cavity Acoustics & Mode Ladder** | $f_{100} = 34.40\text{ Hz}$, $Q = 1,941.3$, $\delta_{\text{bl}} = 0.552\text{ mm}$, $1,570.80\text{ Pa/m}$, 6 degenerate pairs $<160\text{ Hz}$ | **`SUPPORTED`** | Barabar $R_a \approx 0.1\text{–}2.0\ \mu\text{m}$ is `PRIOR-CONSISTENT` (archaeometry) / `PROPOSED-INCOMPLETE` for unmeasured cave dimensions (`T-9`). |
| **Deccan Earthquake $b$-Value (`B1`)** | **$b = 1.2532$**, $\text{CI}_{95}\ [1.1292,\, 1.3900]$, $\text{SD} = 0.0682$, $M_c = 4.4$, $N \ge M_c = 492$ ($N_{\text{total}} = 973$) | **`SUPPORTED` (`OWN-TEST`)** | Executed on 2000–2026 USGS ComCat (`Ellora ±10°`, `AgentA/outputs/bfit_comcat.json`). Laboratory NME slow-dynamics fit (`nme_fit.json`) voided per `D2` (`T-1`). |
| **Dynamic Strain–$g$ Coupling (`B2`)** | $\kappa_{\text{req}} = (\delta g/g)/\varepsilon_{\text{ac}} = \mathbf{6.80 \times 10^{-4}}$ at $21.5\text{ kHz}$ vs. static $\kappa_{\text{allowed}} \le 10^{-11}$ | **`SUPPORTED`** (arithmetic) / **`PRIOR-CONSTRAINED`** (static) / **`PROPOSED`** (`E1` / `T-5`) | Remediation `D5`: static $\kappa \le 10^{-11}$ does not close dynamic kHz coupling; `E1` (`T-5`) remains the primary bench discovery test. |
| **Coherence Ladder (`L2`)** | Classical vs. quantum crossover $f_{\text{th}}(300\text{ K}) = \mathbf{6.251\text{ THz}}$; $n_{\text{th}}(21.5\text{ kHz}, 300\text{ K}) = \mathbf{2.907\times 10^8}$ | **`SUPPORTED`** | Remediation `D11`: `L2_COHERENCE_LADDER_v2.csv` carries explicit evaluation frequency $f$ in column header (`21.5 kHz` acoustic vs. `100 MHz` SQUID). |
| **Schumann / `CRY4` & `PEGS` / Bio Gaps (`B3`, `B4`)** | $B_{\text{CRY4}} / B_{\text{Schumann}} = \mathbf{3.57 \times 10^7}$; $\Delta g_{\text{bio}} / \Delta g_{\text{PEGS}} = \mathbf{1.0 \times 10^7}$ | **`SUPPORTED`** (ratio math) / **`PRIOR-CONSTRAINED`** (external bars) | Remediation `D4` & `D8`: external biological thresholds (`35.7 µT`, `10⁻³ g`) tagged *(not re-fetched)* and graded `PRIOR-CONSTRAINED`. |
| **`E4` Network & Quantum Scaling (`B5`)** | $\text{UL}(N=10) = \mathbf{0.145\text{ nm/s}^2}$; $\text{UL}(N=30) = \mathbf{0.0838\text{ nm/s}^2}$; quantum-limited $\text{UL} = \mathbf{0.0145\text{ nm/s}^2}$ ($\delta g/g \approx 1.5\times 10^{-12}$) | **`SUPPORTED`** (`DERIVATION`) | Scales our `OWN-TEST` `E4` baseline ($0.459\text{ nm/s}^2$ at $N=2$) by $\sqrt{N_{\text{stations}}}$ (`T-4`). |

---

## 4. Complete Remediation of `XTR-01` Defects (`D1`–`D13`)

Every defect identified in [`CORPUS_INTEGRATION_REPORT_XTR01.md`](CORPUS_INTEGRATION_REPORT_XTR01.md) (§4 `D1`–`D13`) has been resolved in this Revised Edition and staged inside [`C:\LuxAura\study\revision\xtr01_canonical\`](revision/xtr01_canonical/):

1. **`D1` (Pass 2 Placeholder Verdict in `AgentA/hard_data_extract.csv`):** Merged with `AgentB/hard_data_extract.csv`, where all 25 rows carry verified `PASS` statuses (`revision/xtr01_canonical/hard_data_extract_R11.csv`).
2. **`D2` (Tautological Fit in `AgentA/outputs/nme_fit.json`):** Voided and excluded from `revision/`; `L3_MEMORY_LADDER_v2.csv` marks the NME slow-dynamics exponent as `PROPOSED (deferred to T-1)` rather than `COMMAND`.
3. **`D3` (Truncated `AgentA/outputs/L1_strain_ladder.csv` and `L3_memory_ladder.csv`):** Voided in favor of Track B's 7-row `L1_STRAIN_LADDER.csv` and 5-row `L3_MEMORY_LADDER_v2.csv`.
4. **`D4` (Un-fetched Citations Used as Verdicts in `AgentA/BRIDGE_B3_B4.md` & `B6.md`):** Re-graded under `MSL-ADD-01` to `PRIOR-CONSTRAINED` with explicit *(not re-fetched)* tags in `BRIDGE_B3_v2.md`, `BRIDGE_B4_v2.md`, and `BRIDGE_B6_v2.md`.
5. **`D5` (`AgentB/BRIDGE_B2.md` Over-Constraint on `E1`):** Updated in `BRIDGE_B2_v2.md` so $\kappa_{\text{allowed}} = 10^{-11}$ is explicitly scoped as `PRIOR-CONSTRAINED (static strain only)`, preserving `E1` (`T-5`) for dynamic $21.5\text{ kHz}$ strain.
6. **`D6` (`AgentB/STRESS_TEST.md` Conflation of $\mathcal{S}=0$ Root with $Q^{-1}=1$):** Corrected in `STRESS_TEST_v2.md` so $\varepsilon = 2.96\times 10^{-4}$ is labeled as the zero-modulus root $\mathcal{S}(\varepsilon) = 0$ and $\varepsilon = 9.42\times 10^{-4}$ as the unit loss-tangent limit $Q^{-1} = 1$.
7. **`D7` (Incomplete Deferrals in `AgentB/DEFERRALS.md`):** Expanded in `DEFERRALS_v2.md` to log `T-1` (raw TenCate digitization), `R14` citation registration for `B3`/`B4`/`B6`, and `L3` normalization.
8. **`D8` (Prohibited External Verdict Words in Track A Bridges):** All `CONTRADICTED` / `INCONSISTENT` labels derived from outside literature replaced with `PRIOR-CONSTRAINED` in `BRIDGE_B1_v2.md`..`BRIDGE_B6_v2.md` and `claims_ledger_regraded.csv`.
9. **`D9` (Un-merged Publication Plans):** Merged into `revision/xtr01_canonical/PUBLICATION_PLAN_v2.md`, combining Track B's 5-paper roadmap + `T-1..T-9` test queue with Track A's 6 target journals and 8 graphic specs.
10. **`D10` (`A3-weak` Onion-Layer Status in Public Reflection):** Explicitly stated in §1 of [`PUBLIC_REFLECTION_ARGON_REVISION.md`](PUBLIC_REFLECTION_ARGON_REVISION.md) and §2 of [`FINAL_MASTER_ANALYSIS_ARGON_REVISION.md`](FINAL_MASTER_ANALYSIS_ARGON_REVISION.md) as **`PROPOSED` with 3 falsifiers and no own poroelastic test (`T-3`) run yet**, alongside the `E4` synodic null (`CONTRADICTED`) and Deccan ComCat $b = 1.2532$ (`SUPPORTED`).
11. **`D11` (Frequency Ambiguity in `L2` Coherence Ladder):** Fixed in `L2_COHERENCE_LADDER_v2.csv` by labeling `n_th_at_21.5kHz_acoustic_or_100MHz_SQUID` and adding an explicit `eval_freq_Hz` column.
12. **`D12` (Workspace Path Convention):** Documented across all Revised Edition manifests and scripts (`AgentA/` and `AgentB/` in root, canonical merged outputs in `revision/xtr01_canonical/`).
13. **`D13` (Semantic Glossary Merge):** Merged into a unified 18-term `revision/xtr01_canonical/semantic_glossary_merged.csv` with dual Vedic readings (`R9`), `MSL-ADD-01` statuses, and paired tests.

---

## 5. Ground-Truth Ledger (Revised Edition — `MSL-ADD-01`)

- **`SUPPORTED` (`20` Claims — Own Tests & Self-Contained Derivations):**
  - **Executed `OWN-TEST` Positive (`1`):** Deccan-region `USGS ComCat` Gutenberg–Richter $b = \mathbf{1.2532}$ ($\text{CI}_{95}\ [1.1292, 1.3900]$, $M_c = 4.4$, $N = 492$, `Ellora ±10°`, 2000–2026, `AgentA/outputs/bfit_comcat.json`).
  - **Self-Contained `DERIVATION` / `COMMAND` (`19`):** NME backbone $\mathcal{S} = \mathbf{0.5600}$, $G_{\text{backbone}} = \mathbf{16.80\text{ GPa}}$, $\sigma_t^{\text{eff}} = \mathbf{11.225\text{ MPa}}$ · Zero-modulus root $\mathcal{S}(\varepsilon)=0$ at $\varepsilon = \mathbf{2.96\times 10^{-4}}$ · Loss limit $Q^{-1}=1$ at $\varepsilon = \mathbf{9.42\times 10^{-4}}$ · Holding power $\dot{q}_{\text{hold}} = \mathbf{7.256\text{ MW/m}^3}$, $V_{\text{active}}(25\text{ kW}) = \mathbf{3.445\text{ L}}$, $100\ \mu\text{m}$ seam area $A_{\text{skin}} = \mathbf{34.45\text{ m}^2}$ · Stokes skin depth $\delta_\nu = \sqrt{2\nu/\omega}$ ($14.95\ \mu\text{m}$ at $21.5\text{ kHz}$ to $0.870\text{ m}$ at $27.55\text{ d}$) · Griffith surface-energy invariance ($E_{s,\text{NME}} = \mathbf{26.19\text{ MJ/m}^3}$, **$989\text{ masons}$** at Kailasa) · Cavity $f_{100} = 34.40\text{ Hz}$, $Q = 1,941.3$, $\delta_{\text{bl}} = 0.552\text{ mm}$, $1,570.80\text{ Pa/m}$, 6 degenerate pairs · Rankine–Hugoniot $7.482 / 8.213\text{ GPa}$, Mach 5.5 $T_2 = 2,046.5\text{ K}$, $\Delta P = 3.462\text{ MPa}$ · Petukhov–Pokrovskii $S_0/\hbar = 196.59$, $\tau_0 = 0.5324\text{ ps}$, $\epsilon^{5/4}$ · Thermal crossover $f_{\text{th}}(300\text{ K}) = \mathbf{6.251\text{ THz}}$ · `E4` network scaling $\text{UL}(N=10) = \mathbf{0.145\text{ nm/s}^2}$, $\text{UL}(N=30) = \mathbf{0.0838\text{ nm/s}^2}$, quantum-limited $\mathbf{0.0145\text{ nm/s}^2}$ · Vedic *pāṭha* braided checksum distance (`VC-08`).
- **`CONTRADICTED` (`4` Claims — Own Tests & Conservation Laws):**
  - `E4` lunar-synodic gravimetry null ($\text{UL} = 0.459\text{ nm/s}^2$, $\delta g/g < \mathbf{4.68\times 10^{-11}}$, `OWN-TEST`) · Closed-cavity mechanical weight cancellation no-go ($838\text{ kN}$ on walls, $1,048\text{ kN}$ on floor, `DERIVATION`) · Constant-$\omega$ substrate Kepler gate ($T = 2\pi/\omega_{\text{eff}} \neq a^{3/2}$, `DERIVATION`) · Acoustic single-quantum `ATP` bond cleavage ($hf/E_{\text{ATP}} = \mathbf{2.617\times 10^{-10}}$, $31.83\text{ octaves}$ below bond energy, `DERIVATION`).
- **`INCONSISTENT` (`16` Claims — Internal Arithmetic & Parameter Self-Contradictions):**
  - Berktay $-86.20\text{ dB}$ roll-off (`ACB01-001`) · `Narayanastra` $Q_d^2 = 816.3 \implies 1.86\times$ walking gain (`M01-005`) · $21.5\text{ kHz}$ phonon condensation at $300\text{ K}$ ($n_{\text{th}} = 2.91\times 10^8$, `A02-001`) · $\varepsilon = 10^{-3}$ bulk vitrification at $Q^{-1} = 1.061 > 1$ (`M01-004`) · "40 octaves sound $\to$ light" ($34.22\text{ octaves}$ exact) · Eleven v1 table/formula self-contradictions fixed in `_v2.md`.
- **`PRIOR-CONSTRAINED` (`26` Claims) & `PRIOR-CONSISTENT` (`19` Claims):**
  - Every comparison against external published bars (`MICROSCOPE`, `PREM`, `IceCube`, `Collinson 2024 +0.55 V`, `Altmann 2001`, `Dales 1964`, `RRUFF`, `Kumeta 2025`, `Sena 2005`, `Xue 2020 G spread`, `B2` static $\kappa \le 10^{-11}$, `B3` $3.57\times 10^7$ `CRY4` gap, `B4` $1.0\times 10^7$ `PEGS` gap, `B6` *Nautilus* banding).
- **`PROPOSED` (`3` Claims) & `PROPOSED-INCOMPLETE` (`3` Claims):**
  - `A3-weak` Onion-Layer / Breathing-Crevice lens + `E4-Mm` poroelastic refit (`T-3`) · `A2` dynamic kHz strain–$g$ coupling (`E1` / `T-5`, $\kappa_{\text{req}} = 6.80\times 10^{-4}$) · `L1`–`L3` slow-dynamics exponent bridge (`T-1`) · `T02-004` ($E_{s,\text{cav}} = 35\text{ MJ/m}^3 \to \text{T-2}$) · `T03-004` (Barabar impulse response $\to \text{T-9}$).
- **`ALLEGORY` (`4` Claims):**
  - $\Psi_g$ (`A04-001`), $\Xi_{23D}$ (`A02-002`), $P_{\text{bs}}$ (`A03-001`), and Pascal Buri glaciology analogy (`A04-002`).

![Twelve ideas by cost and payoff: E1 and the E4 refit come first](FINAL_MASTER_ANALYSIS_figures/fig2_ideas_cost_vs_payoff.png)

*End of `FINAL_MASTER_ANALYSIS_REVISION.md`. Full 95-row re-evaluated ledger in [`extrapolation_XTR01/ARGON/claims_ledger_regraded.csv`](extrapolation_XTR01/ARGON/claims_ledger_regraded.csv) and canonical Revised Edition package in [`revision/`](revision/).*
