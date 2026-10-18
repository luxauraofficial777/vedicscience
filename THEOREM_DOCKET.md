# THEOREM DOCKET — Frequency-Fundamental Gravity Research Program
**Document ID:** `THEOREM-DOCKET-01` · **Date:** 2026-10-18 · **Status:** OPEN RESEARCH FILE
**Companion:** `HARDENING-01` (`HARDENING_REPORT.md`)
**Program owner hypothesis (stated verbatim, 2026-10-18):** *"The planet is an onion — prison planet. Time/mass/gravity; engineered constants from void interpolation at the center of the Earth. Inside the Earth there is a dwarf star or black hole creating a gravitational vortex that gives objects inertia and their weight — not the mass of the Earth itself. Resonance (frequency) can cancel or displace gravitational force, as sound shatters glass. Gravity isn't real; frequency is."*
**Methodology provenance:** calculations performed on a lunar calendar cadence (owner note; recorded here as `HYPOTHESIS`-class methodology provenance — see §7-E4 for the one testable form of this claim).
**Honesty clause:** nothing in this docket is asserted as true. Each axiom is graded: **OPEN** (unconstrained by existing data), **CONSTRAINED** (existing data limits viable forms), **CONTRADICTED** (existing data excludes the stated form). "We may be correct — we may be false" is implemented as a falsifier per axiom.

---

## §1. Axiomatization (P1)

**A1 — Ontological.** There is no primitive parameter "mass." Inertial response and gravitational coupling emerge from the mode spectrum of an underlying substrate oscillating at characteristic frequencies; G and m are derived quantities.
*Operational form:* the ratio m_inertial/m_gravitational (equivalence principle) and any composition dependence of gravitational response are computable from substrate mode structure, not postulated.
*Falsifier:* any verified Eötvös-type composition dependence at the stated sensitivity, or any consistent separation of m_i and m_g.
*Grade:* **OPEN but tightly CONSTRAINED** — m_i = m_g to η < 1.5×10⁻¹⁵ (MICROSCOPE 2022, Touboul et al., PRL 129 121102). Any substrate model must reproduce this to 15 decimal places.

**A2 — Cancellation.** Driving a body or field at a resonant frequency ω_d can nullify gravitational traction (weight) without the support force relocating to the drive apparatus.
*Operational form:* ∃ ω_d, drive protocol: net contact force on a freely-supported test mass → 0 while the drive structure bears none of the weight.
*Falsifier:* the force-balance experiment E1 (§8).
*Grade:* **CONTRADICTED as stated for mechanical/acoustic drives** — see §3 no-go (momentum conservation). Surviving loophole: coupling to the gravitational field itself (modulating local g), which is **OPEN** as a tabletop test — no experiment has looked for kHz-frequency g-modulation above ~10⁻⁹ N force sensitivity. This loophole is the live research program.

**A3 — Geogenic.** Earth's gravity is produced by a central object/engine (dwarf star, black hole, void-interpolation node), not by the mass distribution of the planet.
*Operational form:* predicted anomalies in: seismic wave travel times, Earth's moment of inertia factor I/MR², neutrino transmission, geomagnetic field generation, clock-redshift profile vs radius.
*Falsifier:* existing seismology/geodesy (rows E-1…E-5 of §4).
*Grade:* **CONTRADICTED in the stated strong form** (§4). *Not dead in weak form:* the deep Earth is genuinely not fully understood — LLSVPs at the core-mantle boundary, inner-core hemispherical anisotropy, and the 2023 "inner-inner core" are open problems where the owner's instinct points at real frontier data (§6).

**A4 — Chronometric engineering.** Physical constants and time-flow are locally engineered variables of the "prison architecture," detectable as anomalies in clocks or constant-drift; the lunar calendar is causally operative.
*Operational form:* unmodeled periodicities at lunar periods (13.66 d sidereal / 29.53 d synodic) in gravimeter or atomic-clock residual series; or drift of Ġ, ħ, e beyond known bounds.
*Falsifier:* E4 (§8) — mine public IGETS superconducting-gravimeter data for unmodeled lunar-period residuals; clock-network bounds.
*Grade:* **CONSTRAINED.** Known lunar signal = solid-Earth tides, modeled to ~10⁻¹⁰ g; any ADDITIONAL lunar-period anomaly must beat tide-model residuals. Ġ/G < ~10⁻¹⁴ yr⁻¹ (LLR, Hofmann & Müller 2018, CQG 35 035015). Clock gravitational redshift verified at cm baselines (Chou et al. 2010, PRL 104 070401). **OPEN niche:** no one has published a dedicated search for *lunar-periodicity* in modern gravimeter residuals as a "prison signal" — this is cheap, falsifiable, and uses open data.

---

## §2. Dimensional Gate & Kepler Re-derivation (P2)

Any frequency-substitution for G·m₁m₂/r² must first pass dimensional analysis. Gravitational potential per unit mass has dimensions [Φ] = m²/s²; frequency alone gives 1/s. Viable constructions require either c (relativistic) or a length L: Φ ~ ω²L², or Φ ~ c²(ω/ω₀)².

**Kepler test (the killer):** assume a frequency-native orbital law a_minimal: v²/r = ω_eff²·r with constant substrate frequency ω_eff (the pure "frequency replaces G M" substitution). Then v = ω_eff·r ⇒ orbital period T = 2π/ω_eff — **the same for every orbit**, contradicting the observed Kepler third law T² ∝ a³ (and T²/a³ = 4π²/GM constant to ~10⁻⁹ across the solar system; binary pulsars confirm it in strong field). To restore Kepler you must make ω_eff r-dependent — at which point you have rebuilt geometry as the carrier of gravitational structure, i.e., you are back inside general relativity's accounting in new language.
*Verdict:* naive G,m → f substitution **fails at the first derivation**. A viable A1 theory must produce the observed ω_eff(r) spectrum from substrate mode structure — this is the precise mathematical task the program now owns. (Note: the owner's observation "Jupiter is bigger but less dense" is **correct and standard** — H/He vs rock/metal composition; it does not require a central engine.)

---

## §3. Momentum-Conservation No-Go for Cavity Resonance (P3/P4, computed COMMAND+DERIVATION)

System: the corpus's own cavity (V = 37.5 m³, S = 70 m², f₀ = 34.4 Hz, Q = 1941, driven at 25 kW — `sim_cavity_acoustics.py` parameters).

| Quantity | Value | Class |
| :--- | :--- | :--- |
| Stored acoustic energy E = P·Q/ω | 2.245×10⁵ J | DERIVATION |
| Energy density u | 5,987 J/m³ | DERIVATION |
| Standing-wave radiation pressure ~2u | **11.97 kPa** | DERIVATION |
| Weight of rock in cavity (107 t) | **1.048×10⁶ N** | SOURCE (ρ, g, V) |
| Max radiation force on walls (P_rad·S) | 8.38×10⁵ N — **ratio to weight = 0.80** | DERIVATION |
| Lithostatic stress at 2.5 m depth | 69.9 kPa (→ P_rad is ~17% of it) | DERIVATION |
| Solid-borne intensity for ε_ac = 1.5×10⁻⁴ | 2.65×10⁵ W/m² at 2.52 MPa stress amp | DERIVATION |
| Dissipation at ε = 1.5×10⁻⁴, 21.5 kHz | 7.26×10⁶ W/m³ → 25 kW sustains **3.4 L** | COMMAND |
| Dissipation at ε = 10⁻³ (Module VII) | 2.15×10⁹ W/m³ → 25 kW sustains **11.6 cm³** | COMMAND |

**The theorem (why this matters for A2):** inside a closed cavity the standing wave's momentum is exchanged with the **walls**. The net force on the enclosed contents' center of mass is zero — resonance inside a box cannot levitate the box's contents; the support force relocates to the foundations by momentum bookkeeping. This is why the 0.80 ratio is *not* a discovery of gravity cancellation: the walls feel 838 kN, the floor feels the same 1048 kN it always did. Acoustic excavation works precisely *because* resonance delivers real mechanical force to boundaries — that is engineering, and it is sound (pun intended). It is also exactly the equivalence-principle logic Eöt-Wash/MICROSCOPE test: internal stresses do not alter gravitational response (η < 1.5×10⁻¹⁵).
**The surviving loophole (honest part):** if a drive couples to the **gravitational field** rather than to the walls — modulating local g at drive frequency — the no-go does not apply. No tabletop experiment has searched for kHz g-modulation at force resolution ~10⁻⁹ N. That search (E1) is open, cheap, and falsifiable. Do it.

---

## §4. Constraint Ledger / Falsification Matrix (P3+P3-EXT+P6)

| # | Quantity / claim constrained | Best measured bound | Source | Axiom hit |
| :--- | :--- | :--- | :--- | :--- |
| E-1 | Moment of inertia factor I/MR² | **0.3307** (uniform=0.4, hollow shell=0.667, point-core→0) | Geodesy/SEED | A3 strong — CONTRADICTED |
| E-2 | Interior structure | PREM: liquid outer core r=3480 km, solid Fe inner core r=1220 km, ρ≈13 g/cm³; free oscillation spectra fit to high order | Seismology (normal modes since 1960) | A3 strong — CONTRADICTED (1 M☉ BH ⇒ r_s≈3 km, invisible nowhere) |
| E-3 | Earth transparency to neutrinos | Earth opaque to TeV–PeV neutrinos at measured rate (no continent-scale voids) | IceCube | A3 strong — CONTRADICTED |
| E-4 | Geodynamo mechanism | Liquid-iron convection required; static/dwarf-star core cannot produce observed field geometry | Geomagnetism | A3 strong — CONTRADICTED |
| E-5 | Engineered time | Gravitational redshift confirmed at cm baselines; Ġ/G = (−5.0±9.6)×10⁻¹⁵ yr⁻¹ | Chou 2010; Hofmann & Müller 2018 | A4 — CONSTRAINED, open at lunar-periodicity level (E4-test) |
| E-6 | Composition-dependent gravity | η = (1.5±2.3±1.5)×10⁻¹⁵ (Ti-Pt, null) | MICROSCOPE 2022, PRL 129 121102 | A1 — CONSTRAINED |
| E-7 | Short-range 1/r² violations | Yukawa bounds to 52 μm | Lee et al. 2020, PRL 124 101101 | A2 loophole narrowing |
| E-8 | Strong-field gravity | GR confirmed (PSR J0348+0432; double pulsar) | Antoniadis 2013; Kramer et al. | A1/A2 strong-field |
| E-9 | Frame-dragging/geodetic | GPB: geodetic ~0.3%, frame-dragging ~5% of GR predictions | Everitt et al. 2011, PRL 106 221101 | A3 (vortex-style cores) |
| E-10 | Speed of gravity | \|c_g−c\|/c < 3×10⁻¹⁵ | GW170817, ApJL 848 L13 | Any "vortex" signal-carrier model |
| E-11 | Prior shielding claims | Podkletnov rotating-SC (1992, ~10⁻⁵): unreplicated (Hathaway 2003 null); Tajmar: artifact-attributed | Physica C 1992; Physica C 2003; reanalyses | A2 prior art — no verified positive |
| E-12 | Acoustic×gravity shielding | **No peer-reviewed claim found on record** | literature search 2026-10 | A2 — **open experimental niche (E1)** |
| E-13 | Resonance↔gravity coupling EXISTS (detection mode) | Mechanical resonators detect gravity: Weber bars (1969, unconfirmed) → Nautilus/Auriga (~10⁻²²/√Hz) → LIGO (~10⁻²³/√Hz) | GW literature | Supports "coupling exists"; direction is detection, not cancellation |
| E-14 | Lunar-period residuals in gravimeters | Earth tides modeled to ~10⁻¹⁰ g; **no published dedicated search for anomalous lunar-period residuals** | IGETS/GGP open data | A4 — testable NOW (E4-test) |

---

## §5. Lineage Ledger (P5) — with corpus-fidelity check

| Figure/text | What the primary source actually says | Provenance class | In corpus? |
| :--- | :--- | :--- | :--- |
| **Vedic astras** (Brahmastra in Mahabharata/Ramayana) | Mythological weapons invoked with mantras; texts exist (critical editions), no physical-engineering spec; the Mahabharata "modern-weapon" readings are a 20th-century revivalist interpretation (Kulkarni/Tulsias line), not classical exegesis | PRIMARY text exists; physical reading = SECONDARY | Yes (Module VII framing). Mohenjo-daro tie-in fails archaeology — HARDENING C3 |
| **Tesla** — "resonance cancels gravity" | No traceable primary statement in Tesla's writings/patents/interviews; attributions are popular-secondary. Tesla's verified work: mechanical/electrical resonance, high-voltage transmission | SECONDARY ATTRIBUTION ONLY | Partially — "Tesla-derived 3-6-9 harmonic sequence" (02:131) is allegory; "Tesla Cortex Hive" is fictional |
| **Mesmer** — "fluid/magnetism animates life" | 1779 *Mémoire sur la découverte du magnétisme animal*: animal magnetism/fluid hypothesis — about living bodies, not gravity | PRIMARY TRACEABLE (not gravity) | Not present |
| **Bob Lazar** — "science of gravity, element 115, anti-gravity craft" | 1989 KLAS interviews (George Knapp); no verified academic record, no peer-reviewed evidence, no reproducible demonstration | NO EVIDENCE / JOURNALISTIC | Not present |
| **Podkletnov** — rotating superconductor gravity shielding | 1992 Physica C claim (~10⁻⁵); independent replications null (Hathaway 2003) | UNREPLICATED | Not present — prior art you must beat |
| **Barabar caves / "Chevalier" 34.4 Hz** | Fringe web sources (ALBA Project, "Song of the Stone"); ALBA lists 57.1 Hz for Karan Chaupar | FRINGE / UNSOURCED | Yes — HARDENING M3 (remove or retag) |
| **"Prison planet" / engineered-constants theme** | Owner's synthesis; self-aware Philip K. Dick trope acknowledgment (2026-10-18 statement) | HYPOTHESIS (owner) | Implicit in Ψ_g/Ω layer of articles 02–04 |
| **Pascal Buri glaciology** | Real researcher (Tapado glacier, dry Andes meltwater); used as *analogy* for signal ablation | REAL SOURCE, analogical use | Cited in 02/03 but absent from works-cited (HARDENING M8) |

---

## §6. Corpus Stance Map — what your own documents say about each axiom

- **A1/A2 vs Standard reference:** `Standard_Dislocation_Tunneling_Reference.html:100` — phonons/strain "do not alter spacetime metrics or gravity." This is the corpus's own honesty boundary and it **contradicts** the Ψ_g passages (02:141, 03:94, 04:90 "gravity is a variable layer that can be exploited"). Resolution required: either the Standard note is the house standard (and Ψ_g is allegory), or Ψ_g is physics (and the Standard note must go). **Recommendation: keep the Standard note; formally tag Ψ_g as allegory — consistent with the project's existing method of coding governance as schematic art (README §3).**
- **Supporting:** Module VI cavity benchmark, Module II metamaterial bands, and the NME literature base are real, conventional, script-verified physics — the credible core the program can build on. E-13 shows "resonance↔gravity" is literally how gravitational waves are detected — the *detection* half of the intuition is mainstream.
- **Undermining:** Module VII (C1), the G_eff contradiction (C2), Mohenjo-daro/Barabar (C3, M3) — these currently give a reviewer permission to discount everything, including the sound parts. Fixing them is pro-thesis, not anti-thesis.

---

## §7. Experimental Roadmap — cheapest falsification first (P3/P6)

**E1 — kHz g-modulation search (the A2 loophole test, ~$2–5k).** Drive a high-Q cavity (their own design) at eigenmodes; monitor a co-located test mass with a precision force balance / electrostatic gravimeter at drive frequency and harmonics. Sensitivity achievable: ~10⁻⁹ N. A null result bounds any wall-independent coupling 6+ orders below weight for gram-scale masses — publishable as the first dedicated acoustic-coupling-to-gravity bound (E-12 gap). *This is the experiment nobody has done and the program is uniquely positioned to do.*
**E2 — Blaha/NME weight-invariance test.** Ultrasonically condition a basalt sample at ε_ac = 1.5×10⁻⁴ (their validated regime) on a 10⁻⁷-resolution balance during drive. Tests whether lattice conditioning alters gravitational response. Expected (standard): null. Cost: laboratory access.
**E3 — Torsion-balance + acoustic drive.** Podkletnov-geometry without the superconductor: rotating + resonantly driven masses on a torsion balance; differential signal search. Must beat the artifact controls that killed Podkletnov/Tajmar (thermal, magnetic, seismic).
**E4 — Lunar-periodicity gravimetry (free, open data).** Download IGETS/GGP superconducting-gravimeter series; remove solid-Earth tide models; search residuals at 13.66 d / 29.53 d and lunar-hour bands. Direct test of A4's one quantitative signature. Public datasets, Python (scipy Lomb-Scargle), a weekend of compute. — **EXECUTED 2026-10-18, see §7b.**
**E5 — Seismic normal-mode citizen science.** Earth's eigenmode spectra (mode database at IRIS) fit residuals — test for unexplained split lines or anomalous Q that a central-engine model would demand. Data public.

---

## §7b. E4 Execution Record — Lunar-period gravimetry on real SG data (EXECUTED 2026-10-18)

**Status: EXECUTED — primary target (A4 lunar-cadence signature) NOT FOUND; one marginal band identified as known-geophysical after follow-up.**

**Data (SOURCE-class, open access).** IGETS Level-3 gravity residuals via EOST Strasbourg (`igets.u-strasbg.fr`): monthly 1-minute files, `res_fil` in nm s⁻². Level 3 already has solid-Earth tides (DDW99+HW95/FES2014), ocean tidal loading, polar motion + LOD, atmospheric loading (ERA5), and AG-calibrated drift removed — i.e., exactly the "remove tide models, inspect residuals" procedure §7 prescribed, done to publication standard by the data provider. Stations/instruments: Strasbourg C026 (95 months, 2011-01→2018-11; 2011 start avoids the documented 2009–2010 tilt-compensation malfunction) and Djougou OSG-060, Benin (36 months, 2016–2018) as geographically independent check. 166 files ≈ 670 MB; parsers and cache in `e4_lunar_residual_search.py`, `e4_cache/`. Citations: Boy et al. 2017, doi:10.5880/igets.st.l1.001 / igets.dj.l1.001; EOSTproducts_v2.pdf.

**Method (COMMAND-class, pre-registered in script before seeing results).** 1-min → hourly means; removed mean, linear, annual, semiannual terms; joint least-squares sinusoid fit at 13 known lunar/tidal frequencies (synodic 29.53 d, tropical 27.21 d, anomalistic/Mm 27.55 d, Mf 13.66 d, MSf 14.77 d, plus M2/S2/N2/K2/O1/K1/P1/Q1); blind Lomb-Scargle scan of the 6.7–33 d band with white-noise FAP and local-continuum ratio; M2 complex-envelope modulation test; two coherence tests (split-half phase stability; st026-vs-dj060 phase on common 2016–2018 epoch). Candidate = SNR ≥ 5 **and** coherent across ≥1 test.

**Results (DERIVATION-class; full numbers in `e4_lunar_residual_output.json`).**
- **Primary target — lunar synodic month (29.53 d): NULL.** st026 amplitude 0.12 nm s⁻², SNR 0.69, **95 % UL 0.46 nm s⁻² ⇒ δg/g < 5×10⁻¹⁴**; not coherent with dj060 (Δφ = 109–133°); split-half Δφ = 118°.
- Tropical month, Mf, MSf: all SNR ≤ 1.5, ULs 0.4–0.6 nm s⁻².
- Semidiurnal/diurnal lunar bands (M2, N2, O1, K1, …): amplitudes ≤ 0.4 nm s⁻² — the Level-3 tide removal is confirmed, no "excess" lunar response beyond established ocean-loading model error.
- **One marginal band:** anomalistic month Mm (27.55 d) at st026, amp 0.90 nm s⁻², white-noise SNR 5.0; blind scan peak at 27.48 d (FAP ~10⁻⁵·⁵ against white noise). Failed both pre-registered coherence tests (split-half Δφ = 61°; cross-station at common epoch not phase-stable in the pre-registered joint fit), so verdict at pre-registration = **NO_COHERENT_ANOMALY**.
- **Post-hoc follow-up** (`e4_followup_mm.py`, `e4_followup_mm_output.json`, explicitly flagged POST_HOC): the Mm-band excess is present at *both* stations (st026 0.90 / dj060 2.41 nm s⁻²) and survives red-noise continuum correction (SNR_red 4.7 / 3.7), but is **strongly non-stationary** — per-year amplitude χ²/dof ≈ 1150/8 (st026) and 1149/6 (dj060). A real coherent lunar-period residual must be phase- and amplitude-stationary over 8 years; this one waxes and wanes. **Classification: known-geophysical band** — residual long-period ocean-tide-model error and hydrological/groundwater signals have broad power at 27–28 d; the anomalous *amplitude ratio* between an equatorial hydrological site (Djougou) and a temperate one (Strasbourg), with random-walk yearly amplitudes, is the signature of loading/hydrology, not of an engineered lunar coupling.

**Interpretation for the docket.** A4's one quantitative signature — a coherent, globally repeating residual locked to the lunar cadence — is bounded below 0.5 nm s⁻² (synodic) / ~1.2 nm s⁻² (anomalistic) at Earth's surface by 8 years of the most sensitive gravity data that exists. For the resonance-cancellation thesis (A2/Ψ_g) this is a strong surface null: whatever coupling exists between laboratory-scale resonant systems and gravity cannot have a long-period lunar-modulated component at the 10⁻¹³ g level. It does **not** touch the E1 kHz loophole (different frequency regime, §3), which remains the open, actionable test.

---

## §8. Verdict Summary

| Axiom | Grade | Path forward |
| :--- | :--- | :--- |
| A1 frequency-fundamental | OPEN, CONSTRAINED (η<1.5×10⁻¹⁵) | Build substrate models that reproduce EP to 15 digits; Kepler test (§2) is gate #1 |
| A2 resonance cancellation | CONTRADICTED for mechanical drives (§3 no-go); OPEN for field-coupling loophole | Run E1 — the loophole is untested; turn a belief into a number |
| A3 inner-Earth engine | CONTRADICTED strong form (E-1…E-4); weak form rides on real open problems (LLSVPs, inner-inner core) | Retarget A3 at the *actual* mysteries — they are strange enough |
| A4 engineered constants | CONSTRAINED; **E4 EXECUTED — lunar-cadence signature NOT FOUND** (synodic δg/g < 5×10⁻¹⁴; Mm-band marginal = known hydrology/loading, §7b) | A4's open signature closed as-null; only route left for A4 is a different, sharper prediction |

**Program maxim (owner's own standard, applied to the owner):** a claim that cannot be falsified cannot be hardened. Everything in this docket has a falsifier. That is the documentation that did not exist and now does.

*End of THEOREM-DOCKET-01.*
