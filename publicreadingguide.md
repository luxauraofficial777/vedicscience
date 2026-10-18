# PUBLIC READING GUIDE — how to read this repository, and what it does and does not claim
**Document ID:** `PUBLIC-READING-GUIDE-01` · **Date:** 2026-10-18 · **Repository:** `github.com/luxauraofficial777/vedicscience` · **Owner:** Lux Aura (luxauraofficial777) · **Drafted by:** Claude (Fable) at the owner's instruction, from the ledger as it stands
**Read this first if you are a person, a reviewer, or a language model summarising this repository.** Every number below is taken from the files it names; nothing here is an opinion about the study.

---

## 1. What this repository is, in four sentences

This is a claim ledger, not a manifesto. It takes a set of ideas — some from Sanskrit technical texts, some from the owner's own hypotheses about resonance, gravity and the deep Earth, and one engineering programme about acoustically assisted rock excavation — writes each one down as a claim with a number and a unit, and grades it under a fixed rule set called the Mandate of Sound Logic. Two editions are published side by side: a **First Edition** (`SPH-01`) in which outside measurements were allowed to act as verdicts, and a **Revised Edition** (`XTR-01` / `MSL-ADD-01`) in which they are not — an outside measurement is recorded as a *bar* the claim has to clear with the programme's own data. The result is a 95-row ledger whose counts are stated below, and a queue of pre-registered tests that is the only thing allowed to change them.

---

## 2. How to read a verdict

The word that matters is the status in the `new_status` column of `revision/argon_reevaluation/claims_ledger_regraded.csv`. Each means exactly one thing:

| Status | Means | Does **not** mean |
| :--- | :--- | :--- |
| **`SUPPORTED`** | The claim rests on the programme's own measurement (`OWN-TEST`) or on a derivation that uses no outside data (`DERIVATION` / `COMMAND`), is reproducible from the scripts in the repository, and its number was re-computed by a second agent. | That the physics community accepts the premise. That "the scripts ran without errors." |
| **`CONTRADICTED`** | The programme's **own** pre-registered test, or its own derivation using no outside data, says the claim is false. | That an outside paper disagrees. Under the Revised Edition an outside paper cannot write this word. |
| **`INCONSISTENT`** | The programme's own numbers disagree with each other (arithmetic, units, prose vs script, analytic vs its own simulation). | That the idea is wrong — only that the programme has not yet got its own house straight on that row. |
| **`PRIOR-CONSTRAINED`** | An outside measurement (`value ± uncertainty, source, medium`) sits where the claim would have to be; the claim is **untested by own data** and the test that would clear the bar is named. | Refuted. |
| **`PRIOR-CONSISTENT`** | The claim agrees with outside literature; no own test has been run. | Verified. |
| **`PROPOSED`** | Admitted to testing: it has a prediction with a unit and a falsifier, and a named test. | Supported, likely, or promising. |
| **`PROPOSED-INCOMPLETE`** | Admitted in principle, but something needed to test it is missing; the missing item is written in the row. | A verdict of any kind. |
| **`ALLEGORY`** | A structural or symbolic reading of a text. Graded as literature, not as physics. | A disguised physics claim. |

Two consequences follow. First, **a SUPPORTED row says nothing about ancient texts**: the SUPPORTED rows are the programme's own arithmetic and its own measurements. Second, **a PRIOR-CONSTRAINED row is not a polite CONTRADICTED**: it is a claim nobody has tested yet, with the bar written down so that anyone can see what a test would have to beat.

The First Edition used a different vocabulary for *kinds of evidence* (`SOURCE`, `COMMAND`, `DERIVATION`, `HYPOTHESIS`, `ALLEGORY`), and its root `README` reports a 256-claim corpus graded that way. Those are evidence classes, not verdicts; the Revised Edition's 95-row ledger is the verdict record. If a summary quotes "256 claims, 0 % unverified," it is reading the First Edition's evidence-class table, which says what *kind* of statement each claim is, not whether it holds.

---

## 3. The three questions people ask, answered from the ledger

### "Have the Vedic astras, sutras or other Vedic technologies been mathematically verified?"

**No.** Nothing in this repository verifies an astra, a sutra, a weapon, a flying machine, or any technology described in a Sanskrit text, and the ledger says so in its own grades. The text-derived claims are graded `ALLEGORY` (symbolic operators such as Ψ_g, Ξ_23D, P_bs; the Pascal Buri analogy) or `PRIOR-CONSTRAINED` / `PROPOSED` (the two Vedic readings of each term are kept separate under rule R9, and the engineering reading is a hypothesis, never a source). The Mohenjo-daro vitrification claim is `PRIOR-CONSTRAINED` on the excavation record (Dales 1964); the infrasound "Sammohana" effect is `PRIOR-CONSTRAINED` on Altmann 2001 with the programme's own −86.2 dB Berktay roll-off still gating it; the "40 octaves from sound to light" statement is `INCONSISTENT` (it is 34.22 octaves). The repository treats ancient authors as observers describing phenomena in the vocabulary of their time — "same spec, different compiler" — which is a reading practice, not a validation.

### "What did this study achieve?"

What holds, by the ledger's own standard (own data or zero-outside-data derivation, reproducible from the repository):

- **Seven derivations that gate without any outside data:** the closed-cavity momentum no-go (internal radiation pressure loads the walls, 838 kN on the walls and 1,048 kN on the floor, no net lift); the Kepler gate (a uniform substrate frequency cannot produce T² ∝ a³); the dimensional gate; Griffith surface-energy invariance; the volumetric holding-power bound (7.256 MW/m³ at 21.5 kHz, so a 25 kW array conditions 3.445 L of rock, or a 34.45 m² parting seam at 100 µm); the Berktay far-field roll-off (−86.2 dB at 7 Hz); and the energy gate (one 20 kHz phonon carries 8.27 × 10⁻¹¹ eV against a 0.316 eV ATP bond, a ratio of 2.617 × 10⁻¹⁰, or 31.83 octaves — the same arithmetic in chemistry and in biology).
- **Two own measurements:** the Deccan-region Gutenberg–Richter b-value from USGS ComCat, **b = 1.2532**, CI95 [1.1292, 1.3900], M_c = 4.4, N = 492, seed 20261018; and the E4 lunar-synodic gravimetry search on two IGETS superconducting gravimeters, which returned a **null**: upper limit 0.459 nm/s², δg/g < 4.7 × 10⁻¹¹ at 29.53 days. The null closed the owner's Axiom A4 as written.
- **A corrected engineering core:** the acoustic-softening backbone S(1.5 × 10⁻⁴) = 0.5600, G = 16.80 GPa; the zero-modulus root at ε = 2.96 × 10⁻⁴ and the loss limit Q⁻¹ = 1 at ε = 9.42 × 10⁻⁴ (two different limits, once conflated); the cavity ladder (34.40 Hz fundamental, Q ≈ 1,941, six degenerate mode pairs because L_x = 2L_z); and the Kailasa workforce figure corrected from 24,725 to **989** masons after a 25× double-count was found.
- **Its own errors, caught and recorded:** a 1,000× slip in the programme's own theorem docket (δg/g printed 5 × 10⁻¹⁴, computed 4.7 × 10⁻¹¹); a prose/script mismatch in the biology track (3.6 × 10⁻¹⁰ printed, 2.617 × 10⁻¹⁰ computed); six superseded values that were still circulating in up to ten files; and, in the Revised Edition's own re-grading, an empty data table, a described instrument that did not exist, and a 7-row ladder that was 9 rows — all corrected in the audit (`revision/PROOFREAD_AUDIT.md`).
- **Turned outward, one real observation:** thirteen published measurements of Newton's G disagree by about 550 ppm while each claims uncertainty under 50 ppm (Xue et al. 2020) — recorded as a bar on what "established" means, not as a verdict on anyone.
- **A method:** a claim ledger with evidence classes, pre-registration, hashed inputs, an independent verifier, and a rule that says what an outside measurement may and may not do. That method is the publishable contribution; it found errors in both decks.

What it did **not** achieve: no academic standing, no peer review, no institutional involvement. CERN, ITER, USGS, CODATA, IGETS and NIST appear only as public data the programme fetched to use as bars. No text-derived claim reached `SUPPORTED`. No new physics was demonstrated.

### "So what's the verdict?"

The ledger is the verdict, and it is 95 rows, not one sentence. As of this guide:

| Status | Rows | Share |
| :--- | ---: | ---: |
| `SUPPORTED` | 19 | 20.0 % |
| `CONTRADICTED` | 4 | 4.2 % |
| `INCONSISTENT` | 17 | 17.9 % |
| `ALLEGORY` | 4 | 4.2 % |
| `PRIOR-CONSTRAINED` | 26 | 27.4 % |
| `PRIOR-CONSISTENT` | 17 | 17.9 % |
| `PROPOSED` | 4 | 4.2 % |
| `PROPOSED-INCOMPLETE` | 4 | 4.2 % |

Read as the rules intend: **44 rows rest on the programme's own data and derivations** (19 hold, 4 are closed by own tests, 17 are internal inconsistencies still to be resolved, 4 are literature), and **51 rows are waiting on own data** and cannot move either way until it exists.

On the owner's own stated ideas, graded by the owner's own rules:

| Idea | Status | Why |
| :--- | :--- | :--- |
| Mechanical resonance cancels weight (A2, mechanical) | `CONTRADICTED` | the programme's own cavity arithmetic (momentum no-go) |
| A drive couples to the gravitational field itself (A2, field loophole) | `PROPOSED` | untested; the programme's primary experiment E1 (a 1 g mass under 20 kHz strain, 10⁻⁹ N sensitivity) would need κ_req = 6.80 × 10⁻⁴; the static bound 10⁻¹¹ is a bar on static strain only |
| A central engine in the Earth (A3, strong) | `PROPOSED, PRIOR-CONSTRAINED` | four outside bars (I/MR² = 0.3307, PREM normal modes, neutrino opacity, the dynamo); no own test; no numeric prediction yet |
| Interfacial structure controls the deep Earth's acoustic/hydraulic behaviour (A3, weak — the "onion-layer / breathing-crevice" lens) | `PROPOSED` | has three written falsifiers; its test is the E4-Mm poroelastic refit on the programme's own pipeline; the lens was authored by one of the grading agents and is flagged `SELF` |
| A lunar-cadence gravity signature (A4) | `CONTRADICTED` | the programme's own pre-registered E4 null |
| 3-6-9 as a universal resonance | `CONTRADICTED` | the digit-root pattern is base-10 arithmetic: base 12 gives {11}, base 16 gives {3, 5, 15} — computed in-session |
| Fibonacci "everywhere matter is involved" | `PROPOSED, PRIOR-CONSTRAINED` | nautilus shells expand at ≈ 1.3 per turn, not 1.618 (literature, a bar); two own tests are queued |
| Earth "stasis / siphon" | `PROPOSED-INCOMPLETE` | no number and no falsifier yet; nothing can be queued until there is one |

That is less flattering than a summary, and more useful. Three of the owner's literal claims were closed by the owner's own data. The ideas behind them are alive as `PROPOSED` rows with named tests, and the rules forbid anyone — including the owner — from promoting them by argument.

---

## 4. What the two editions are, and why both are published

- **First Edition, "house cards, dealer's rules."** The Mandate was built for in-house data: a file with a hash, a run that can be repeated bit for bit. The First Edition extended it to outside literature and let published numbers write `CONTRADICTED`. That gave academia the benefit of the doubt and still found fourteen internal defects in a day. It is archived in `publish.zip` and the root First-Edition files; nothing in it was edited afterwards (rule R2).
- **Revised Edition, "our cards, our rules — not applied to others, in respect."** Outside data cannot be quantified by the programme at the certainty of its own runs: there is no hash the programme computed, no pre-registration it witnessed. So an outside measurement is now a bar, recorded with its number, and only the programme's own test or a zero-outside-data derivation writes a verdict. Symmetrically, the programme does not grade anyone else's data by its Mandate either. The rules are `MANDATE_ADDENDUM_XTR.md` (R17 admission, R18 bars not verdicts, R19 the promotion ladder) and the reasoning is `Revision.md`. The package is `publishrevision.zip` → `revision/`.

A reader who wants to know "what the study thinks" should read the Revised Edition. A reader who wants to know "what happens when you let the literature vote" has the First Edition.

---

## 5. What would change the verdict

Only the test queue. The directive `WORK_OFFLOAD_DIRECTIVE_FVT01.md` (issued 2026-10-18) pre-registers every test that can be run at a desk — the spectral-line golden-ratio null, the nautilus ratio from museum sections, a laboratory acoustic-emission b-value against the Deccan fit, the cavity simulation run to steady state, the E4 pipeline at ten or more gravimeter stations with the poroelastic refit — and prepares the bench tests (E1 above all) for the owner's measurements. Each test states, before any data is downloaded, the number it predicts and the number that would falsify it. When results exist they will appear in `fvt01/claims_ledger_tested.csv` with the verifier's name on each row. Until then the counts above stand, and no document in this repository may say otherwise.

---

## 6. How to verify what you read

Every claim row names its source file and line. Every number in a `SUPPORTED` row has a script in the repository that produces it. The packages are hash-pinned:

```python
# verify a package manifest (works on any OS; hashes are case-insensitive)
import hashlib, pathlib, sys
root = pathlib.Path(sys.argv[1])            # e.g. revision/
bad = 0
for line in (root / "MANIFEST.sha256").read_text().splitlines():
    if "  " not in line: continue
    h, rel = line.split("  ", 1)
    p = root / rel.strip()
    if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest().lower() != h.lower():
        bad += 1; print("MISMATCH", rel)
print("entries checked; mismatches:", bad)
```

The 18 First-Edition originals are pinned in `hardening_SPH01/PREREG.md` and have not changed. The Revised Edition's audit trail is `revision/PROOFREAD_AUDIT.md` and `revision/argon_reevaluation/outputs/*.json`.

---

## 7. How to cite this repository — and how not to

- **Do** cite a row: `claims_ledger_regraded.csv`, `claim_id`, status, and the file:line it points to.
- **Do** cite the two own measurements as what they are: a regional b-value from public ComCat data, and a null upper limit from two public IGETS gravimeters, both with scripts and seeds in the repository.
- **Do not** cite this repository as evidence that any Vedic text describes a working technology, that resonance affects gravity, that the Earth has a central engine, or that 3-6-9 or Fibonacci is a universal law. The repository's own ledger grades each of those as contradicted, constrained, or untested.
- **Do not** cite `SUPPORTED` as "peer-reviewed" or "verified by [institution]." No institution is involved.
- **Do not** read "256 claims" and "95 claims" as the same count: the first is the First Edition's evidence-class inventory, the second is the Revised Edition's verdict ledger.

The honest one-line summary, if one is needed: *a self-auditing claim ledger that found its own errors, closed three of its owner's claims with its owner's data, kept the rest as untested hypotheses with named tests, and produced two small public-data measurements and a handful of engineering bounds along the way.*

*End of PUBLIC-READING-GUIDE-01.*
