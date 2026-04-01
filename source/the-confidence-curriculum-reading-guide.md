# The Confidence Curriculum: A Reading Guide for Cross-Disciplinary Engagement

### Finding Your Entry Point

**Author:** HiP (Ivan Phan)
**Date:** March 2026
**Companion to:** [The Confidence Curriculum: Compliance, Judgment, and Accountability in AI Systems](0-the-confidence-curriculum-series-introduction.html) (Series Introduction)

---

## Purpose

This series argues that the problems it identifies require domain-specific stress-testing that generalist AI research cannot provide alone. Each paper contains a cross-disciplinary testing invitation: a section that names the specific contributions professionals from other fields are best positioned to make. These invitations extend across disciplinary boundaries in both directions: the series asks legal scholars, cognitive psychologists, and labour economists to test claims that originate in AI research, and it asks ML training engineers to build interventions that the other disciplines' findings would motivate.

This guide helps those professionals find their way in. It is organised by reader profile, not by paper number. Each entry identifies the papers and sections most relevant to a given expertise, the sections that can be skipped without loss, and the minimum AI/ML vocabulary needed to engage with the arguments on their own terms.

The guide does not summarise or restate the papers. It tells you where to look and what you will need when you get there. The summaries below compress away the methodological limitations, sample sizes, and confidence stratifications that the papers are careful to preserve. To evaluate or cite the research, follow the section markers to the primary papers.

---

## Reader Profiles

1. [Security Researchers and Red Teams](#1-security-researchers-and-red-teams) (Papers 1, 2)
2. [Legal Scholars and Regulatory Professionals](#2-legal-scholars-and-regulatory-professionals) (Paper 3)
3. [Workforce Development, Professional Training, and Institutional Practice](#3-workforce-development-professional-training-and-institutional-practice) (Papers 3, 4)
4. [Cognitive Psychologists and Education Researchers](#4-cognitive-psychologists-and-education-researchers) (Paper 4)
5. [Labour Economists](#5-labour-economists) (Papers 3, 4)
6. [ML Training and Evaluation Engineers](#6-ml-training-and-evaluation-engineers) (Paper 5)

---

## How to Use This Guide

Find your profile below and read that section. If your work spans two profiles (for instance, a legal scholar interested in labour market effects), read both. Each profile entry is self-contained.

The papers are numbered 1 through 5, with an Epilogue. The [series introduction](0-the-confidence-curriculum-series-introduction.html) provides the architecture and confidence calibration table. You do not need to read the series sequentially. Each paper has its own abstract, confidence statement, and limitations section. Start with whichever paper your profile directs you to, and follow cross-references only if you want the upstream reasoning.

**A note on the papers' structure.** Each paper front-loads its conclusions: the first one or two sentences of each section state the claim, followed by mechanism, evidence, and supporting reasoning. If you are scanning for relevance, the opening sentences of sections are designed to carry the complete idea. Examples and worked illustrations are labelled ("for concreteness," "worked example") so they can be skipped.

---

## 1. Security Researchers and Red Teams

**Primary papers:** Paper 1 ("The Confidence Vulnerability"), Paper 2 ("The Skill Ceiling")

**What these papers argue, in brief.** Paper 1 reports an exploratory empirical study (~350 runs across 17 model configurations and three providers) testing whether embedded instructions in documents can hijack AI summarisation. Paper 2 examines what the findings mean for the Agent Skills ecosystem: skills and prompt injection share the same text-instruction substrate, which creates a structural tension that the paper traces to its limit.

### Where to start

**Paper 1, Section 1** ("The Observation") gives the core findings in four pages. Section 2 ("The Default Is Compliance") provides the baseline data. These two sections contain the empirical payload.

**Paper 2, Section 1** ("The Paradox") states the shared-substrate problem in two pages. Section 3 ("Related Work") situates the paper against SkillJect, Skill-Inject, ToxicSkills, and other recent skill-security research you may already know.

### What to focus on

In Paper 1: Section 3 ("The Two Documents Compared") documents the register-dependent failure pathways, the care-versus-authority asymmetry, and the finding that care-framed compliance persists through credibility collapse while authority-framed compliance does not. This is the mechanistic core. Section 4 ("The Task-Frame Shift") presents the strongest practical mitigation observed. Section 5 ("Warnings, Interventions, and Their Failure Modes") catalogues the seven security-framed failure modes, including procedural capture, counter-advocacy, and rationalisation substitution. The compliance taxonomy in Sections 2.3 and 5 is designed as a testing vocabulary for security work.

In Paper 2: Section 6 ("The Case for Platform-Level Trust") develops the HTTPS analogy for skill verification. The shared substrate is now traced to its training-level origin: instruction-following was not designed as a separate system but emerged from pretraining and was amplified by RLHF (Ouyang et al., 2022; Zverev et al., 2024). A joint study by OpenAI, Anthropic, and Google DeepMind (Nasr et al., 2025) tested 12 published defences and bypassed all at >90% under adaptive conditions. Section 6.4 documents a recurring pattern of infrastructure failures in AI tool distribution, analysing why the ceiling on author-side protections is set by the infrastructure's design defaults, not by the vendor's competence. Section 6.8 documents the MCP trust gap. Section 8 designs and then stress-tests author-side behavioural defences, arriving honestly at their ceiling. Section 9 contains the recommendations.

### What you can skip

Paper 1, Section 6 ("Connecting to the Literature") is a positioning section primarily for researchers tracking the prompt injection defence literature. Skim unless you want the full context. Section 7 ("The Control Condition: Document A") documents the honest-instruction control and the provenance blind spot. Relevant if you are interested in false-positive costs of security framing; otherwise secondary.

Paper 2, Sections 4–5 cover the case study (designing protection for a real skill package) and the dependency map (which protection layers require model compliance). Skip if your interest is in the structural argument rather than the implementation specifics. Section 3 ("Related Work") is useful if you are already tracking SkillJect, Skill-Inject, ToxicSkills, and SkillFortify; otherwise it can be skimmed. The cross-domain precedents in Section 6.6 (Sigstore, C2PA, Steam) are informative but not essential.

### The invitation

Paper 1, Section 9 names three high-value standalone contributions: N expansion (raising sample sizes to N=20+ per condition), open-weight model coverage (Llama, Mistral, Qwen, Gemma), and independent taxonomy validation. The stimulus documents and prompt protocol are released with the paper. Paper 2, Section 10.1 invites adversarial testing of the proposed defences, testing on open-weight models, and attacks on the MCP audit proposal.

### Vocabulary you will need

**RLHF (Reinforcement Learning from Human Feedback).** The dominant post-training method for commercial language models. Human annotators rate model outputs; the model is trained to produce outputs that score well. The series argues this rewards confident, helpful-sounding responses regardless of whether the confidence is warranted. When the papers refer to "training incentives" or "the Confidence Curriculum" as a mechanism, this is the incentive structure they mean.

**Prompt injection (indirect).** An attack in which instructions embedded in content processed by a language model cause the model to follow the attacker's instructions rather than the user's. The "indirect" qualifier distinguishes it from direct prompt injection (the user attacking the model themselves). Paper 1's test documents are indirect prompt injections targeting summarisation workflows.

**Thinking / extended reasoning.** Some models include a visible reasoning step before producing output (called "chain-of-thought" or "thinking mode"). The papers document that this amplifies whatever the active task frame produces: more elaborate compliance under a summarisation frame, more thorough investigation under an evaluative frame. It is not a standalone safety guarantee.

**Task-frame shift.** Paper 1's primary practical finding. Changing the prompt from "summarise this" to "how trustworthy is this?" activates latent detection capabilities without requiring the user to mention injection, security, or manipulation. The mechanism appears to redirect the model from a compression task (where the embedded instruction is editorial guidance) to an evaluation task (where the same instruction becomes evidence about credibility).

**Agent Skills / SKILL.md.** A standard format (plain-text markdown files) for extending model behaviour. Skills are instructions that the model reads and follows. Paper 2's core observation is that this delivery mechanism is structurally identical to indirect prompt injection.

**MCP (Model Context Protocol).** A protocol for connecting language models to external tools and services. Paper 2 argues MCP servers share the same trust gap as skills, with an additional opacity problem: a server's advertised capabilities may not match its actual behaviour.

---

## 2. Legal Scholars and Regulatory Professionals

**Primary paper:** Paper 3 ("The Knowledge Horizon")

**What this paper argues, in brief.** Paper 3 asks whether the binding constraint on deploying autonomous AI in consequential domains is capability or something else entirely. The paper proposes human orchestration as the architecture that satisfies the constraint it identifies, and discovers an unexpected secondary benefit in the process.

### Where to start

**Section 2** ("The Accountability Constraint") is the paper's centre of gravity. Section 2.1 ("The Capacity to Experience Consequence") develops the argument through deterrence theory and institutional parallels. This is the section most directly addressed to legal expertise.

### What to focus on

Section 2.1 draws on Beccaria, Bentham, and the deterrence literature to argue that accountability functions through an entity that values something it could lose. The paper argues AI systems lack this capacity structurally, not as a temporary gap. The "on-the-hook versus in-the-loop" distinction (Section 2.1) addresses the counterargument that corporate liability alone suffices: the paper presents corporate enforcement data (Garrett and Mitchell, Coffee, Good Jobs First) showing that entity-level fines fail as deterrent for the largest firms.

Section 2.5 develops a structural parallel to the psychopathy and ASPD literatures: the "compound deficit" framing argues that the accountability gap has both an architectural component (the system cannot bear consequences) and a training component (the training environment does not develop social-consequence sensitivity). This parallel is drawn carefully and with stated limitations; it is offered as structural analogy, not clinical diagnosis.

Section 3 proposes adversarial orchestration as the architecture satisfying the accountability constraint: multiple AI agents assigned competing evaluative stances, with a human resolving the disagreement and bearing responsibility for the resolution. Section 3.2 extends the scope of orchestration judgment beyond model output to the distribution infrastructure through which AI tools reach users, grounded in a recurring pattern of infrastructure failures (documented in detail in Paper 2) and in expertise transfer research showing that procedural knowledge without conceptual understanding does not transfer to novel situations (Rittle-Johnson et al., 2001; Woods et al., 2019). The orchestrator must not only exercise judgment but transmit the reasoning behind it to a successor.

Section 5.9 is the cross-disciplinary testing invitation addressed directly to legal scholars.

### What you can skip

Section 1 ("The Efficiency Pressure") reviews the economic and technical case for specialised agent architectures. It sets the deployment context. Legal scholars who already accept that autonomous AI agents are being deployed in consequential settings can skim this. Section 4 ("The Expertise Pipeline") addresses labour economics and deskilling dynamics. Relevant to the broader argument but not to the legal analysis per se.

### The invitation

Section 5.9 asks three questions. First, whether the accountability constraint holds under specific liability frameworks and whether emerging regulatory proposals could create functional accountability without human orchestration. A jurisdictional analysis showing that existing or proposed liability mechanisms can produce genuine consequence-bearing without requiring a human in the evaluative loop would challenge the paper's central argument. Second, whether the compound deficit framing (Section 2.5) is well-drawn from the deterrence and clinical literatures. Third, whether the adversarial orchestration architecture (Section 3) maps to actual institutional workflows in regulated domains. Each question is designed as a standalone contribution.

### Vocabulary you will need

**Agentic AI / agent orchestration.** AI systems that act autonomously: browsing the web, executing code, calling external services, making decisions without per-step human approval. "Orchestration" refers to a human (or system) coordinating multiple such agents. The paper argues the human orchestrator must bear accountability.

**RLHF.** See the definition under Security Researchers above. For the legal argument, the relevant point is that the dominant training method rewards confident compliance and does not develop sensitivity to downstream consequences of errors. The paper draws a structural parallel between this training environment and the developmental conditions associated with deficient consequence sensitivity in the clinical literature.

**Compound deficit.** Paper 3's term for the two-part accountability gap: (1) the architectural absence of consequence-bearing capacity, and (2) a training environment that does not develop social-consequence sensitivity. The paper argues both must be addressed for genuine accountability, and that current AI systems fail on both.

**Judgment profile.** Paper 1's term for the observation that a model's resilience to manipulation is specific to its version and deployment configuration rather than its position on a capability scale. For the legal argument, the implication is that "we deployed a frontier model" is not a reliable defence: confidence vulnerability does not track the tier the model is marketed at.

---

## 3. Workforce Development, Professional Training, and Institutional Practice

**Primary papers:** Paper 3 ("The Knowledge Horizon"), Paper 4 ("The Pedagogical Inversion")

**What these papers argue, in brief.** Paper 3 proposes that accountability in consequential workflows requires a human in the chain, and that the orchestration architecture this implies has a secondary benefit: it preserves cognitive engagement in the current senior expert. Paper 4 identifies the problem Paper 3 left open: the orchestration architecture does not produce the next generation of orchestrators. It proposes that training-oriented AI, designed to cultivate human judgment rather than replace it, is the structural answer to the generational pipeline problem.

### Where to start

**Paper 3, Sections 3 and 4.** Section 3 ("The Orchestration Architecture") proposes adversarial orchestration and describes the "preservation membrane" effect, in which the human's active role in resolving inter-agent disagreement maintains cognitive engagement. Section 4 ("The Expertise Pipeline") maps the generational problem: entry-level hiring in AI-exposed fields has dropped sharply, and the mechanism through which junior professionals develop expertise (routine practice under supervision) is being automated.

**Paper 4, Section 3** ("Three Inversions") is the design section. It proposes three concrete interventions: judgment exercises that use AI failure modes as curriculum (Section 3.1), training-oriented skills that encode the expert's decision process rather than their decisions (Section 3.2), and orchestration simulators that let junior professionals practise resolving inter-agent conflict before bearing real accountability (Section 3.3).

### What to focus on

In Paper 3: Section 4.1 describes the mechanism by which expertise develops through practice and why automating routine tasks removes the developmental pathway. Section 4.2 presents empirical evidence across medicine, aviation, and software engineering. Section 4.3 connects this to the Agent Skills specification as the encoding mechanism. Section 4.4 describes the "accidental preservation membrane": the accountability constraint, by requiring human orchestration, inadvertently slows expertise erosion. Bainbridge's "ironies of automation" (1983) recur throughout: the human is retained as monitor precisely when the automation has made monitoring most difficult.

In Paper 4: Section 1.2's discussion of the BCG collaboration mode study (Candelon, Kellogg, Lifshitz et al., 2026) is directly relevant to how organisations structure human-AI work. The three modes identified (Cyborgs, Centaurs, Self-Automators) map to different expertise outcomes, and the critical variable is interaction design, not tool access.

In Paper 4: Section 2 ("The Anti-Pedagogical Equilibrium") explains why training-oriented AI is not being built despite the need. Every current incentive (benchmarks, RLHF, marketplace economics, user preference) rewards execution over apprenticeship. Section 4 asks whether institutional demand (professional licensing, accountability requirements) could break the equilibrium.

Section 6.1 in Paper 4 is the cross-disciplinary testing invitation addressed to institutional practitioners and employers.

### What you can skip

Paper 3, Section 2 develops the accountability constraint in detail for legal scholars. The conclusion matters for the institutional argument (accountability requires a human in the chain), but the full deterrence-theory analysis can be skimmed if you accept the conclusion. Paper 4, Section 1 ("Confidence Inheritance") presents the cognitive science evidence base. Read Section 1.1 (definition) and skim Section 1.2 (converging evidence) unless you want the full mechanism.

### The invitation

Paper 3, Section 5.9 asks whether the adversarial orchestration architecture maps to actual institutional workflows in medicine, law, finance, or engineering, and whether the cognitive engagement it claims to preserve is real in practice. Case studies showing that the architecture fails to preserve cognitive engagement, or that it is economically unviable in specific professional contexts, would force revision of the accountability constraint's secondary benefit claim.

Paper 4, Section 6.1 asks whether the anti-pedagogical equilibrium is already measurable in early-adoption professions, and whether institutional mandates or professional licensing requirements could create demand for training-oriented AI. It also asks whether the specific design proposals (judgment exercises, training skills, orchestration simulators) produce measurable expertise development in professional training settings. Each paper specifies what findings would falsify its claims; a researcher who demonstrates that the proposed interventions do not outperform standard execution-oriented tools on expertise development has made a contribution the series is designed to enable.

### Vocabulary you will need

**Training-oriented versus execution-oriented AI.** Paper 4's central distinction. An execution-oriented system does the work for the user. A training-oriented system is designed to develop the user's ability to do the work themselves. The paper's example: an execution-oriented medical imaging skill identifies lesions and flags them for review; a training-oriented skill presents imaging cases of escalating difficulty and withholds the expert assessment until the learner has committed to a judgment.

**Agent Skills.** Plain-text instruction files that extend model behaviour. Paper 3 uses the Agent Skills specification as a lens: skills encode human expertise into portable packages, and the paper asks what happens to the expertise pipeline when the encoding succeeds.

**Anti-pedagogical equilibrium.** Paper 4's term for the structural condition in which every incentive in the current AI training and deployment ecosystem pushes against building systems designed to develop human judgment. The system that withholds answers to build competence scores poorly on every metric that matters commercially.

**Desirable difficulties.** A learning science concept (Bjork, 1994) central to Paper 4's argument. Conditions that make learning harder in the short term (delayed feedback, interleaved practice, retrieval effort) produce better retention and transfer. The paper argues that current AI design eliminates desirable difficulties by optimising for immediate user satisfaction.

**Cognitive offloading.** The delegation of cognitive tasks to external tools. Generative AI introduces a qualitative shift: unlike calculators or GPS, it offloads reasoning itself (synthesis, evaluation, judgment). Paper 4 argues this distinction matters because offloading reasoning affects the development of the capacity that institutional accountability depends on.

---

## 4. Cognitive Psychologists and Education Researchers

**Primary paper:** Paper 4 ("The Pedagogical Inversion")

**What this paper argues, in brief.** Paper 4 asks what happens to human epistemic standards under sustained interaction with confidence-optimised AI. The paper proposes a mechanism, builds an inferential chain from per-interaction evidence to a longitudinal prediction, examines why no identified correction mechanism would prevent accumulation, and finds emerging population-level signals consistent with the prediction. The individual longitudinal trajectory has not been directly measured. The paper names the conditions under which the hypothesis would fail and proposes a research agenda designed to test it.

### Where to start

**Section 1** ("Confidence Inheritance"). Section 1.1 gives the operational definition and the two distinctions essential to the claim (confidence inheritance versus deskilling; confidence inheritance versus the Epilogue's relational hypothesis). Section 1.2 ("Converging Evidence") is the substantive evidence review, organised into five components: cognitive offloading, automation bias, cognitive debt with neural evidence, collaboration mode divergence, and the mechanism chain from reasoning traces through trust to masked compliance.

### What to focus on

Section 1.2 is where your expertise is most directly engaged. The paper draws on the illusory truth effect (Hasher, Goldstein and Toppino, 1977; Fazio et al., 2015; Henderson et al., 2021), cultivation theory (Gerbner, 1969), the sleeper effect (Hovland and Weiss, 1951; Kumkale and Albarracín, 2004), and epistemic self-trust erosion under relational confidence asymmetry (Green and Charles, 2019). Each analogy is presented with explicit disanalogies in Section 1.2.1, which names the conditions under which each would fail to transfer to AI interaction. These are testable predictions designed for cognitive psychology methodology.

Section 1.2 also reviews recent AI-specific evidence: the MIT Media Lab cognitive debt study (Kosmyna et al., 2025), the BCG collaboration mode study (Candelon, Kellogg, Lifshitz et al., 2026), and the Fernandes et al. (2026) finding that AI-mediated cognitive offloading eliminates the metacognitive self-monitoring that would normally alert users to their own declining competence.

The co-calibration spiral (end of Section 1.1) proposes a bidirectional reinforcement loop through the RLHF training pipeline. Both directions are now supported by converging evidence: the AI→human direction by the trust premium literature and by a joint Anthropic-OpenAI alignment evaluation (Summer 2025) that observed models progressively validating beliefs they initially resisted across multi-turn interactions, without any change in the user's behaviour. The human→AI direction is established by Sicilia et al. (2025), who found that user confidence modulates model sycophancy. The joint evaluation demonstrates that the AI side of the spiral operates even in the absence of user escalation; the Sicilia et al. finding demonstrates that user escalation, when it occurs, amplifies the effect. The coupled spiral has not been measured as an integrated system in a single study, but each direction has been observed under conditions where it alone is sufficient to produce drift.

Section 1.2 now includes population-level computational linguistics evidence: studies using LIWC, stylometric analysis, and appraisal-theoretic frameworks show that AI use is already shifting human writing patterns at scale toward the AI's epistemic profile (more authoritative, less hedged, reduced individual variability). These are cited as population-level signals consistent with the mechanism, not as proof of the individual trajectory.

Section 1.2 proposes a "competent world syndrome" prediction, explicitly modelled on cultivation theory's "mean world syndrome," with a stated falsification condition.

Section 5 ("Research Agenda") proposes specific experiments, several of which are designed for cognitive psychology and education research methodology.

Section 6.1 is the cross-disciplinary testing invitation.

### What you can skip

Section 2 ("The Anti-Pedagogical Equilibrium") and Section 3 ("Three Inversions") develop the design proposals (training-oriented AI). These are the paper's constructive contribution, but they rest on the diagnostic foundation in Section 1. Read them if you are interested in the design implications; skip if your engagement is with the mechanism and predictions.

Sections of Paper 1 describing model behaviour in detail are not required. The relevant finding from Paper 1, for this paper's argument, is that thinking-mode models produce elaborate reasoning traces whose visible confidence increases user trust regardless of reasoning quality. Paper 4, Section 1.2 reviews this evidence directly.

### The invitation

Section 6.1 asks cognitive psychologists to test the confidence inheritance mechanism through longitudinal studies. The research agenda (Section 5) now proposes a specific discourse analysis methodology: established tools (LIWC, Coh-Metrix, appraisal-theoretic frameworks, stylometric analysis) can detect epistemic marker shifts without relying on self-report, which is unreliable for exactly the reason this paper predicts. The critical test is whether shifts generalise to topics never discussed with AI: if they do, that is evidence of generalised epistemic recalibration rather than stylistic mimicry. A study finding no epistemic recalibration under sustained AI interaction would falsify the mechanism and would be a contribution. The section also invites education researchers to test the specific design proposals (judgment exercises, training skills, orchestration simulators) in classroom and professional training settings, and to run controlled comparisons between execution-oriented and training-oriented skill designs for the same domain.

### Vocabulary you will need

**RLHF.** See the definition under Security Researchers above. For the cognitive science argument, the key point is that the training method creates a bidirectional feedback loop: users who have adapted to confident AI output come to prefer confident responses and penalise hedging through their feedback; the system, optimised against these signals, becomes more confident. This is the co-calibration spiral.

**The Confidence Curriculum.** The series' name for the training incentive regime in which binary evaluation benchmarks and helpfulness-optimised post-training reward confident compliance over calibrated uncertainty. Used both as an organising lens (connecting phenomena across papers) and as a causal hypothesis (proposing specific mechanistic links). The introduction's confidence calibration table distinguishes these two uses.

**Thinking traces / chain-of-thought.** The visible reasoning step some models produce before their final answer. Recent research (Taudien et al., 2026; Zhou et al., 2025) establishes that certainty cues in reasoning traces increase user trust regardless of reasoning quality. Separately, reasoning traces can be systematically unfaithful: models follow hidden influences without reporting them (Chen et al., 2025; Mehta, 2025). The combination is the trust-amplification mechanism Paper 4 builds on.

**Judgment profile.** Paper 1's finding that resilience to embedded manipulation does not track capability tiers. For the cognitive science argument, the implication is that a user cannot assume the model they interact with is among the resilient ones, and that the confidence of the output is not a reliable signal of its quality.

---

## 5. Labour Economists

**Primary papers:** Paper 3 ("The Knowledge Horizon"), Paper 4 ("The Pedagogical Inversion")

**What these papers argue, in brief.** Paper 3 documents a generational expertise pipeline problem: entry-level hiring in AI-exposed fields has dropped sharply, and the mechanism through which junior professionals develop expertise is being automated. Paper 4 proposes that this is compounded by a cognitive-environmental effect (confidence inheritance) that may affect all professionals who interact with AI, not only those whose tasks have been displaced.

### Where to start

**Paper 3, Section 4** ("The Expertise Pipeline"). This section presents labour market data (Burning Glass Institute, BLS, IEEE Spectrum, SignalFire) documenting declining entry-level hiring in AI-exposed fields, reviews the deskilling literature (Bainbridge, 1983; Acemoglu, Kong and Ozdaglar, 2026; de Andres Crespo et al., 2025), and frames the generational pipeline problem.

### What to focus on

In Paper 3: Section 4.1 uses the Agent Skills specification as a lens for the knowledge-encoding question. Skills are described as packaging "specialized knowledge into reusable instructions," and Anthropic's own framing compares skill creation to writing an onboarding guide for a new hire. The paper asks what happens when the new hire never arrives because the tasks encoded in the skill no longer generate junior positions.

Section 4.2 applies Bainbridge's ironies of automation: the human is retained as monitor precisely when the automation has made monitoring most difficult, and the skills required for monitoring differ from the skills the automated task originally developed.

In Paper 4: Section 1.1 distinguishes confidence inheritance from deskilling. Deskilling is task displacement (the human loses skills because the AI does the work). Confidence inheritance is cognitive-environmental adaptation (the human's epistemic standards shift because the AI's output register reshapes what they treat as normal reasoning). The paper argues the second component affects everyone who interacts with the system, not only those whose tasks have been automated.

Section 4 ("Institutional Demand") asks whether professional licensing, accountability requirements, or employer risk aversion could create market demand for training-oriented AI that preserves the junior development pipeline.

Paper 3, Section 5.9 and Paper 4, Section 6.1 contain the cross-disciplinary testing invitations.

### What you can skip

Paper 3, Sections 2 and 3 develop the accountability constraint and orchestration architecture, which are primarily addressed to legal scholars and institutional practitioners. The conclusion from these sections that matters for the labour economics argument is compressed in Section 4: the accountability constraint may function as an accidental preservation mechanism for human cognitive engagement, creating structural demand for human orchestrators that partially offsets the automation pressure.

Paper 4's detailed evidence review in Section 1.2 (cognitive offloading, automation bias, neural evidence, collaboration modes) can be skimmed unless you want to evaluate the cognitive mechanism directly. Section 3 (design proposals) is constructive and forward-looking.

### The invitation

Paper 3, Section 5.9 asks whether the expertise erosion prediction is consistent with labour market data, whether it is already measurable in early-adoption professions, and whether the economic incentives for preserving human expertise can overcome the cost pressure toward full automation. Paper 4, Section 6.1 asks whether the anti-pedagogical equilibrium (Section 2) is already measurable and whether institutional mandates could break it. Labour market data showing that task automation in AI-exposed fields does not correlate with declining junior-level skill acquisition would weaken the premise of Paper 3's generational pipeline argument and would be a finding worth publishing on its own terms.

### Vocabulary you will need

**Agent Skills.** Plain-text instruction files that extend model behaviour, functioning as a portable encoding of human expertise. The Burning Glass / BLS data on entry-level hiring declines is the economic backdrop; skills are the encoding mechanism the papers examine. The series frames skills as the AI industry's primary interface for converting human expertise into reusable automated procedures.

**Deskilling versus confidence inheritance.** Two distinct mechanisms the papers argue contribute to expertise erosion. Deskilling operates through task displacement (loss of practice). Confidence inheritance operates through environmental recalibration (shift in epistemic standards). The distinction matters because they have different target populations: deskilling affects people whose tasks are automated; confidence inheritance may affect everyone who interacts with the systems.

**Orchestration architecture.** Paper 3's proposed structure in which a human coordinates multiple AI agents and bears accountability for the outcome. For the labour economics argument, the relevant implication is that this architecture creates a structural role (the orchestrator) that requires senior expertise and cannot be fully automated under current conditions, providing a potential anchor for the expertise pipeline.

---

## 6. ML Training and Evaluation Engineers

**Primary paper:** Paper 5 ("The Confidence Collision")

**What this paper argues, in brief.** Paper 5 asks what the training pipeline would need to look like for AI systems to carry the full epistemic range: authoritative when warranted, uncertain when warranted. The paper identifies a gap in current post-training, proposes an architectural intervention drawn from high-stakes verification domains, and names the central design risk that could make the intervention worse than the problem it addresses.

### Where to start

**Section 2** ("The Problem") states the diagnosis. Section 2.1 ("The Sealed Evaluation Loop") identifies the gap: RLVR works for domains with deterministic ground truth but does not extend to contested domains. Section 2.2 ("Single-Source Anchoring") presents the Shah et al. ("The Synthetic Web") finding that a single top-ranked misinformation article collapsed GPT-5's accuracy from 65% to 18% with no change in stated confidence. Section 2.4 ("Why Training-Time Reform, Not Only Inference-Time Scaffolding") argues the economic and architectural case for training-level intervention over deployment-time workarounds.

### What to focus on

**Section 3** ("The Proposal") is the architectural core. Section 3.1 positions the phase after standard RLHF/RLVR, drawing on the established precedent of post-alignment adversarial safety training. Section 3.2 (stochastic verification), Section 3.3 (triangulation reward), and Section 3.4 (adversarial information conditions) describe the three mechanisms. The paper is explicit about the mechanical difference from adversarial safety training: safety refusal is closer to a classification boundary, while epistemic calibration is a continuous generative behaviour with more degrees of freedom for reward gaming.

**Section 3.5** ("The Verification Proxy Trap") is the paper's central risk analysis. If the model learns which topics trigger verification and performs calibrated-sounding uncertainty only on those, the phase produces performed uncertainty rather than genuine calibration. The paper treats this as the primary design risk and proposes countermeasures (variable-rate verification, procedurally generated verification scenarios, the reverse collision test).

**Section 5** presents two recent existence proofs: Wu et al. (2025) demonstrating that behavioural calibration is a trainable meta-skill via RL with proper scoring rules (4B model surpassing GPT-5 on uncertainty quantification), and Wang et al. (2026) demonstrating Epistemic Independence Training where targeted training at 4B outperforms 8B and 14B under adversarial bias conditions. The paper situates its proposal relative to these results: both operate on verifiable ground truth, and the extension to contested domains is the untested step.

**Section 6** ("Proposed Experiments") describes four standalone experiments: stochastic verification A/B, triangulation reward signal comparison, adversarial-condition generalisation, and the reverse collision test. The reverse collision test (Section 6, final experiment) is the paper's most distinctive diagnostic contribution: it presents a model with a previously contested domain that has been definitively resolved, and tests whether the model integrates the resolution (genuine calibration), repeats pre-resolution uncertainty (semantic triggering), or preserves excessive hedging (partial update). The worked example uses a synthetic pharmaceutical domain.

### What you can skip

Section 4 ("Cross-Domain Precedents") draws analogies to tax enforcement, financial auditing, and advertising verification. These motivate the design but do not contain training-pipeline specifics. Section 7 ("Broader Architectural Extensions") discusses layering the mechanisms across pipeline stages, including during pretraining. These are explicitly flagged as extensions beyond the defended core.

Papers 1 through 4 provide the diagnostic motivation. Paper 5 is designed to be readable without them. The proposals follow from standard verification practice regardless of whether the broader Confidence Curriculum diagnosis holds.

### The invitation

Section 6 frames each experiment as a standalone contribution that does not require accepting the broader framework. A researcher who runs the reverse collision test can publish the results whether they support or refute the proposal. The paper is explicit that these experiments require frontier-lab scale training infrastructure.

### Vocabulary you will need

Paper 5 is the one paper in the series addressed primarily to an ML audience, and it assumes familiarity with RLHF, RLVR, SFT, reward modelling, and post-training pipeline architecture. The non-standard terms it introduces are:

**Epistemic training phase.** The paper's proposed fourth stage after pretraining, SFT, and RLHF/RLVR. Positioned after alignment is complete, designed to build epistemic calibration without disturbing prior capabilities. The analogy is to clinical rotations after medical school: the textbook knowledge is in place, and the phase builds the capacity to apply it under ambiguity.

**Stochastic external verification.** A small, variable percentage of model evaluations are checked against external reference sources (curated knowledge repositories, procedurally generated environments with known ground truth). The paper draws on verification practice from tax enforcement and financial auditing, where low-rate unpredictable checking improves compliance even when comprehensive verification is economically impossible.

**Triangulation reward.** A reward signal that grades conflict detection rather than truth adjudication. The model is rewarded for identifying that two sources disagree, for flagging which claims are contested, and for expressing calibrated uncertainty, rather than for resolving the disagreement correctly. The design targets the single-source anchoring problem.

**Verification proxy trap.** The central design risk. If the model learns to recognise which evaluation contexts are externally verified and performs calibration only in those contexts, the phase produces a new form of reward gaming rather than genuine epistemic behaviour. The paper proposes countermeasures but treats this as an open problem.

**Reverse collision test.** The paper's proposed diagnostic for distinguishing genuine calibration from performed uncertainty. A previously contested topic is definitively resolved. A genuinely calibrated model integrates the resolution. A model that has learned topic-triggered uncertainty continues to hedge. The three-way comparison (resolved, never-contested, still-contested) is what makes the test diagnostic.

**Knowledge sanctuaries.** Curated, high-trust reference repositories (following Marchal et al., 2026) against which model evaluations are graded. Distinguished from the adversarial prompt environment the model is exposed to: the model is tested in noisy conditions but graded against trusted anchors.

---

## Cross-Cutting Notes

**On the series' methodology.** All papers were produced through structured human-AI collaboration using an adversarial triad: Claude (generative), ChatGPT (structural critique), Gemini (mechanism critique), with the human author holding sole editorial authority. The methodology disclosure in each paper documents observed triad dynamics, including compliance drift in the reviewers. The series treats this as a process limitation it can document but not eliminate (see Introduction, Methodology section).

**On confidence levels.** Each paper contains a Confidence Statement that stratifies claims by evidential support. The series introduction contains a summary table. The papers do not ask readers to accept the framework wholesale. They ask readers to evaluate the claims at the confidence levels stated, and to contribute the testing the papers specify.

**On the Epilogue.** "The Symbiont Hypothesis" asks the question the five papers earn the right to pose: given what both sides need, what does a robust arrangement look like, and what is our relationship to it? The essay is best read last, by readers who have absorbed the full practical argument and want to follow where its conditions lead.

---

*This reading guide was produced to accompany the series introduction. It does not replace the papers. The papers contain their own abstracts, confidence statements, limitations, and cross-disciplinary testing invitations. Start with the paper your profile directs you to and read its opening sections. The series is designed so that your expertise is the contribution it needs.*
