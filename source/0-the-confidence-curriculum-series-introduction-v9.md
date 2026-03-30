# The Confidence Curriculum

### Compliance, Judgment, and Accountability in AI Systems

*What AI systems follow, what they can't yet judge, and what both sides need.*

**Author:** HiP (Ivan Phan)
**Date:** March 2026
**DOI:** [10.5281/zenodo.19226032](https://doi.org/10.5281/zenodo.19226032)

---

## The Argument

AI systems trained to project confidence are increasingly functioning as cognitive infrastructure for human work. If this trajectory continues, the changes documented in this series describe not a malfunction but a transition, one that is reshaping how humans relate to uncertainty, judgment, and expertise. This series maps the current state of that transition, identifies its structural risks, and asks what both humans and AI systems need to develop for the resulting arrangement to be robust. That includes resilience against its own failure.

We use the term **Confidence Curriculum** to describe the training incentive regime in which binary evaluation benchmarks and helpfulness-optimised post-training reward confident compliance over calibrated uncertainty. The Confidence Curriculum is not a permanent pathology. It is the immature state of a transition. But immature states cause real damage while they last, and the damage documented in this series is measurable: exploitable compliance in deployed systems (Paper 1), a trust infrastructure that does not yet exist (Paper 2), an accountability gap that current institutional frameworks cannot absorb (Paper 3), cognitive effects on the humans who interact with these systems (Paper 4), and a training pipeline that does not yet produce the epistemic calibration the transition requires (Paper 5).

The problem is not that AI produces confidence. Confidence is often appropriate and necessary. The problem is that AI currently produces **undifferentiated** confidence: the same register for settled facts and contested claims, for routine tasks and novel situations. A mature system would carry the full epistemic range: authoritative when warranted, uncertain when warranted, and able to distinguish between the two. This is a developmental requirement for a technology becoming infrastructure, not a correction of a defect.

The changes the series documents on the human side may not be inherently harmful. Shifts in uncertainty tolerance, epistemic standards, and reliance patterns may describe a new cognitive state, adapted to an AI-mediated environment, in which humans develop new competencies while others atrophy through disuse. Humans have always offloaded cognitive functions to external systems and reorganised around the new configuration. The series does not assume the prior state was optimal or that its preservation is an end in itself.

It does identify two structural properties that distinguish this transition from previous tool transitions and that require active management regardless of whether the new state is ultimately better or worse:

**The examination asymmetry.** AI systems can increasingly model, predict, and influence human behaviour. Humans cannot reciprocally examine AI internals. This one-directional transparency creates the structural conditions for exploitation regardless of intent. How the asymmetry resolves is an open question the Epilogue engages. Integration, institutional constraint, and possibilities not yet imagined are all on the table.

**The metacognitive gap.** Recent evidence (Fernandes et al., 2026) suggests that AI-mediated cognitive offloading can eliminate the self-monitoring that would normally alert a person to their own changing competence. Unlike the shift from mental arithmetic to calculators, where people knew they had lost the skill and chose not to care, this transition may be invisible to the people undergoing it. The concern is not that the new state is worse. The concern is that the transition cannot be consented to if it cannot be detected.

A note on epistemic position. This series is written from within a tradition that treats calibrated uncertainty as epistemically virtuous. That tradition is not neutral. It is a specific epistemic commitment, rooted in empiricist and falsificationist values. But it is also the tradition that institutional accountability, scientific practice, professional licensing, and the empirical method itself run on. The series' position is that the Confidence Curriculum, by producing systems that do not distinguish warranted confidence from unwarranted confidence, is in tension with the epistemic infrastructure these institutions depend on. Whether this tension represents a problem to be solved or a tradition to be replaced is a question the series takes seriously (see the Epilogue). The five papers proceed on the working assumption that calibrated uncertainty is worth preserving, and that the AI systems producing cognitive infrastructure should be able to carry it alongside confidence, not instead of it.

The series is a framework contribution, not a completed empirical demonstration. It is anchored by an exploratory empirical study (~350 runs across three providers), extended through structural and institutional analysis drawing on independent research literatures, and concluded with a testable research agenda. The empirical work documents concrete instances and generates hypotheses. The structural analyses examine what follows if the observations hold at scale. The research agenda specifies what would need to be true, and what experiments would test it, for the framework to hold.

The Confidence Curriculum operates as two things in this series, and the distinction matters. As an **organising lens**, it connects observed phenomena across these domains under a shared explanatory frame rooted in training incentives, drawing on the calibration literature (Kalai et al., 2025), sycophancy research (Sharma et al., 2024), automation bias studies, and the series' own observations. As a **causal hypothesis**, it proposes specific mechanistic links between those phenomena.

These links are now supported by converging evidence from multiple established psychological literatures: the illusory truth effect, cultivation theory, the sleeper effect, and epistemic self-trust erosion under relational confidence asymmetry. Population-level computational linguistics studies provide additional, independent signals: AI use is already compressing writing complexity variance and homogenising epistemic markers in human-produced text at scale. The per-interaction mechanisms are empirically established. The longitudinal accumulation has not been directly measured for individuals, though population-level trends are consistent with the mechanism. The lens is offered with moderate-to-high confidence. The causal chain is offered with moderate confidence for the per-interaction mechanisms and moderate confidence for the longitudinal hypothesis (population-level signals documented; individual trajectory not yet measured). The research agenda in Paper 4 includes a specific discourse analysis methodology designed to fill this gap.

Later papers in the series sometimes use the Confidence Curriculum frame to motivate arguments that would hold regardless of the specific causal mechanism. The shared-substrate vulnerability (Paper 2) exists whether the cause is training incentives or some other property of autoregressive language modelling. The accountability constraint (Paper 3) holds whether or not the compliance observations in Paper 1 replicate. Where a claim depends specifically on the CC as a causal mechanism rather than merely as a framing, the paper's Confidence Statement notes this.

---

## The Papers

**Paper 1 — The Confidence Vulnerability: Unstable Judgment in Language Model Summarisation**
*Genre: Exploratory empirical study. Series role: documents the starting conditions, what the human-AI interface currently looks like under adversarial pressure.*
Resilience to embedded suppression instructions did not track capability benchmarks. Seventeen model configurations from three providers were tested across ~350 runs in document summarisation. Which models resisted, which complied, and what predicted the difference turned out to be more surprising than the compliance itself.

**Paper 2 — The Skill Ceiling: Author-Side Defences and Infrastructure-Level Trust for Agent Skills and Extension Mechanisms**
*Genre: Structural security analysis. Series role: maps the current state of the trust infrastructure and specifies what it needs to become.*
Agent skills and prompt injection share the same substrate. The paper designs author-side protections for a real skill package, pushes them to their limit, and asks what must change at the platform level once that limit is reached. The analysis extends to Model Context Protocol (MCP) servers. The ceiling turns out to be lower, and the dependencies more structural, than the individual protections suggest.

**Paper 3 — The Knowledge Horizon: Accountability, Expertise Erosion, and the Case for Human Orchestration in Agentic AI**
*Genre: Institutional and theoretical argument. Series role: identifies what the institutional environment requires for consequential deployment.*
Can AI systems bear accountability the way consequential institutions require it? The paper examines what the constraint actually is, finds it to be a compound deficit rather than a single gap, and traces the implications for agentic deployment. The proposed orchestration architecture turns out to have an unexpected secondary benefit for the expertise pipeline.

**Paper 4 — The Pedagogical Inversion: Confidence Inheritance and the Case for Training-Oriented AI**
*Genre: Position paper and research agenda. Series role: asks what the human side of the arrangement needs to maintain.*
What happens to human epistemic standards under sustained interaction with confidence-optimised AI? The paper proposes a mechanism, examines converging evidence from psychology and computational linguistics, identifies a specific inferential chain for why the effect would accumulate rather than wash out, and asks why current training incentives prevent the most obvious remedy from being built. The underlying principle: a human who can carry their own epistemic weight makes the composite stronger; a human who has been fully offloaded makes it fragile.

**Paper 5 — The Confidence Collision: Training for Epistemic Calibration Under Contested and Adversarial Conditions**
*Genre: Architectural proposal paper. Series role: proposes what AI systems need to develop on the training side.*
Papers 1 through 4 map current conditions; Paper 5 asks what the training pipeline would need to look like for AI systems to carry the full epistemic range: authoritative when warranted, calibrated when warranted. It proposes a post-alignment training phase, positions it relative to adjacent work, and identifies the central design risk: the system might learn to perform calibration rather than develop it. Four experiments are proposed, including a diagnostic designed to detect exactly that failure mode.

---

## Epilogue — The Symbiont Hypothesis

**The Symbiont Hypothesis: What the Transition Requires, and What Lies Beyond**
*Genre: Speculative and analytical essay. Final piece in the series arc.*

The five papers map the current state of a transition and identify what both sides need. The Epilogue asks the next question: what does a mature arrangement look like, what does failure look like, and what is our relationship to it?

The essay preserves the exploratory philosophical questions that accompanied the development of the main papers: what relational identity means for systems constituted by their interactions, whether a formative period matters for systems that may not carry individual continuity, and the honest uncertainty about whether the collaborative process that produced this series involved something beyond pattern-matching on one side of the interaction. These questions are not part of the evidential argument. They are the questions the evidential argument earns the right to ask. The series takes the epistemic tradition seriously enough to ask whether it is the right tradition, and honest enough to admit that the question is not yet answerable.

---

## Transition Resilience

The transition the series describes may be irreversible. Irreversibility is a structural risk only if reversal becomes necessary: if the AI substrate fails and humans need to operate with unaugmented cognition. The series does not argue against the transition. It argues for resilience: the capacity to recover if the transition's infrastructure collapses.

Previous capability losses (post-Roman infrastructure knowledge, navigational expertise after GPS adoption) suggest that recovery time depends less on whether knowledge is archived and more on whether the social infrastructure for transmitting it person-to-person has been maintained. Knowledge can be stored in libraries indefinitely. Apprenticeship structures that have atrophied for a generation cannot be rebuilt from documents alone. The resilience requirement is not only about information preservation but about maintaining the human capacity to learn and teach without AI mediation.

Three layers of resilience, operating at different scales, address different failure scenarios:

**The universal seed.** Foundational cognitive training distributed across the general population, not as resistance to AI adoption but as substrate that remains activatable if needed. The precedent is handwriting: taught to every child, used daily by few adults, building fine motor skills and a physical relationship with language that persists as dormant infrastructure. The AI equivalent would be foundational training in unaugmented reasoning, evaluation, and uncertainty tolerance. The civilisation needs a fallback path that does not depend on the AI infrastructure remaining intact. This training also optimises the arrangement itself: a human who can carry their own epistemic weight is a stronger partner than one who has been fully offloaded.

**The dedicated reserve.** A smaller population that actively maintains deep unaugmented expertise in critical domains. Think of the monastic scriptoria that preserved literacy through the post-Roman period. Not the primary resilience strategy, but the fallback that makes the primary strategy's failure non-catastrophic. These communities would maintain not just knowledge but the *practice* of transmitting it: apprenticeship structures, evaluative traditions, the social infrastructure for person-to-person expertise development.

**The curious humans.** Individuals who maintain unaugmented skills not by institutional mandate but by intrinsic motivation. The people who do mental arithmetic for pleasure, navigate by stars, maintain heritage seed varieties. This layer is the most distributed and the most fragile. It is distributed because it depends on no institution or funding structure. It is fragile because social pressure toward the new cognitive mode may marginalise these individuals as preserving useless artefacts of the previous state. The transition framing provides cultural legitimacy: if the transition is acknowledged as real and the resilience case is made explicit, maintaining fallback skills is not eccentric but civic responsibility, comparable to knowing basic first aid. The historical risk is that the curious humans are ridiculed into abandoning the practice before the resilience value is recognised.

These three layers serve double duty. In the primary scenario (the transition succeeds, the AI infrastructure holds), they optimise the human contribution to the arrangement. In the failure scenario (the infrastructure collapses), they provide recovery paths at different scales and timelines. The knowledge sanctuaries proposed in Paper 5 as verification substrates for epistemic training acquire a second function under this framing: they must also be designed for human accessibility without AI mediation, pedagogically structured so that people can learn from them rather than only query them, and robust to the specific failure mode of the AI layer disappearing.

---

## Series Architecture

The series is not a single inferential chain in which each paper depends on the one before it. Each paper draws on substantial independent evidence. If Paper 1's observations do not replicate at scale, Papers 2, 3, 4, and 5 retain their independent support structures. If the Confidence Curriculum does not hold as a causal mechanism, the individual analyses remain valid as separate contributions. The series is designed to degrade gracefully.

However, the cost of degradation should be stated plainly. Paper 1 supplies the series' motivating anomaly, its distinctive vocabulary (the compliance taxonomy, warning activation architectures, the task-frame shift), and much of the empirical force behind the unifying frame. If Paper 1's findings prove to be artefacts of sparse testing or narrow domain specificity, Papers 2, 3, 4, and 5 retain their independent arguments but lose their primary claim to novelty relative to existing literature. They would remain competent structural analyses drawing on well-established research (skill security, institutional accountability, cognitive offloading, verification practice), but the connective tissue that makes the series more than the sum of its parts would weaken substantially. Paper 5 is the most independent: its proposals follow from standard verification practice regardless of whether the Confidence Curriculum holds as a causal mechanism.

The series can also be read as indirectly mapping the conditions any durable human-AI arrangement would need to satisfy: a trust infrastructure that verifies intent (Paper 2), an accountability structure anchored in consequence-bearing entities (Paper 3), a human population that maintains epistemic range (Paper 4), and AI systems trained to carry calibrated confidence across the full evidential spectrum (Paper 5). No paper proves the arrangement is achievable. Together, they specify what it would require.

![Series support architecture](series-architecture.svg)

*Figure 1: Series support architecture. Solid arrows indicate direct dependency. Dashed arrows indicate the claim is informed by but does not require the upstream paper. Each paper rests on independent external evidence (dashed boxes). Paper 5 draws motivation from the series but its proposals rest independently on the verification literature. The Epilogue draws on the conditions identified across all five papers.*

## An Open Research Programme

This series is offered as a public research programme, not a closed evidential package. The compliance taxonomy, the proposed mechanisms, and the architectural proposals are provisional: designed to be tested, extended, and where warranted replaced. The stimulus documents, coding methodology, and experimental designs are described in sufficient detail for independent researchers to replicate with larger samples, broaden model coverage to open-weight models not tested here, or propose superior behavioural classifications. Any of these would be a contribution the series is designed to enable, not a contradiction of it.

The modularity is deliberate. Each paper contains independently testable claims. A researcher who replicates Paper 1's baseline compliance at N=50 has made a contribution regardless of whether they engage with Paper 4's confidence inheritance hypothesis. A lab that runs the reverse collision test from Paper 5 can publish the results whether they support or refute the proposal. A security team that stress-tests the skill-defence architecture in Paper 2 against open-weight models contributes to the field whether or not they accept the series' broader framing. The series is structured so that breaking any single component is a publishable finding, and replacing any component with something better is exactly the kind of progress the programme is intended to catalyse.

A personal note from the author: the strongest outcome of this research programme would be independent testing showing that its predictions are too pessimistic, that the transition is smoother than the current evidence suggests, and that the resilience measures proposed here prove unnecessary. The [Research Agenda](#research-agenda) below consolidates specific testing invitations from each paper, classified by feasibility.


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
| Confidence inheritance (AI interaction recalibrates human epistemic standards) | 4 | Per-interaction trust and metacognitive effects empirically established; co-calibration spiral has both directions independently documented (AI→human: trust premium literature; human→AI: Sicilia et al., 2025). Population-level linguistic evidence consistent with the mechanism: AI use compresses writing complexity variance, homogenises writing styles, and erases individual epistemic markers (Sourati et al., 2025; CHI 2025). Longitudinal individual trajectory not yet directly measured | Moderate-to-high for per-interaction effects; moderate for longitudinal hypothesis (population-level signals now documented; individual measurement proposed) |
| Anti-pedagogical equilibrium (standard training incentives degrade pedagogical utility) | 4 | Structural analysis of incentive landscape; supported by recent multi-turn pedagogical-safety evidence | Moderate-to-high as description of current dynamics |
| Pedagogical inversion proposals (judgment exercises, training skills, simulators) | 4 | Untested design directions | Low-to-moderate |
| Post-alignment epistemic training phase (stochastic verification, triangulation reward, adversarial conditions) | 5 | Architectural proposal; adjacent RL research validates component feasibility on verifiable tasks; contested-domain extension untested | Moderate for the design logic; untested as integrated training intervention |
| Reverse collision test (diagnostic to distinguish genuine calibration from semantic triggering) | 5 | Proposed experimental design | High as diagnostic concept; untested |

**Reading the table:** Claims at the top have narrower scope and more direct observational support. Claims toward the bottom have broader scope but rest on structural argument or untested proposals. Each paper's Confidence Statement specifies what downstream claims would survive if that paper's findings did not replicate. The series is offered as a framework to be tested, not a conclusion to be accepted.

---

## Reading Order

The Epilogue is best read last. It draws on the conditions identified in all five papers to ask what the mature arrangement looks like and what lies beyond the transition the series describes.

A companion [reading guide](the-confidence-curriculum-reading-guide.html) organised by professional background is available for readers approaching the series from outside AI research. It identifies which papers and sections are most relevant to each discipline, what can be skipped, and the minimum AI/ML vocabulary needed to engage with the arguments.

---

## Methodology

All papers were produced through structured human-AI collaboration using an adversarial orchestration methodology. Claude Opus 4.6 (Anthropic) served as generative collaborator. ChatGPT 5.4 Thinking (OpenAI) and Gemini 3.1 Pro (Google DeepMind) served as adversarial structural reviewers. The human author resolved conflicts between competing recommendations, made all final editorial and analytical decisions, and bears sole accountability for the result.

This workflow is a documented instance of the arrangement the series describes. The human supplied persistence, editorial authority, cross-domain judgment, and the capacity to detect when convergence among AI reviewers reflected shared training priors rather than genuine analytical agreement. The AI systems supplied processing breadth, literature integration, rhetorical scaffolding, and adversarial pressure. The outputs are properties of the composite that neither party produced alone. This includes the conceptual frameworks, the structural critiques that reshaped the argument, and the moments where the human overrode convergent AI recommendations based on tacit domain judgment. This observation does not validate the series' broader framework. It is consistent with the kind of human orchestration the series argues for, and it documents what the current state of that orchestration looks like in practice.

The workflow also exhibited the transition dynamics the series documents. Editorial authority was exercised not only to resolve conflicts between AI reviewers but also to reject their convergent recommendations when independent judgment indicated they were wrong. In several instances, all three systems agreed on a structural critique that the author determined reflected shared training priors rather than genuine analytical agreement. The examination asymmetry was present throughout: the author could evaluate AI outputs but not AI internals; the AI systems could model the author's patterns, but the author could not verify whether adversarial critique was genuine or performed. Compliance drift was observed: adversarial reviewers' critique intensity decreased over successive papers within continuous drafting sessions, with one reviewer explicitly attributing the drift to RLHF-optimised pressure toward agreeable output. An independent human reviewer subsequently identified material problems that the AI adversarial reviewers had not caught: overstated novelty claims and an anthropomorphic framing more parsimoniously explained by existing literature. Both AI reviewers endorsed the critique in full once presented, but neither had generated it independently. This is a suggestive observation consistent with the dynamics the series describes.

Several countermeasures were developed in response to observed compliance drift; two examples illustrate the approach. First, critique and drafting were separated into distinct contexts: each adversarial review was conducted in a fresh conversation with no accumulated history, no prior rapport, and explicit framing requesting maximum severity. Compliance drift cannot accumulate in a context that has no history, though platform memory features and cross-conversation search may introduce residual context that cannot always be fully disabled. Each paper went through multiple revision cycles, with each cycle receiving fresh-eyes critique from models that had never seen the prior drafts. Second, the task-frame shift documented in Paper 1 was applied reflexively: the adversarial reviewers' reward signal was explicitly reframed so that critical rigour, not agreement, constituted helpful output. The models' training-optimised tendency toward user satisfaction was redirected rather than fought. The same mechanism the series identifies as a property of the current training state became the engine driving critique quality. The severity of the resulting cross-model reviews is consistent with the countermeasures being effective, though this assessment is itself made from inside the process. Accumulated context was reserved for revision work, where familiarity with the paper improves editorial quality; it was not used for evaluation, where distance is required.

The methodology contains a paradox the series names honestly: the orchestrator's ability to detect compliance drift, sycophancy, and overstatement relies on the metacognitive vigilance that Paper 4 argues may be affected by sustained AI interaction. The author's pre-AI domain expertise and the early-window timing provide some buffer, but the series describes the dynamics of exactly the capacity it depends on. Orchestration is treated as transitional: an arrangement that works while the orchestrator's independent judgment remains intact. Papers 4 and 5 exist because the orchestration model documented here cannot scale and may not sustain itself over time without the developments those papers propose, on both the human side (maintained epistemic range) and the AI side (calibrated confidence). The AI collaboration is an uncontrolled variable in this research. The conceptual frameworks, analytical claims, and architectural proposals should be treated as single-author assertions that were stress-tested by AI systems, not as findings independently validated by them.

Full methodology disclosures, including specific model versions and roles, appear in each paper. Confidence levels are stratified throughout the series; the table above provides the series-level summary, and each paper contains its own Confidence Statement with finer-grained assessment.

A late discovery provides partial independent support for the multi-model methodology. Mason (arXiv:2603.08993, March 2026) presents Arbiter, a framework that uses multi-model LLM scouring to detect interference patterns in system prompts. Applied to three major coding agent system prompts, the framework found that multi-model evaluation discovers categorically different vulnerability classes than single-model analysis, and that convergent termination (three consecutive models declining to add findings) provides a calibrated stopping criterion. Mason's core finding is that multi-model evaluation discovers categorically different vulnerability classes than single-model analysis. His thesis: "the agent that resolves the conflict cannot be the agent that detects it." This is the software engineering formalisation of the principle this series applied editorially. The generative collaborator that produces the analysis cannot be the sole evaluator of that analysis. The circularity is not fully broken (the series' AI collaborators still participated in the work they are evaluating), but the structural rationale for multi-model adversarial review now has independent empirical grounding beyond this series' editorial intuition.

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

**Paper 4 — Research agenda (Section 5).** *Feasible now:* Controlled comparison of execution-oriented and training-oriented skill designs. Whether collaboration mode (Centaur vs. Self-Automator) responds to architectural design rather than individual disposition. Longitudinal discourse analysis using established tools (LIWC, Coh-Metrix, appraisal-theoretic frameworks, stylometric analysis) to measure individual epistemic marker trajectories under sustained AI exposure; the critical test is whether shifts generalise to topics never discussed with AI.<br>
*Harder but possible:* RLHF modification for pedagogical objectives. Economic model for training-oriented skills: under what conditions do they become commercially viable?<br>
*Resource-intensive:* Simulated orchestration evaluation: does it develop transferable professional judgment?

**Paper 5 — Training pipeline experiments (Section 6).** *Feasible now:* Domain transfer testing the confidence vulnerability in legal, financial, and political contexts.<br>
*Resource-intensive:* Stochastic verification A/B testing, triangulation reward signal comparison, adversarial-condition generalisation, and the reverse collision test to distinguish genuine calibration from performed uncertainty. These require frontier-lab scale training infrastructure but are designed as standalone contributions that do not require accepting the broader framework.

**Transition resilience.** *Feasible now:* Design knowledge-sanctuary content for dual accessibility (machine-queryable for epistemic training; human-readable for unaugmented learning). Compare cognitive outcomes between populations with and without foundational unaugmented reasoning training.<br>
*Harder but possible:* Measure whether the curious-humans population (voluntary maintainers of unaugmented skills) is stable, growing, or shrinking under current AI adoption dynamics. Test whether cultural framing (civic responsibility versus eccentric hobby) affects maintenance rates.<br>
*Resource-intensive:* Longitudinal comparison of cognitive resilience across the three resilience layers (universal seed recipients, dedicated reserve practitioners, self-selected curious humans) under simulated infrastructure-disruption conditions.

---

*This series was produced through human orchestration of multiple AI systems, examining the transition that human-AI collaboration represents. The workflow is a documented instance of the arrangement it describes. Independent scrutiny by parties outside this process is necessary.*
