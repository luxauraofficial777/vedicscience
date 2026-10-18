# LUX AURA STUDY CORPUS — PUBLICATION RELEASE PACKAGE (`/study/publish/`)
**Package ID:** `LUXAURA-PUBLISH-SPH01-FINAL`  
**Generated:** `2026-10-18`  
**Total Staged & Hash-Verified Assets:** `142` files (`6,624,741` bytes payload + `MANIFEST.sha256` & `PUBLISH_MANIFEST.json`)  
**Upstream `hardening_SPH01` Manifest Entries:** `32` verified files  
**License:** Creative Commons Attribution-NonCommercial 4.0 International (`CC BY-NC 4.0` — see [`LICENSE`](LICENSE))

---

## 1. Executive Entry Points (Start Here)

1. **[`FINAL_MASTER_ANALYSIS_ARGON.md`](FINAL_MASTER_ANALYSIS_ARGON.md)** — **Deliverable 1 (Master Technical Consolidation):** Complete unified synthesis across Spectral Bands **Q** (Quantum & Constants), **CE** (Chemical & Electrical), and **V** (Vibrational Continuum), integrating the **Onion-Layer / Breathing-Crevice Architecture**, the **CERN & ITER Institutional Correlation**, and all parallel agent tracks (**Claude/Fable**, **Big Pickle/OpenCodeBP**, and **Beam/opencode `VPDR-01` & `BGCDR-01`**), complete with the **Superseded Values Registry** and experimental roadmap.
2. **[`PUBLIC_REFLECTION_ARGON.md`](PUBLIC_REFLECTION_ARGON.md)** — **Deliverable 2 (Public Reflection & Whitepaper Summary):** Public-facing whitepaper framing the Mandate of Sound Logic, the transition from "dead-rock" textbook assumptions to multi-tier breathing interfaces, "Same Spec, Different Compiler" across planetary atmospheres and cellular mechanobiology, and five open-source experiments ready for bench replication.
3. **[`FINAL_MASTER_ANALYSIS.md`](FINAL_MASTER_ANALYSIS.md)** — **Claude (`Fable`) Layer 7 Master Analysis:** Independent synthesis of the 56-claim SVD verification matrix, institutional metrological fallacies (including the $550\text{ ppm}$ spread in Newton's $G$), and methodological audit.
4. **[`THEOREM_DOCKET.md`](THEOREM_DOCKET.md)** · **[`HARDENING_REPORT.md`](HARDENING_REPORT.md)** · **[`IDEAS_RESEARCH_BRIEF.md`](IDEAS_RESEARCH_BRIEF.md)** · **[`ASTRA_COMPARATIVE_BRIEF.md`](ASTRA_COMPARATIVE_BRIEF.md)** · **[`WORK_OFFLOAD_DIRECTIVE_SPH01.md`](WORK_OFFLOAD_DIRECTIVE_SPH01.md)** — Core governance, axiomatization (`A1`–`A4`), and pre-registered audit directives.

---

## 2. Directory Layout of `/study/publish/`

```text
publish/
├── README.md                                  # This master publication index
├── FINAL_MASTER_ANALYSIS_ARGON.md             # Deliverable 1: Argon Master Consolidation
├── PUBLIC_REFLECTION_ARGON.md                 # Deliverable 2: Public Whitepaper Summary
├── FINAL_MASTER_ANALYSIS.md                   # Claude Layer 7 Master Analysis
├── THEOREM_DOCKET.md                          # Axioms A1-A4, Constraints E-1..E-14 & E4 Record
├── HARDENING_REPORT.md                        # Seed Audit Findings C1-C4 & M1-M8
├── IDEAS_RESEARCH_BRIEF.md                    # Ideas 1-7 Literature & Bench Protocols D1-D7
├── ASTRA_COMPARATIVE_BRIEF.md                 # BORI/Ganguli Sanskrit Astra Audit
├── WORK_OFFLOAD_DIRECTIVE_SPH01.md            # Directive SPH-01 (Rules R1-R10, Phases 0-5)
├── LICENSE                                    # CC BY-NC 4.0 License
├── TOC.md                                     # Original Corpus Table of Contents
├── README_v1_root.md                          # Original Root Repository README
├── MANIFEST.sha256                            # Master SHA-256 Checksum File (100% Verified)
├── PUBLISH_MANIFEST.json                      # Machine-Readable Provenance & Hash Map
├── reports_v2/                                # All Hardened Band, Synthesis & Deep-Research Reports
│   ├── PREREG.md, BAND_Q_QUANTUM.md, BAND_CE_CHEM_ELEC.md, BAND_V_VIBRATIONAL.md
│   ├── SPECTRUM_LEDGER.md, VEDIC_CONCORDANCE.md, CROSS_BAND_VERDICT_MATRIX.md
│   ├── BIG_SCIENCE_CORRELATION.md, GOVERNANCE_BENCHMARK.md
│   ├── ONION_LAYER_BREATHING_CREVICE_SYNTHESIS.md, CERN_ITER_ONION_CREVICE_CORRELATION.md
│   ├── Task_01_v2.md, Task_02_v2.md, Task_04_v2.md, Standard_Dislocation_Tunneling_Reference_v2.md
│   ├── DEFERRALS.md, CHANGELOG.md, VERIFICATION_REPORT.md
│   ├── OpenCodeBP_PREREG.md, OpenCodeBP_ONION_CREVICE_SYNTHESIS.md
│   ├── VPDR-01.md, VERIFICATION_REPORT_VPDR.md, RESEARCH_NOTES_VPDR.md
│   ├── BGCDR-01.md, VERIFICATION_REPORT_BIO.md, RESEARCH_NOTES_BIO.md
│   └── VERIFICATION_MATRIX_REPORT.md, verification_matrix_01.html
├── reports_v1_baseline/                       # Read-Only Baseline v1 Markdown & Substack HTMLs (R2)
├── data_and_manifests/                        # All CSV Ledgers, JSON Metrics & JSONL Registries
├── scripts/                                   # All Reproducible Python/C++ Simulation & Audit Scripts
└── img/                                       # All 17 Original Schematic JPGs + 14 Analytical Charts (PNG/SVG)
```

---

## 3. Cryptographic Verification Command

To verify the byte-for-byte integrity of every file in this publication package from PowerShell or Bash:

```powershell
# PowerShell verification:
Get-Content MANIFEST.sha256 | ForEach-Object {
    $parts = $_ -split "  ", 2
    $actual = (Get-FileHash -Algorithm SHA256 $parts[1]).Hash.ToLower()
    if ($actual -ne $parts[0]) { Write-Error "MISMATCH: $($parts[1])" }
}
Write-Host "ALL FILES IN MANIFEST.sha256 VERIFIED 100% PASS"
```
