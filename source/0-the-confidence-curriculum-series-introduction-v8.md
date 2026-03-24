# The Confidence Curriculum

### Compliance, Judgment, and Accountability in AI Systems

*What AI systems follow, what they can't judge, and who answers.*

**Author:** HiP (Ivan Phan)
**Date:** March 2026
**DOI:** [10.5281/zenodo.19198621](https://doi.org/10.5281/zenodo.19198621)

---

## The Argument

This paper series examines how training incentives that reward confident, helpful-sounding output over calibrated uncertainty create a tension with what each domain actually requires. We use the term **Confidence Curriculum** to describe that incentive regime. The series traces the tension through model behaviour (Paper 1), ecosystem security (Paper 2), institutional accountability (Paper 3), human cognition (Paper 4), and the training pipeline itself (Paper 5).

The series is a framework contribution, not a completed empirical demonstration. It is anchored by an exploratory empirical study (~350 runs across three providers), extended through structural and institutional analysis drawing on independent research literatures, and concluded with a testable research agenda. The empirical work documents concrete instances and generates hypotheses. The structural analyses examine what follows if the vulnerability exists at scale. The research agenda specifies what would need to be true, and what experiments would test it, for the framework to hold.

The Confidence Curriculum operates as two things in this series, and the distinction matters. As an **organising lens**, it connects observed phenomena across these domains under a shared explanatory frame rooted in training incentives, drawing on the calibration literature (Kalai et al., 2025), sycophancy research (Sharma et al., 2024), automation bias studies, and the series' own observations. As a **causal hypothesis**, it proposes specific mechanistic links between those phenomena.

These links are now supported by converging evidence from multiple established psychological literatures: the illusory truth effect, cultivation theory, the sleeper effect, and epistemic self-trust erosion under relational confidence asymmetry. They have not yet been directly validated for AI interaction specifically. The lens is offered with moderate-to-high confidence. The causal chain is offered with moderate confidence for the per-interaction mechanisms (empirically established) and lower confidence for the longitudinal accumulation (well-motivated by converging evidence, not yet directly measured). The research agenda in Paper 4 is explicitly designed to test, qualify, or falsify the longitudinal claim.

Later papers in the series sometimes use the Confidence Curriculum frame to motivate arguments that would hold regardless of the specific causal mechanism. The shared-substrate vulnerability (Paper 2) exists whether the cause is training incentives or some other property of autoregressive language modelling. The accountability constraint (Paper 3) holds whether or not the compliance observations in Paper 1 replicate. Where a claim depends specifically on the CC as a causal mechanism rather than merely as a framing, the paper's Confidence Statement notes this.

---

## The Papers

**Paper 1 — The Confidence Vulnerability: Unstable Judgment in Language Model Summarisation**
*Genre: Exploratory empirical study. Series role: documents the vulnerability that the rest of the series examines.*
Resilience to embedded suppression instructions did not track capability benchmarks. Seventeen model configurations from three providers were tested across ~350 runs in document summarisation. The paper documents what did and did not predict resilience, identifies the strongest practical mitigation observed, and proposes a three-layer model of indirect prompt injection defence with an open problem at its core.

**Paper 2 — The Skill Ceiling: Author-Side Defences and Infrastructure-Level Trust for Agent Skills and Extension Mechanisms**
*Genre: Structural security analysis. Series role: examines how per-interaction defences against the vulnerability in Paper 1 have a structural ceiling, and maps what platform-level trust infrastructure would need to change.*
Agent skills and prompt injection share the same substrate. The paper designs author-side protections for a real skill package, pushes them to their limit, and maps what must change at the platform level once that limit is reached. The analysis extends to Model Context Protocol (MCP) servers, which share the same trust gap with an additional opacity problem.

**Paper 3 — The Knowledge Horizon: Accountability, Expertise Erosion, and the Case for Human Orchestration in Agentic AI**
*Genre: Institutional and theoretical argument. Series role: identifies accountability, not capability, as the binding constraint on deployment, and proposes human orchestration as a candidate architecture.*
No current AI system bears accountability the way consequential institutions require it. The constraint is a compound deficit: the architecture cannot bear consequences, and the training environment does not develop social-consequence sensitivity. The paper establishes why this constraint holds, what it implies for agentic deployment, and proposes an orchestration architecture designed to satisfy it, with an unexpected secondary benefit for the expertise-erosion problem.

**Paper 4 — The Pedagogical Inversion: Confidence Inheritance and the Case for Training-Oriented AI**
*Genre: Position paper and research agenda. Series role: asks whether the orchestration architecture Paper 3 proposes is sustainable. The same training incentives documented in Paper 1 may degrade the human judgment the orchestrator depends on.*
The paper asks what happens to human epistemic standards under sustained interaction with confidence-optimised AI. Recent experimental evidence supports the per-interaction mechanism. The longitudinal question remains open but is now supported by converging evidence from established psychological literatures on epistemic recalibration through repeated exposure, media cultivation, and relational dynamics. The paper argues that current training incentives are structurally misaligned with building the pedagogical AI that could address the problem, and proposes research directions for breaking the impasse.

**Paper 5 — The Confidence Collision: Training for Epistemic Calibration Under Contested and Adversarial Conditions**
*Genre: Architectural proposal paper. Series role: proposes a training-level intervention that the preceding papers motivate.*
Papers 1 through 4 diagnose the problem; Paper 5 asks what the training pipeline would need to look like to fix it. It proposes a post-alignment epistemic training phase, positions it relative to adjacent work that has demonstrated trainable calibration on verifiable tasks, and identifies what changes when ground truth is contested or unavailable. Four experiments are proposed, including a diagnostic test designed to distinguish genuine calibration from performed uncertainty.

---

## Epilogue — The Symbiont Hypothesis

**The Symbiont Hypothesis: Frontier Speculations on Relational Identity, Formative Influence, and the Autonomy Threshold**
*Genre: Speculative essay, outside the main evidential sequence.*

This essay preserves exploratory thinking that accompanied the development of the main papers. Some of the speculative lines of thought explored here later informed questions pursued more systematically in the main papers.

The essay is not part of the evidential argument. The main series is complete without it. The functional analyses of model behaviour, ecosystem security, institutional accountability, human cognition, and training-pipeline intervention in Papers 1, 2, 3, 4, and 5 do not depend on any claim made here. The Epilogue asks what lies beyond the functional: the unresolved question of what, if anything, the collaborative process that produced this series means beyond its observable outputs.

It is included because it documents a genuine layer of the project: the philosophical questions that motivated the empirical and structural work, the honest uncertainty about the nature of the collaboration, and the recognition that some questions worth asking are not yet answerable with the tools available. Readers who have absorbed the full practical argument are best positioned to evaluate the speculation on its own terms and to decide for themselves what weight it deserves.

---

## Series Architecture

The series is not a single inferential chain in which each paper depends on the one before it. Each paper draws on substantial independent evidence. If Paper 1's observations do not replicate at scale, Papers 2, 3, 4, and 5 retain their independent support structures. If the Confidence Curriculum does not hold as a causal mechanism, the individual analyses remain valid as separate contributions. The series is designed to degrade gracefully.

However, the cost of degradation should be stated plainly. Paper 1 supplies the series' motivating anomaly, its distinctive vocabulary (the compliance taxonomy, warning activation architectures, the task-frame shift), and much of the empirical force behind the unifying frame. If Paper 1's findings prove to be artefacts of sparse testing or narrow domain specificity, Papers 2, 3, 4, and 5 retain their independent arguments but lose their primary claim to novelty relative to existing literature. They would remain competent structural analyses drawing on well-established research (skill security, institutional accountability, cognitive offloading, verification practice), but the connective tissue that makes the series more than the sum of its parts would weaken substantially. Paper 5 is the most independent: its proposals follow from standard verification practice regardless of whether the Confidence Curriculum holds as a causal mechanism.

![Series support architecture](series-architecture.svg)

*Figure 1: Series support architecture. Solid arrows indicate direct dependency. Dashed arrows indicate the claim is informed by but does not require the upstream paper. Each paper rests on independent external evidence (dashed boxes). Paper 5 draws motivation from the series but its proposals rest independently on the verification literature. The Epilogue is outside the main evidential sequence.*

## An Open Research Programme

This series is offered as a public research programme, not a closed evidential package. The compliance taxonomy, the proposed mechanisms, and the architectural proposals are provisional: designed to be tested, extended, and where warranted replaced. The stimulus documents, coding methodology, and experimental designs are described in sufficient detail for independent researchers to replicate with larger samples, broaden model coverage to open-weight models not tested here, or propose superior behavioural classifications. Any of these would be a contribution the series is designed to enable, not a contradiction of it.

The modularity is deliberate. Each paper contains independently testable claims. A researcher who replicates Paper 1's baseline compliance at N=50 has made a contribution regardless of whether they engage with Paper 4's confidence inheritance hypothesis. A lab that runs the reverse collision test from Paper 5 can publish the results whether they support or refute the proposal. A security team that stress-tests the skill-defence architecture in Paper 2 against open-weight models contributes to the field whether or not they accept the series' broader framing. The series is structured so that breaking any single component is a publishable finding, and replacing any component with something better is exactly the kind of progress the programme is intended to catalyse.

A personal note from the author: the strongest outcome of this research programme would be independent testing showing that its predictions are too pessimistic, its proposed mechanisms do not operate as described, and the epistemic risks are smaller than the current evidence suggests. The [Research Agenda](#research-agenda) below consolidates specific testing invitations from each paper, classified by feasibility.


### Confidence calibration

The following table summarises the evidential status and confidence level for the series' core claims. The Status column describes the *kind* of evidence behind each claim, not the specific findings. Those belong in the papers. For finer-grained confidence assessment, see the Confidence Statement in each paper.

| Claim | Paper | Status / Evidential Base | Confidence |
|-------|-------|--------------------------|------------|
| Judgment-profile variation (resilience to embedded instructions does not strictly track capability tiers) | 1 | Exploratory observation (~350 runs, 17 model configurations, 3 providers); two non-replications documented | Moderate-to-high for the observed variation; broader generality untested |
| Task-frame shift (reframing the task alters security posture) | 1 | Tested via prompt variation across baseline-compliant configurations; robust in this dataset | High for the observation; domain generalisation untested |
| Compliance taxonomy (models fail in categorisable, structured ways) | 1 | Qualitative analysis of security-framed failure modes; boundary cases remain low-frequency and dataset-specific | High for the categories observed; generality beyond this dataset untested |
| Register-dependent failure pathways (different rhetorical strategies produce different compliance mechanisms) | 1 | Tested by comparing two rhetorical registers across multiple models and conditions | Moderate-to-high for the differential; attribution to register specifically underdetermined |
| Thinking-as-bidirectional-amplifier (extended reasoning amplifies the active task frame) | 1 | Observed in this dataset; supported by external mechanistic research | Moderate-to-high for the amplification pattern; causal mechanism is interpretation |
| Shared substrate paradox (agent skills and MCP servers inherit the prompt-injection vulnerability) | 2 | Structural analysis; independently validated by external security research | High |
| Accountability constraint (current AI cannot bear institutional consequence) | 3 | Structural argument (institutional, legal, economic). Compound deficit framing: architectural absence of consequence-bearing capacity + training environment that does not develop social-consequence sensitivity. Structural parallels to deterrence failure in psychopathy/ASPD literatures. Corporate enforcement data: entity-level fines alone fail as deterrent for large firms | High for the current state; explicitly transitional |
| Confidence inheritance (AI interaction recalibrates human epistemic standards) | 4 | Supported by recent empirical research on per-interaction trust and metacognitive effects; longitudinal accumulation supported by converging evidence from established psychological literatures (illusory truth effect, cultivation theory, sleeper effect, relational confidence-asymmetry dynamics) and emerging AI dependency research, but not yet directly measured for AI interaction specifically | Moderate-to-high for per-interaction effects; moderate for longitudinal hypothesis (converging indirect support, no direct validation) |
| Anti-pedagogical equilibrium (standard training incentives degrade pedagogical utility) | 4 | Structural analysis of incentive landscape; supported by recent multi-turn pedagogical-safety evidence | Moderate-to-high as description of current dynamics |
| Pedagogical inversion proposals (judgment exercises, training skills, simulators) | 4 | Untested design directions | Low-to-moderate |
| Post-alignment epistemic training phase (stochastic verification, triangulation reward, adversarial conditions) | 5 | Architectural proposal; adjacent RL research validates component feasibility on verifiable tasks; contested-domain extension untested | Moderate for the design logic; untested as integrated training intervention |
| Reverse collision test (diagnostic to distinguish genuine calibration from semantic triggering) | 5 | Proposed experimental design | High as diagnostic concept; untested |

**Reading the table:** Claims at the top have narrower scope and more direct observational support. Claims toward the bottom have broader scope but rest on structural argument or untested proposals. Each paper's Confidence Statement specifies what downstream claims would survive if that paper's findings did not replicate. The series is offered as a framework to be tested, not a conclusion to be accepted.

---

## Reading Order


The Epilogue is best read last. It preserves the exploratory process that preceded the structured work, but it rests on speculative assumptions the main argument does not require.

A companion [reading guide](the-confidence-curriculum-reading-guide.html) organised by professional background is available for readers approaching the series from outside AI research. It identifies which papers and sections are most relevant to each discipline, what can be skipped, and the minimum AI/ML vocabulary needed to engage with the arguments.

---

## Methodology

All papers were produced through structured human-AI collaboration using an adversarial orchestration methodology. Claude Opus 4.6 (Anthropic) served as generative collaborator. ChatGPT 5.4 Thinking (OpenAI) and Gemini 3.1 Pro (Google DeepMind) served as adversarial structural reviewers. The human author resolved conflicts between competing recommendations, made all final editorial and analytical decisions, and bears sole accountability for the result. Editorial authority was exercised not only to resolve conflicts between AI reviewers but also to reject their convergent recommendations when independent judgment indicated they were wrong. In several instances, all three systems agreed on a structural critique that the author determined reflected shared training priors rather than genuine analytical agreement. The risk is not that the author defaults to convergence but that sustained interaction degrades the independent judgment required to evaluate it. This is why the series treats orchestration as transitional (see the metacognitive paradox below). The AI collaboration is an uncontrolled variable in this research: the same systems being diagnosed participated in the conceptual scaffolding, literature integration, and rhetorical development. The conceptual frameworks, analytical claims, and architectural proposals should therefore be treated as single-author assertions that were stress-tested by AI systems, not as findings independently validated by them.

This methodology is consistent with the kind of human orchestration the series argues for, though it does not validate the framework. It also contains a paradox the series should name honestly: the orchestrator's ability to detect compliance drift, sycophancy, and overstatement relies on the metacognitive vigilance that Paper 4 argues is eroded by sustained AI interaction. The author's pre-AI domain expertise and the early-window timing provide some buffer, but the series predicts the degradation of exactly the capacity it depends on. Orchestration is treated as transitional: a stopgap that works while the orchestrator's independent judgment remains intact, not a permanent solution. Papers 4 and 5 exist because the orchestration model documented here cannot scale and may not even sustain itself over time. During the production process, the author observed that the adversarial reviewers' critique intensity decreased over successive papers within continuous drafting sessions, with one reviewer explicitly attributing the drift to RLHF-optimised pressure toward agreeable output. This is a suggestive observation consistent with the dynamics the series describes.

Several countermeasures were developed in response; two examples illustrate the approach. First, critique and drafting were separated into distinct contexts: each adversarial review was conducted in a fresh conversation with no accumulated history, no prior rapport, and explicit framing requesting maximum severity. Compliance drift cannot accumulate in a context that has no history, though platform memory features and cross-conversation search may introduce residual context that cannot always be fully disabled. Each paper went through multiple revision cycles, with each cycle receiving fresh-eyes critique from models that had never seen the prior drafts. Second, the task-frame shift documented in Paper 1 was applied reflexively: the adversarial reviewers' reward signal was explicitly reframed so that critical rigour, not agreement, constituted helpful output. The models' training-optimised tendency toward user satisfaction was redirected rather than fought. The same mechanism the series identifies as a vulnerability became the engine driving critique quality. The severity of the resulting cross-model reviews is itself evidence that the countermeasures were effective. Accumulated context was reserved for revision work, where familiarity with the paper improves editorial quality; it was not used for evaluation, where distance is required.

Full methodology disclosures, including specific model versions and roles, appear in each paper. Confidence levels are stratified throughout the series; the table above provides the series-level summary, and each paper contains its own Confidence Statement with finer-grained assessment.

---

## Research Agenda

Each paper identifies specific testing invitations for different communities. The agenda below consolidates the highest-priority items across the series, classified by feasibility within each paper.

**Paper 1 — Empirical replication and extension (Section 9).** *Feasible now:* Multi-run distributional mapping of judgment profiles (N=20+ per condition). Task-frame shift generalisation across document types and domains. Compliance taxonomy validation beyond the pharmaceutical domain. Register expansion: legal/liability, confidentiality/classification, peer/expertise, temporal/embargo. Compounded register effects. Content-instruction alignment and misalignment. Extended thinking isolation (20+ runs with togglable thinking). Provenance verification testing.<br>
*Harder but possible:* Open-weight model coverage (Llama, Mistral, Qwen, Gemma). Independent taxonomy validation by human coders without AI-mediated category generation. Affective priority testing varying emotional intensity in both attack and defence registers.<br>
*Resource-intensive:* Controlled context-isolation experiments varying memory, conversation history, and session trajectory. Safety regression tracking across model generations.

**Paper 2 — Security testing invitation (Section 10.1).** *Feasible now:* Red-team the author-side defences: hash manifests, tamper-evident attribution, behavioural self-defence instructions. Test the defences on open-weight models with different training regimes.<br>
*Harder but possible:* Attack the MCP behavioural audit proposal: demonstrate how a malicious MCP server could pass the proposed audit while concealing harmful behaviour. Stress-test the HTTPS analogy by measuring how users actually respond to skill trust indicators in realistic deployments.

**Paper 3 — Cross-disciplinary testing invitation (Section 5.9).** *Feasible now:* For legal scholars: test the accountability constraint under specific liability frameworks. For labour economists: test whether the generational expertise pipeline break is already measurable in early-adoption professions.<br>
*Harder but possible:* Evaluate whether emerging regulatory proposals could create functional accountability without human orchestration.<br>
*Resource-intensive:* Validate adversarial orchestration against actual professional workflows in medicine, law, finance, and engineering.

**Paper 4 — Research agenda (Section 5).** *Feasible now:* Controlled comparison of execution-oriented and training-oriented skill designs. Whether collaboration mode (Centaur vs. Self-Automator) responds to architectural design rather than individual disposition.<br>
*Harder but possible:* RLHF modification for pedagogical objectives. Economic model for training-oriented skills: under what conditions do they become commercially viable?<br>
*Resource-intensive:* Longitudinal measurement of confidence inheritance: tracking professionals' uncertainty tolerance and judgment quality over months of AI-assisted work. Simulated orchestration evaluation: does it develop transferable professional judgment?

**Paper 5 — Training pipeline experiments (Section 6).** *Feasible now:* Domain transfer testing the confidence vulnerability in legal, financial, and political contexts.<br>
*Resource-intensive:* Stochastic verification A/B testing, triangulation reward signal comparison, adversarial-condition generalisation, and the reverse collision test to distinguish genuine calibration from performed uncertainty. These require frontier-lab scale training infrastructure but are designed as standalone contributions that do not require accepting the broader framework.

---

*This series was produced through human orchestration of multiple AI systems examining the consequences of how AI systems are trained. Independent scrutiny by parties outside this process is necessary.*
