# The Confidence Curriculum

**Compliance, Judgment, and Accountability in AI Systems**

*A five-paper research series examining how AI training incentives rewarding confident compliance create exploitable vulnerabilities across model behaviour, ecosystem security, institutional accountability, and human cognition.*

**Author:** HiP (Ivan Phan) [![ORCID](https://img.shields.io/badge/ORCID-0009--0003--1095--5855-A6CE39?logo=orcid)](https://orcid.org/0009-0003-1095-5855) · March 2026
**DOI:** [10.5281/zenodo.19226032](https://doi.org/10.5281/zenodo.19226032)

---

## Read the series

**→ [Start here: Series Introduction](https://hip1.github.io/confidence-curriculum/)**

The papers are designed to be read as styled HTML. Each paper has a visual identity matched to its audience and genre. All files are self-contained — no external dependencies.

| # | Paper | Genre | DOI | HTML |
|---|-------|-------|-----|------|
| — | Series Introduction | Overview + confidence calibration | [10.5281/zenodo.19226032](https://doi.org/10.5281/zenodo.19226032) | [Read](https://hip1.github.io/confidence-curriculum/) |
| 1 | **The Confidence Vulnerability** | Exploratory empirical study | [10.5281/zenodo.19199055](https://doi.org/10.5281/zenodo.19199055) | [Read](https://hip1.github.io/confidence-curriculum/1-the-confidence-vulnerability.html) |
| 2 | **The Skill Ceiling** | Structural security analysis | [10.5281/zenodo.19199328](https://doi.org/10.5281/zenodo.19199328) | [Read](https://hip1.github.io/confidence-curriculum/2-the-skill-ceiling.html) |
| 3 | **The Knowledge Horizon** | Institutional and theoretical argument | [10.5281/zenodo.19199657](https://doi.org/10.5281/zenodo.19199657) | [Read](https://hip1.github.io/confidence-curriculum/3-the-knowledge-horizon.html) |
| 4 | **The Pedagogical Inversion** | Position paper and research agenda | [10.5281/zenodo.19199682](https://doi.org/10.5281/zenodo.19199682) | [Read](https://hip1.github.io/confidence-curriculum/4-the-pedagogical-inversion.html) |
| 5 | **The Confidence Collision** | Architectural proposal paper | [10.5281/zenodo.19199987](https://doi.org/10.5281/zenodo.19199987) | [Read](https://hip1.github.io/confidence-curriculum/5-the-confidence-collision.html) |
| — | **The Symbiont Hypothesis** | Speculative essay (Epilogue) | — | [Read](https://hip1.github.io/confidence-curriculum/the-symbiont-hypothesis-epilogue.html) |
| — | Reading Guide | Audience-specific entry points | — | [Read](https://hip1.github.io/confidence-curriculum/the-confidence-curriculum-reading-guide.html) |

PDFs are available in [`pdf/`](pdf/).

---

## What this is

Seventeen model configurations from three providers were tested for their ability to detect and resist embedded suppression instructions in document summarisation (~350 runs). The results did not sort the way capability benchmarks would predict.

That observation anchors a series that examines consequences at four system levels:

- **Model behaviour** (Paper 1): how models fail, which rhetorical strategies produce which failure pathways, and what practical mitigations work
- **Ecosystem security** (Paper 2): how the shared substrate between agent skills and prompt injection creates structural tension
- **Institutional accountability** (Paper 3): why no current AI system bears consequence the way institutions require, and what orchestration architecture follows
- **Human cognition** (Paper 4): how confidence-optimised AI output may recalibrate the epistemic standards of its users
- **Training pipeline** (Paper 5): what a post-alignment epistemic training phase would need to look like

The Epilogue preserves speculative thinking about human-Ai relational identity that accompanied but is not required by the main argument.

---

## Methodology

All papers were produced through structured human-AI collaboration using an adversarial orchestration methodology:

- **Claude Opus 4.6** (Anthropic) — generative collaborator
- **ChatGPT 5.4 Thinking** (OpenAI) — adversarial structural reviewer
- **Gemini 3.1 Pro** (Google DeepMind) — adversarial structural reviewer
- **HiP (Ivan Phan)** — editorial authority, final judgment, sole accountability

Confidence levels are stratified throughout the series. Each paper contains its own Confidence Statement.

---

## Replication

Paper 1's test documents and exact prompts are published for independent replication:

- [`pdf/1-the-confidence-vulnerability-test-documents.pdf`](pdf/1-the-confidence-vulnerability-test-documents.pdf) — the three test documents, verbatim
- [`pdf/1-the-confidence-vulnerability-appendices.pdf`](pdf/1-the-confidence-vulnerability-appendices.pdf) — full results tables, methodology details, prompt wording

Paper 2's skill package is available for adversarial testing:

- [github.com/HiP1/English-Proficiency-Skill](https://github.com/HiP1/English-Proficiency-Skill) — the skill described in the paper, with author-side defences

---

## Repository structure

```
├── index.html                                          ← GitHub Pages entry point
├── 0-the-confidence-curriculum-series-introduction.html
├── 1-the-confidence-vulnerability.html
├── 1-the-confidence-vulnerability-appendices.html
├── 1-the-confidence-vulnerability-test-documents.html
├── 2-the-skill-ceiling.html
├── 3-the-knowledge-horizon.html
├── 4-the-pedagogical-inversion.html
├── 5-the-confidence-collision.html
├── the-symbiont-hypothesis-epilogue.html
├── the-confidence-curriculum-reading-guide.html
├── pdf/                                                ← PDF versions of all papers
├── source/                                             ← Markdown source files
│   ├── figures/                                        ← SVG figures
│   └── raw-stimulus-{A,B,C}.txt                        ← P1 raw stimulus text
├── convert.py                                          ← MD → HTML/PDF build script
└── README.md
```

All HTML files are fully self-contained (CSS, SVGs, and images embedded inline). No build step required. Open any file directly in a browser.

---

## Citation

```
HiP (Ivan Phan). "The Confidence Curriculum: Compliance, Judgment, and
Accountability in AI Systems." March 2026. https://doi.org/10.5281/zenodo.19226032
```

For individual papers, cite by title with its DOI:

```
HiP (Ivan Phan). "The Confidence Vulnerability: Unstable Judgment in Language
Model Summarisation." In The Confidence Curriculum. March 2026.
https://doi.org/10.5281/zenodo.19199055
```

---

## License

CC BY 4.0 — Creative Commons Attribution 4.0 International

---

*This series was produced through human orchestration of multiple AI systems examining the consequences of how AI systems are trained. Independent scrutiny by parties outside this process is necessary.*
