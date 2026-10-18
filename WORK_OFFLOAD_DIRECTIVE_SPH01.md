# WORK OFFLOAD DIRECTIVE — Spectral Research & Hardening
**Directive ID:** `SPH-01` · **Issued:** 2026-10-18 · **Owner:** Lux Aura (luxauraofficial777) · **Drafted by:** Claude
**Executors:** implementation agents (Gemini, Big Pickle, or equivalent) · **Verifier:** one independent agent that did none of the work
**Output folder:** `C:\LuxAura\study\hardening_SPH01\` (create it; never edit original source docs)

---

## 0. Mission (owner's words)

> "Analyze on a quantum, chemical/electrical, and vibrational (sound) wave spectrum our speculative data against the organized quantum/chemical-electrical data and the vedic data … correlate all projects and data relativity against ITER/CERN development/projections."

In practice:
1. Extract every claim in the speculative corpus.
2. Place every frequency and energy on one spectrum.
3. Test each claim in three bands (Quantum, Chemical/Electrical, Vibrational) against established reference data and the verified Vedic passages.
4. Map everything onto current ITER and CERN work and timelines.
5. Have an independent agent verify the result.

---

## 1. Rules of engagement (binding)

- **R1 — Mandate classes.** Tag every claim and number `SOURCE` / `COMMAND` / `DERIVATION` / `HYPOTHESIS`. Allegory gets the tag `ALLEGORY`.
- **R2 — Originals are read-only.** Write all outputs into `hardening_SPH01\`. Corrections to source docs go in as new versioned files (e.g. `Task_04_v2.md`), never as edits.
- **R3 — No citation from memory.** Every reference must resolve to a fetched DOI or URL, with the quoted passage saved in `citations.jsonl`. Anything unchecked is marked *(not re-fetched)* and cannot support a SUPPORTED verdict.
- **R4 — Pre-register.** Before touching any dataset, commit hypotheses, thresholds and analysis code to `PREREG.md` (git hash + timestamp).
- **R5 — Symmetry.** State in advance what supports and what falsifies each claim. A null result is a result and gets reported the same way.
- **R6 — Determinism (M1/M8).** Pin dependency versions (`requirements.txt`), fix random seeds, hash every output (SHA-256) in `outputs/MANIFEST.sha256`. Re-running from a clean checkout must reproduce byte-identical tables.
- **R7 — Deferrals.** Anything skipped or postponed gets an entry in `DEFERRALS.md`: what, why, and what is needed to resume.
- **R8 — Safety.** No human exposure to high-level sound or infrasound, and no weapon design work. Effects on people come from published literature only.
- **R9 — Two readings for Vedic passages.** Record the standard Indological reading and the program's reading side by side, each with its own evidence tag.
- **R10 — Quota.** At most two agents run at once. Phases 0–1 are sequential; the band tracks can run two at a time.

---

## 2. Inputs

- **Speculative corpus:**
  - `Task_01`–`Task_05`
  - `Consolidated_Master_Report_AS_NME.md` (Modules I–VII)
  - Substack articles `02`–`04`
  - the 17 schematics in `img\`
  - `THEOREM_DOCKET.md` (axioms A1–A4)
  - the owner's stated ideas in `IDEAS_RESEARCH_BRIEF.md` §0
- **Organized/reference set:** listed per band in §5.
- **Vedic set:** verified passages in `ASTRA_COMPARATIVE_BRIEF.md`; GRETIL e-texts (BORI Mahabharata, Rigveda Saṃhitā, Baroda Ramayana); Ganguli and Griffith translations for English checks.
- **Prior audits (seed findings to re-verify, not assume):** `HARDENING_REPORT.md`, the research report of 2026-10-18 (Part C), `IDEAS_RESEARCH_BRIEF.md`, `ASTRA_COMPARATIVE_BRIEF.md`. Seed findings are listed in §11.

---

## 3. Phase 0 — Claim extraction (1–2 days)

**Output:** `claims_ledger.csv`, one row per atomic claim.

| Column | Content |
| :--- | :--- |
| `claim_id` | e.g. `T01-014` |
| `file`, `line` | canonical copy (deduplicate by SHA-256; 17 files exist in duplicate) |
| `text` | verbatim |
| `band` | `Q`, `CE`, `V` or a combination; `X` for cross-band |
| `quantity`, `value`, `unit` | numbers with units |
| `freq_Hz`, `energy_eV` | if the claim names a frequency or energy |
| `claimed_class` | the class the doc gives it (e.g. "verified") |
| `vedic_link` | astra or passage ID, if any |
| `verdict`, `actual_class`, `evidence` | filled in Phases 2–3 |

**Acceptance:** every numeric claim in Tasks 01–05, the Master report and articles 02–04 is captured. The verifier samples 10% of rows against the source.

---

## 4. Phase 1 — The Spectrum Ledger (1 day)

**Output:** `spectrum_ledger.csv`, `SPECTRUM_LEDGER.md`, and one chart (log frequency axis from 10⁻⁶ Hz to 10¹⁵ Hz, coloured by band).

**Columns:**
- source and label;
- f (Hz);
- quantum energy hf (eV);
- hf/k_BT at 300 K;
- thermal occupation n_th at 300 K;
- wavelength (acoustic: in air, water and basalt; EM: in vacuum);
- regime (classical / quantum);
- band;
- reference anchor.

**Seed entries:**
- **Corpus:** 7 Hz beat; 34.4 Hz cavity mode; 20.35–28 kHz rock resonances; 25 kHz phonon mode; 40.000/40.007 kHz carriers; 10 GHz phonon (`verify_quantum_resonance.py`); Raman 464 cm⁻¹ (≈13.8 THz); Si–O stretch ~1000 cm⁻¹.
- **Human/Vedic:** speaking-voice fundamentals ~100–250 Hz; recorded chant pitch (from task V5/A1); bowstring and conch spectra (literature).
- **Earth:** Earth's breathing mode 0.8147 mHz; Schumann resonance ~7.8 Hz *(not re-fetched)*; lunar tidal periods Mf (13.66 d) and Mm (27.55 d).
- **Big science:** ITER ion cyclotron heating 40–55 MHz; ITER electron cyclotron heating 170 GHz (hf ≈ 7×10⁻⁴ eV); LHC radio-frequency cavities 400 MHz *(not re-fetched)*.
- **Chemistry anchors:** bond dissociation energies ~1–10 eV; molecular vibrations ~0.05–0.5 eV.

**Pre-registered key analysis:** a 20 kHz sound quantum carries 8.3×10⁻¹¹ eV, about 5×10¹⁰ times less than a ~4 eV chemical bond. Every Sound Logic chemistry claim must therefore name its energy-concentration mechanism: cavitation collapse, nonlinear focusing, or coherent many-quantum coupling. Claims that name none are scored UNTESTABLE-AS-WRITTEN and sent to rewrite.

---

## 5. Phase 2 — Band tracks

Each band follows the same template: claims to test → reference data → Vedic correspondence → tasks → pass criteria.

### Band Q — Quantum

**Claims:**
- Λ_sl as a "sub-physical field operator" (article 02 §II.3);
- "coherent phonon condensation" at 21.5 kHz;
- tunneling "assisted" by sound;
- the ΔT_drift integral;
- the Ξ_23D equation;
- A1 (mass derived from substrate frequencies);
- A4 (engineered constants).

**References:**
- NIST CODATA constants;
- the primary papers by Petukhov & Pokrovskii (Sov. Phys. JETP 36, 336, 1973), Caldeira & Leggett (1981), and Büttiker & Landauer (1982) *(not re-fetched)*;
- quantum acoustics, i.e. when phonons really are quantum: Chu et al., *Science* 358, 199 (2017), GHz phonons at millikelvin *(not re-fetched)*;
- origin of mass: the Higgs mechanism, and lattice QCD showing most nucleon mass is field binding energy (Dürr et al., *Science* 322, 1224, 2008) *(not re-fetched)*;
- MICROSCOPE 2022 and lunar laser ranging (Hofmann & Müller 2018).

**Vedic:** śabda/nāda (sound as primordial), mapped at concept level only and tagged `HYPOTHESIS` with its Indological reading alongside.

**Tasks:**
- **Q1** — Classify the regime of every quantum claim using the Spectrum Ledger (n_th ≫ 1 means classical).
- **Q2** — Repair `Standard_Dislocation_Tunneling_Reference`:
  - reconcile its three S₀ prefactors and its τ₀ formula;
  - fix Table 2's temperature law and the factor-2 ring-down error;
  - resolve the ε^(5/4) vs ε¹ scaling (the document's own rescaling gives ε¹; check it against the 1973 paper).
- **Q3** — Rewrite Ξ_23D as well-typed mathematics: use √det(JJᵀ) for a non-square map, and give the dimension of each form and its integration domain. If that can't be done, tag it `ALLEGORY`.
- **Q4** — Write an A1 steelman memo covering where mass already emerges from field dynamics (QCD binding, the Higgs mechanism), what A1 must add, and which observation would distinguish it.
- **Q5** — Build a table of current bounds on variation of α, G and μ for A4: Webb 2011 (contested), atomic clocks, Oklo, lunar laser ranging.

**Pass:** every Q claim has a regime, an evidence class, and a verdict.

### Band CE — Chemical / Electrical

**Claims:**
- the bond force-constant table and the piezoelectric table (`Standard_Mineral_Spectroscopy_Acoustics_Reference.md`);
- electromagnetic "stasis" of the atmosphere;
- vitrification chemistry (Fe³⁺→Fe²⁺, Module VII);
- resonant cavity chemistry;
- "compiles differently" under pressure;
- the owner's claim that electrical discharge and chemical bonds vary across environments more than gravity does.

**References:**
- NIST Chemistry WebBook; RRUFF Raman database; Materials Project;
- NRLMSIS 2.0 neutral-atmosphere model;
- Collinson et al., *Nature* (2024), Earth's ambipolar field; Gunell et al., *A&A* 614, L3 (2018);
- Thomas et al. (2016, 2019) and Imperatore et al. (2021) on cavity chemistry;
- Dong et al., *Nature Chemistry* (2017), Na₂He;
- Paschen's law for breakdown voltage vs pressure × gap *(not re-fetched)*.

**Vedic:**
- Vajra as lightning, an electrical discharge whose shock wave is thunder; RV 4.50.5 pairs song with thunder. This is the clearest cross-band (CE + V) passage.
- Agneyastra and Varunastra as a thermal fire/water pair.

**Tasks:**
- **CE1** — Check the bond table against RRUFF spectra and published force constants, and flag any force constants back-fitted to the observed peaks.
- **CE2** — Run the homosphere test (IDEAS-01 D4): compare measured N₂/O₂/Ar ratios against the sorting an electromagnetic hold would produce.
- **CE3** — Build an environment-variance table:
  - Paschen breakdown voltages for Earth air (101 kPa), Mars CO₂ (~600 Pa), Venus CO₂ (~92 bar) and Titan N₂ (~1.45 bar);
  - surface gravity of each body from orbiter-measured GM;
  - the ratio of discharge variance to gravity variance.

  This turns the owner's "discharge varies more than gravity" into numbers.
- **CE4** — Compare Module VII's vitrification mechanism with the experimental literature on burning stone forts (fire and rampart experiments) and the Mössbauer redox studies.
- **CE5** — Review the replication status of resonant cavity chemistry, 2016 to present, listing every replication attempt and its result.

**Pass:** each CE claim has a verdict and a measured anchor.

### Band V — Vibrational / Sound

**Claims:**
- the softening chain in Tasks 01–03 (G_eff, σ_t);
- the excavation energy matrix;
- cavity eigenmodes and the FDTD solver;
- Barabar's 34.4 Hz mode and wall roughness R_a;
- cavitation jet velocity;
- the 7 Hz parametric beat;
- infrasound syncope;
- chirp gating;
- the Narayanastra Doppler trap;
- Earth "dampening" / temporal sync.

**References:**
- Guyer & Johnson, "Nonlinear mesoscopic elasticity," *Physics Today* 52(4), 30 (1999) *(not re-fetched)*;
- Plesset & Chapman, *J. Fluid Mech.* 47, 283 (1971) *(not re-fetched)*;
- Altmann, *Science & Global Security* 9, 165 (2001);
- Berktay, *J. Sound Vib.* 2, 435 (1965) *(not re-fetched)*;
- lithotripsy literature;
- Roult et al. (2010) on Earth's normal modes;
- Vallée et al., *Science* (2017), prompt gravity signals;
- Esposito, Krichevsky & Nicolis, PRL 122, 084501 (2019).

**Vedic:** Sammohana (bowstring twang and conch); Bṛhaspati's song and thunder; śabdavedhi; chant pitch.

**Tasks:**
- **V1** — Resolve the G_eff/σ_t chain to one value at ε = 1.5×10⁻⁴ with a stated drive frequency; source the dispersion factor Re[D] = 0.450 or remove it (HARDENING C2).
- **V2** — Recompute the excavation budget:
  - include the cost of holding the softening field (MW/m³);
  - apply Griffith invariance (σ²/G is constant, so softening doesn't lower fracture energy);
  - correct the workforce figure, which counts chisel efficiency twice (~990 workers, not 24,725).
- **V3** — Fix the FDTD solver:
  - run the C++ code to steady state (at least Q/π cycles);
  - implement a real impedance boundary;
  - reconcile its 1.74 Pa/m with the reported 1,570.80 Pa/m.
- **V4** — Barabar: find any measured acoustic data in peer-reviewed literature, the real chamber dimensions and geometry, and measured polish roughness. Fix the mm→µm roughness error.
- **V5** — ASTRA-01 tasks:
  - A1, chant pitch analysis;
  - A3, parametric demodulation at safe levels;
  - A4, stone-breaking energy benchmark;
  - A5, Doppler sweep.
- **V6** — IDEAS-01 D2: replicate the prompt gravity signal from public data, and estimate whether sound-carried mass is detectable in the same records.
- **V7** (optional, physical) — IDEAS-01 D5: sonochemistry frequency bench test at matched power.

**Pass:** every V claim has a verdict; V1–V3 produce corrected, versioned docs.

### Vedic concordance (runs alongside the bands)

**Output:** `VEDIC_CONCORDANCE.csv` + `.md` (task ASTRA-01 A2).
- Locate every sound term (*śabda, ghoṣa, rava, nāda, svana, nirghāta*) and every *mantra* invocation in the BORI and GRETIL texts.
- Measure their co-occurrence with astra names against a baseline of non-astra battle passages.
- Map BORI ↔ Ganguli section numbers.
- Link each passage to its band(s) and claim IDs.

---

## 6. Phase 3 — Cross-band verdict matrix (1–2 days)

**Output:** `CROSS_BAND_VERDICT_MATRIX.md`, with one row per claim and columns Q / CE / V / Vedic.

- **Cell values:** `CONSISTENT` · `INCONSISTENT` · `UNTESTABLE-AS-WRITTEN` · `OPEN`, plus the evidence class and source ID.
- **UNTESTABLE claims** must get either a testable rewrite (quantity, units, predicted value, measurement) or the tag `ALLEGORY`.
- **Summary section:** claims promoted (supported), demoted, rewritten, or re-tagged as allegory.

---

## 7. Phase 4 — ITER / CERN correlation (2–3 days of desk research)

### 7.1 Status baseline (as of 2026-10-18; re-verify at execution)

- **ITER**
  - The 2024 baseline sets research operation (deuterium) in 2034, full magnetic energy in 2036, and deuterium-tritium operation in 2039, at about €5bn extra cost (Physics World).
  - As of September 2026, 6 of 9 vacuum-vessel sector modules are in the pit. Sector module 9 is on the critical path for early December 2026, the ninth sector was delivered on 7 October 2026, and the schedule is maintained (ANS, 9 Sep 2026).
- **ITER heating**
  - Neutral beams: 2×16.5 MW, deuterium at 1 MeV.
  - Ion cyclotron resonance: 20 MW at 40–55 MHz.
  - Electron cyclotron resonance: 170 GHz, 40 MW initially and up to 67 MW, from 1 MW gyrotrons (iter.org).
- **CERN**
  - The last LHC Run 3 beams were at the end of June 2026, and Long Shutdown 3 began in July 2026 (~4 years).
  - High-Luminosity LHC first operations are targeted for June 2030, with up to 10× the luminosity. The LHC programme runs to 2041.
- **European Strategy (22 May 2026)**
  - FCC-ee (~91 km) is the preferred next large project, at about €16bn for its first phase.
  - A construction decision is expected around 2028, with operation in the mid-to-late 2040s (heise).

### 7.2 Physics-overlap map

**Output:** `BIG_SCIENCE_CORRELATION.md`. For each axiom or claim, name the ITER or CERN measurement that constrains or informs it.

| Program idea | ITER / CERN touchpoint | Task |
| :--- | :--- | :--- |
| **Resonance moves energy into matter** (Sound Logic) | ITER cyclotron-resonance heating: frequency-matched energy transfer at megawatt scale | Compute ITER's average heating power density. Seed estimate: ~73 MW into ~830 m³ of plasma ≈ 0.09 MW/m³ *(verify both figures)*. Compare with the corpus claims of 2.15 GW/m³ (vitrification, ~24,000× higher) and 4–7 MW/m³ (softening, ~50–80× higher). |
| **Electromagnetic "stasis"** (Idea 5) | Tokamak magnetic confinement at 5.3 T holds charged plasma only; neutral particles reach the walls and are pumped out at the divertor *(not re-fetched)* | Quantify what confines charged vs neutral matter, and apply the result to the atmosphere claim. |
| **Acoustic waves in plasma** (Sound Logic vocabulary) | Geodesic acoustic modes, ion-acoustic waves, Alfvén eigenmodes in tokamaks *(not re-fetched)* | Literature map of real "acoustic" modes in fusion plasmas and how they are measured. |
| **Mass is not primitive** (A1) | Higgs mechanism (CERN, 2012); most nucleon mass comes from QCD binding energy | Feed task Q4: what A1 must add beyond the Standard Model. |
| **Gravity and antimatter** (A2/A3) | ALPHA-g: antihydrogen falls down (Anderson et al., *Nature* 621, 716, 2023) *(not re-fetched)*; follow-ups from AEgIS and GBAR | Track the precision roadmap and the bounds it places on any "opposite source" for gravity cancellation. |
| **Atmosphere and charge** (Idea 5) | CERN CLOUD experiment: ions and atmospheric aerosol formation (Kirkby et al., *Nature* 476, 429, 2011) *(not re-fetched)* | Summarise measured ion effects on the atmosphere and feed CE2. |
| **Environment-dependent constants** (Idea 1) | Running couplings measured at LEP and LHC; HL-LHC precision Higgs couplings | Feed task Q5. |
| **Fifth forces / new light fields** (Idea 1, A2) | NA64 and LHC searches for new light bosons | Build a bounds table and identify any regime still open for a screened coupling. |

### 7.3 Projections timeline

**Output:** a table covering 2026–2045, giving each milestone, its date, its source, and what a positive or null outcome would mean for each axiom. Milestones include:
- ITER sector module 9;
- ITER research operation in 2034, full magnetic energy in 2036, and D–T in 2039;
- HL-LHC start in 2030;
- the FCC-ee construction decision around 2028 and operation in the mid-to-late 2040s;
- antimatter-gravity precision results.

### 7.4 All-projects governance benchmark

**Output:** `GOVERNANCE_BENCHMARK.md`.

**Compare:** the Mandate M1–M10 and the program's pipelines (DQ4 pipeline CLI, CyberGrime/PSXMatrix, the VoidWalkers build ledger) against CERN and ITER practice:
- CERN Open Data Portal and REANA reproducible-analysis platform;
- the DPHEP data-preservation effort;
- Geant4/ROOT validation suites;
- ITER's IMAS data dictionary;
- ITER's nuclear quality-assurance documentation.

**Deliver:** a gap table of adoptable practices, for example a schema/data dictionary for every JSON output, provenance metadata in every file, and versioned containers for scripts.

---

## 8. Phase 5 — Independent verification (1–2 days)

A separate agent that took no part in Phases 0–4:
1. re-runs every script from a clean checkout and checks the SHA-256 manifest;
2. checks a 10% random sample of ledger rows, plus 100% of claims marked SUPPORTED or CONSISTENT;
3. resolves every citation in `citations.jsonl`.

**Output:** `VERIFICATION_REPORT.md`. Disagreements are not resolved by the executor; they go to the owner.

---

## 9. Deliverables (in `hardening_SPH01\`)

```
PREREG.md                     claims_ledger.csv
spectrum_ledger.csv           SPECTRUM_LEDGER.md (+ chart PNG)
BAND_Q_QUANTUM.md             BAND_CE_CHEM_ELEC.md
BAND_V_VIBRATIONAL.md         VEDIC_CONCORDANCE.csv / .md
CROSS_BAND_VERDICT_MATRIX.md  BIG_SCIENCE_CORRELATION.md
GOVERNANCE_BENCHMARK.md       DEFERRALS.md
VERIFICATION_REPORT.md        citations.jsonl
scripts/ (pinned)             outputs/ + MANIFEST.sha256
versioned corrections: Task_01_v2.md, Task_04_v2.md, Standard_Dislocation_Tunneling_Reference_v2.md, ...
CHANGELOG.md
```

---

## 10. Sequencing (cheapest first; at most 2 agents concurrently)

| Step | Track A | Track B | Est. |
| :--- | :--- | :--- | :--- |
| 1 | Phase 0 claim ledger | — | 1–2 d |
| 2 | Phase 1 Spectrum Ledger | Vedic concordance setup | 1 d |
| 3 | Band Q (Q1–Q5) | Band V desk tasks (V1–V4) | 3–5 d |
| 4 | Band CE (CE1–CE5) | Band V data tasks (V5–V6) | 4–7 d |
| 5 | Phase 4 ITER/CERN (7.1–7.4) | Vedic concordance finish | 2–3 d |
| 6 | Phase 3 verdict matrix | — | 1–2 d |
| 7 | Phase 5 verification (independent agent) | — | 1–2 d |
| Opt. | V7 sonochemistry bench test | — | 2–4 wk |

---

## 11. Seed findings to re-verify (from prior audits; do not assume)

1. G_eff at ε = 1.5×10⁻⁴ takes three incompatible values: 6.89 GPa (Task 01), 16.8 GPa (Task 03 and scripts), and a 0.230 ratio (Task 02).
2. The cost of holding the softening field is ~4–7 MW/m³; 25 kW sustains ~3.4 L of rock.
3. Griffith invariance: σ_t ∝ √G makes σ²/G constant, so softening does not lower fracture energy by the corpus's own equations.
4. The excavation workforce counts chisel efficiency twice: ~990 workers, not 24,725.
5. Module VII runs at Q⁻¹ = 1.061 (outside the model) and needs 2.15 GW/m³; the Mach 5.5 overpressure is 3.46 MPa, not 3.41.
6. The C++ FDTD gives 1.74 Pa/m against the reported 1,570.80 Pa/m; the radiation-force column has units of N/m⁴, not N/m³.
7. Barabar's R_a of 0.1–0.5 mm for "mirror polish" is ~1000× too rough; the 34.4 Hz mode is computed, not measured.
8. The ΔT_drift regime ξ ≥ 1 needs ~43 atm of acoustic amplitude in air; Task 03's own operating point is ξ ≈ 0.0006.
9. ξ_jet = 25.085 is fitted to produce the 3.25 GPa target.
10. Narayanastra: the script's damping gives Q ≈ 29, so Q² ≈ 800, not 10³–10⁴; a walking target's Doppler shift is ~⅓ of the resonance linewidth.
11. The 7 Hz beat: parametric demodulation output scales with the square of the difference frequency, roughly −86 dB going from 1 kHz to 7 Hz.
12. Article 01 contains the Master report (`format_all_substack_articles.py:535–540` copies the wrong file); ~50 Works Cited URLs are truncated.
13. Task 04's provenance for the "atomic" quote is wrong: it comes from Pauwels & Bergier (1960), is spliced from Mausala and Karna Parva, and "Gurkha" is von Däniken's mis-transliteration. The 1953 book's co-author is Adamski.
14. `THEOREM_DOCKET.md` needs citation fixes: MICROSCOPE's central value is −1.5×10⁻¹⁵; Gravity Probe B measured frame-dragging to ~19%, not ~5%; the clock redshift result is *Science* 329, 1630; and its Ġ/G value is inconsistent with Hofmann & Müller 2018.

---

## 12. Stop and escalation rules

- If a claim cannot be made testable after one rewrite attempt, tag it `ALLEGORY` or `UNTESTABLE`, log it in `DEFERRALS.md`, and move on.
- If two sources conflict, record both with their evidence classes; do not pick silently.
- Never fabricate data, fits, or citations. A missing value stays missing and is logged.
- If any result would promote a speculative claim to SUPPORTED, stop. Hand it to the independent verifier before it enters any public document.

---

## Sources for §7.1

- [Physics World — ITER 2024 baseline](https://physicsworld.com/a/iter-fusion-reactor-hit-by-massive-decade-long-delay-and-e5bn-price-hike/)
- [ANS Nuclear Newswire — ITER progress, 9 Sep 2026](https://ans.org/news/2026-09-09/article-8375/iter-reports-substantial-progress-in-assembly-and-installation-work)
- [ITER — External heating systems](https://www.iter.org/node/2753)
- [heise — CERN Council strategy decision, FCC-ee](https://heise.de/-11305189)
- [Science Times — LHC enters Long Shutdown 3](https://www.sciencetimes.com/articles/62039/20260706/large-hadron-collider-waves-goodbye-it-enters-long-shutdown-3-after-nearly-20-years-service.htm)

*End of SPH-01.*
