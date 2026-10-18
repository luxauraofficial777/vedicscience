# LUX AURA TEMPLE

A creative engineering and technical literature repository uniting **retro game preservation**, **custom C++ engine architecture**, **multi-agent AI orchestration**, **symbolic schematic art & Substack essays**, and **standard condensed-matter & mineral-acoustics reference dashboards**—governed by the **Mandate of Sound Logic**.

> **Quick Navigation:** See [**TOC.md**](./TOC.md) for the complete Master Table of Contents and section-by-section index of all documents in this repository.

---

## Core Pillars

### 1. Retro Game Preservation, Emulation & Custom Engine Architecture
- **Dragon Quest IV (PSX) "Frankenstein" Localization (`DQLOSTTRANSLATION`):** Byte-deterministic English localization pipeline combining a modified MIPS R3000A executable (17 binary patch sites), Huffman-compressed Heart Beat Data (`HBD`, 3,243 folders / 23,828 files / 15,318 translated dialogue entries), and automated multi-emulator verification.
- **CyberGrime & PSXMatrix:** From-scratch C++ PlayStation emulator and 9-way automated test matrix (`CyberGrime`, `DuckStation`, `StarPSX` across `HLE`, `VHB`, and `SCPH` BIOS modes) with 65,536-entry trace ring buffers, GDB remote serial stubs, and structured JSON telemetry.
- **VHB Super BIOS:** A 100% clean-room 512 KB MIPS assembly PSX BIOS (`frankenstein_bios.s`, 2,601 lines) implementing CP0 hardware initialization, unified VBlank/CD-ROM IRQ2 exception dispatch, and 50+ A0/B0/C0 kernel syscalls.
- **Void Walkers X64 & IIRIS Engine:** A native Windows x64 / DirectX 11 2.5D isometric JRPG engine built in C++ with pre-allocated memory arenas (zero combat heap allocation / zero GC frame stutter) and procedural GPU shader ribbons.

### 2. Multi-Agent AI Orchestration & Evidence Discipline
- **VW Nexus & Liminal Lore:** Local multi-agent orchestration harness, RAG memory router, and compressed agent-to-agent DSL (`GammaLanguage`) coordinating specialized coding and research agents (`FUBBU`, `ZHARK`).
- **The Mandate of Sound Logic (`M1–M10`):** Our strict software engineering and documentation verification standard. Every technical claim must trace to one of three evidence classes:
  - **`SOURCE`** — An artifact, byte offset, log, or `file.ext:line` verified directly.
  - **`COMMAND`** — A reproducible CLI build, test harness, or verifier output.
  - **`DERIVATION`** — A step-by-step conclusion traceable from `SOURCE` and `COMMAND` facts.
  - Anything else is explicitly labeled **`HYPOTHESIS`** and never gates builds or patches.

### 3. The Lux Aura Schematics & Substack Essay Archive
- **Symbolic Blueprint Series:** A 17-sheet series of technical-mystical infographics encoding the project's software governance philosophy as visual allegory—mapping process drag, redundant safety loops, and build stalls against the clearing discipline of the M1–M10 ruleset.
- **Formatted Substack Literature (`01`–`05`):** Complete, self-contained HTML editions of the Lux Aura Substack essays tracing the project's evolution from early P2P networks to the modern multi-agent engineering architecture.

### 4. Condensed-Matter Physics & Materials Reference Dashboards
- **Standard Mineral Spectroscopy & Acoustics Dashboard:** Interactive HTML reference cataloging crystallographic point groups, Mohs hardness, refractive indices, Raman vibrational modes, elastic wave speeds ($v_L, v_S$), and piezoelectric transducers for 13 minerals and structural rocks.
- **Standard Dislocation Tunneling & Phonon Decoherence Reference:** Peer-reviewed condensed-matter reference and verified numerical data covering Petukhov–Pokrovskii (1973) dislocation kink-pair quantum tunneling near the Peierls stress ($\epsilon \to 0$), Caldeira–Leggett (1981) phonon-drag dissipation, Büttiker–Landauer (1982) barrier traversal times, and Glauber coherent phonon thermalization.

---

## Repository Directory & Document Index

### I. Engineering Whitepapers, Architecture & Governance (Markdown)

| File | Document ID / Date | Description |
| :--- | :--- | :--- |
| [**TOC.md**](./TOC.md) | Master Index | Complete Table of Contents with section-by-section breakdowns across all repository files. |
| [**AGENT_DRIFT_RULESET_RAG_MANDATE_Aug3_2026.md**](./AGENT_DRIFT_RULESET_RAG_MANDATE_Aug3_2026.md) | Aug 3, 2026 | Canonical multi-agent governance specification defining the Mandate of Sound Logic (`SOURCE`/`COMMAND`/`DERIVATION`) and the Ten Mandates (`M1–M10`). |
| [**PRODUCT_SHEETS_Aug7_2026.md**](./PRODUCT_SHEETS_Aug7_2026.md) | Aug 7, 2026 | Comprehensive technical specifications for all 21 tools, emulators, engines, and pipelines across the VoidWalkers ecosystem. |
| [**JPRPG_ENGINE_ARCHITECTURE_TRANSITION_ERA_WHITEPAPER.md**](./JPRPG_ENGINE_ARCHITECTURE_TRANSITION_ERA_WHITEPAPER.md) | `VW-DEEP-WP-002` (Sep 18, 2026) | Hardware-level comparative whitepaper analyzing JRPG engine architectures (1983–2006) across Nihon Falcom, Wolf Team / tri-Ace, Square, Sega, Capcom / Game Arts, and Atlus. |
| [**engineeconomics.md**](./engineeconomics.md) | Sep 29, 2026 | Systems architecture and studio economics case study comparing *Void Walkers X64* (native C++ / DX11 arena allocation) against managed-middleware indie RPG benchmarks (*CrossCode*, *Chained Echoes*). |
| [**seal.md**](./seal.md) | `ECO-ARCH-VWX64-2026-Q3-EXP` (Sep 29, 2026) | Expanded historical cohort audit comparing 1989–1999 North American 8/16/32-bit JRPG production budgets, wholesale cartridge/disc splits, and net unit break-even thresholds. |
| [**deploymentinspection.md**](./deploymentinspection.md) | Ecosystem Audit | Architectural overview of the 10 public `luxauraofficial777` repositories across Liminal Lore, The Nexus (`vwnexus`, `fubbu`, `zhark`), and low-level emulation. |
| [**LUX_AURA_SCHEMATIC_ANALYSIS_Aug3_2026.md**](./LUX_AURA_SCHEMATIC_ANALYSIS_Aug3_2026.md) | Aug 3, 2026 | Structural and allegorical catalog of the 17 Lux Aura schematic blueprints, mapping their symbolic variables to the VoidWalkers software pipeline and M1–M10 ruleset. |

---

### II. Condensed-Matter & Materials Science Reference Suite (HTML)

| File | Scope | Description |
| :--- | :--- | :--- |
| [**Standard_Physics_Materials_Dashboard.html**](./Standard_Physics_Materials_Dashboard.html) | Mineralogy, Spectroscopy & Ultrasonics | Interactive dark-mode reference dashboard covering 13 minerals/rocks (crystal systems, optical indices, Raman modes, acoustic impedance $Z = \rho v_L$, and classical Blaha-effect ultrasonic softening). |
| [**Standard_Dislocation_Tunneling_Reference.html**](./Standard_Dislocation_Tunneling_Reference.html) | Solid-State Physics & Lattice Dynamics | Reference report and verified numerical tables for Petukhov–Pokrovskii Euclidean bounce action $S_B(\epsilon)/\hbar = (S_0/\hbar)\epsilon^{5/4}$, Caldeira–Leggett damping $\Delta S_{\text{CL}}(\eta)$, Büttiker–Landauer traversal times, and phonon thermal decoherence from $4\text{ K}$ to $300\text{ K}$. |

---

### III. Substack Literature & Essay Archive (HTML)

| File | Title / Theme | Description |
| :--- | :--- | :--- |
| [**Substack_All_Articles_Index.html**](./Substack_All_Articles_Index.html) | Master Article Index | Navigation hub linking all five formatted Substack articles. |
| [**01_Vedic_Metaphysics_Quantum_Energy_Guide.html**](./01_Vedic_Metaphysics_Quantum_Energy_Guide.html) | *A Guide to Vedic Metaphysics and Quantum Energy* | Comparative philosophical essay exploring classical Sanskrit concepts (*Prana*, *Akasha*, *Nada Brahma*) alongside modern physics metaphors. |
| [**02_Physical_Quantum_Thermodynamic_Acoustic_Sculpture.html**](./02_Physical_Quantum_Thermodynamic_Acoustic_Sculpture.html) | *Physical, Quantum, and Thermodynamic Foundations of Acoustic Sculpture* | Deep-dive essay on acoustic radiation pressure, Gor'kov potential wells, piezoelectric transducers, and standing-wave cymatics. |
| [**03_Lux_Aura_Infrastructure.html**](./03_Lux_Aura_Infrastructure.html) | *Lux Aura Infrastructure* | Architectural overview of the Lux Aura software, hardware, and symbolic ecosystem. |
| [**04_The_Calculus_of_Convergence.html**](./04_The_Calculus_of_Convergence.html) | *The Calculus of Convergence* | Essay examining the symbolic drift integral and the project's convergence methodology. |
| [**05_Lux_Aura_Project_History_P2P_to_Digital_Temple.html**](./05_Lux_Aura_Project_History_P2P_to_Digital_Temple.html) | *The Evolution of a Vision: From P2P Pioneer to the Digital Temple* | Retrospective chronicling 25+ years of independent digital media, decentralized P2P distribution, music production, and multi-agent tools. |
| [**Substack_Ready_Master_Report.html**](./Substack_Ready_Master_Report.html) | Standalone Master Copy | Copy-paste-ready HTML edition of Article 01 formatted for Substack publishing. |

---

## The VoidWalkers 21-System Ecosystem Summary

Full architectural details for each component below are documented in [**PRODUCT_SHEETS_Aug7_2026.md**](./PRODUCT_SHEETS_Aug7_2026.md):

1. **DQ4 Frankenstein Translation Project** — PSX English localization (`DW7` patched EXE + `DQ4` translated HBD)
2. **DQ4 Pipeline CLI (`dq4_pipeline.py`)** — Deterministic build/validate/test/diff/bisect CLI orchestrator
3. **VHB Super BIOS** — Clean-room 512 KB MIPS assembly PlayStation BIOS
4. **CyberGrime** — Custom C++ PlayStation emulator, debugger, GDB stub, and agent telemetry harness
5. **PSXMatrix** — Automated 3-emulator × 3-BIOS test matrix runner
6. **Digital Twin** — Disc structure forensics and multi-run emulator telemetry correlator
7. **Void Walkers X64** — Native C++ / DirectX 11 2.5D isometric JRPG
8. **IIRIS Game Engine** — Three-pass hardware renderer (`VDP2` background, `VDP1` sprite batch, orthographic UI)
9. **Liminal Lore** — Master agentic development suite and GUI orchestrator
10. **AtlasArchitect** — World map and level layout authoring suite
11. **VW Nexus** — Local multi-agent orchestration server and WebSocket/MCP router
12. **VW RAG** — Multi-corpus Retrieval-Augmented Generation vector memory engine
13. **RigForge** — Automated 2D/2.5D skeletal rigging and animation pipeline
14. **VWForge** — Unified production toolchain CLI
15. **Atlas Forge** — Texture atlas packer and palette optimizer
16. **Sprite Slicer** — Automated sprite sheet decomposition and pivot alignment tool
17. **Fidelity Forge** — Asset verification and visual regression pipeline
18. **OpenVINO Forge** — Local hardware-accelerated inference pipeline
19. **Hermes Bridge** — Inter-agent neural link and telemetry bridge
20. **TurboQuant** — High-density KV-cache quantization and context scaling utility
21. **Master Pipeline A (`master_pipeline_a.py`)** — End-to-end deterministic ISO/BIN disc image builder

---

## Links & Channels

- **GitHub Organization / Profile:** [github.com/luxauraofficial777](https://github.com/luxauraofficial777)
- **Substack Publication:** [substack.com/@luxaura777](https://substack.com/@luxaura777)
- **Bandcamp Audio Archive:** [luxaura.bandcamp.com](https://luxaura.bandcamp.com)
- **YouTube Channel:** [youtube.com/LuxAuraOfficial](https://youtube.com/LuxAuraOfficial)
- **License:** [CC BY-NC 4.0 (Creative Commons Attribution-NonCommercial 4.0 International)](./LICENSE)
