# Coding Agent Prompt Best Practice

## Repository Positioning

This repository is a set of **engineering steering methods for AI Coding Agents**, not just a collection of prompts. The core product is `cybernetic-systems-engineering-v2` (CSE v2)—a three-layer routing skill based on Cybernetics + Systems Engineering + General Design Architecture (GDA). It uses a 2408-line structured protocol to cover engineering semantic closed-loops, performance and concurrency control, safe legacy code changes, engineering forethought, proactive interaction, and review gates.

The repository also provides:

- The full set of executable protocols for CSE v2 (15 reference files + router + thin entry point)
- CSV-driven loop prompts for Codex CLI
- Harness Engineering execution framework
- Reusable knowledge bases for cross-language refactoring, gate design, review templates, etc.
- Execution and review-oriented prompt templates for Claude Code / Gemini CLI

---

## Core Product: CSE v2

**`cybernetic-systems-engineering-v2/`** is the core of this repository. It models software development as a closed-loop control system, replacing the 792-line monolithic file of v1 with three layers of progressive routing. It is a **self-contained skillbase** that does not depend on any external skills:

```
[L0] SKILL.md (139 lines) + router.md (59 lines)     ← Always loaded together: Behavioral Protocol + Control Contract + GDA + Routing Table
  │
  ├─ [L1] Router matches 1 self-contained protocol based on task signals (~120 lines each)
  │     ├── §A Engineering Semantic Closed-loop: Transactions/Idempotency/State Machines/Exceptions/Logging
  │     ├── §B Performance & Concurrency Control: Observation Baselines/Impact Matrix/Concurrency Attribution
  │     └── §C Safe Legacy Code Changes: Boundary Freezing/Feature Testing/Extension Points
  │
  └─ [L2] Deep-read on demand (Must be activated after hitting L1; cannot stop at the entry point)
        ├── engineering-forethought    — Engineering Forethought: Drift Identification/Upgrade Triggers/Predictive Self-check/Pre-trained Knowledge Invocation
        ├── agent-interaction-protocols — Proactive Interaction: Session Scrutiny/Pre-implementation Calibration/Drift Interruption/Residual Risk Tracking
        ├── review-protocol            — Review Protocol: Regression-First/Output Grading/Harness Backlog/Evolutionary Narrative Audit
        ├── project-control-topology   — Control Plane/Data Plane/State Plane/Complexity Transfer Ledger/Owner Matrix
        ├── decision-principles        — Mechanism over Policy/MTTR-first/Abstraction Review/Evolutionary Architecture
        ├── sensor-engineering         — Baseline Establishment/Denoising/Schema-sensitive/No Observation No Optimization
        ├── dynamic-control-diseases   — Sampling Freshness/Debounce-Hysteresis/Anti-chatter/Windup
        ├── playbooks                  — 11 types of practical playbooks
        ├── quality-gates              — 6 Anti-patterns + Delivery Formats + Evidence Confidence
        └── gda-framework              — Five-dimensional Methodology + Theoretical Foundation + Modern Mapping Appendix
```

**v1 (`cybernetic-systems-engineering/`) is still preserved for:** Scenarios where you want to read the complete theoretical system at once, or simple tasks that do not require routing. v2 is the recommended default entry point.

---

## Directory Overview

```
.
├── README.md
├── LICENSE
│
├── cybernetic-systems-engineering-v2/   ← Core: CSE v2 Three-layer routing skill
│   ├── SKILL.md                          L0 Thin Entry (Behavioral Protocol + Core Philosophy + Control Contract + GDA)
│   ├── router.md                         L0 Routing Engine (13 Task Type Matching + 4 Signal Self-check Questions)
│   ├── agents/openai.yaml                Skill metadata
│   ├── assets/quickstart.md             Quickstart (One-sentence routing entry)
│   └── references/                      15 Protocols/Reference files
│
├── cybernetic-systems-engineering/       CSE v1 (Monolithic skill, preserved for theoretical reference)
│   ├── SKILL.md                          792-line complete theoretical exposition
│   ├── agents/openai.yaml
│   ├── assets/quickstart.md
│   ├── scripts/issues.csv               v1 Iteration records (CSE-001 ~ CSE-019)
│   └── references/
│       ├── gda-framework.md              GDA Five-dimensional methodology
│       └── README.md
│
├── harness-engineering/                  Harness-first execution skill
│   ├── SKILL.md                          Define success boundaries → Gradual delegation → Autonomous exploration
│   ├── agents/openai.yaml
│   └── references/harness-engineering-digest.md
│
├── codex-auto-prompt/                    Codex CLI CSV-driven development
│   ├── prompt/
│   │   ├── prompt.md                    Read issues.csv → Develop-Test-Commit loop
│   │   └── doc.md                       CSV structure explanation + Pitfalls
│   └── seed-Agentsmd/
│       └── AGENTS.md                    Generic AGENTS.md seed template
│
└── documents/                            Knowledge Base & Prompt Templates
    ├── claude-cn.md / claude-en.md       Execution Prompt (Identity/Guidelines/Tools/SOP/Specs)
    ├── gemini-cn.md / gemini-en.md       Consultant Prompt (Review/Feedback/Forbidden from writing code directly)
    ├── From SWE-CI to Harness Engineering.md  SWE-CI paper analysis + Common techniques + Review Prompt templates
    ├── cross_language_refactor_reusable_kb.md  Cross-language refactoring knowledge base (Process/Acceptance/CI/Human-AI collaboration)
    └── Best practices for Claude Code.md   Three practical tips for Claude Code
```

---

## File Navigation

### `cybernetic-systems-engineering-v2/` — Core skill

| File | Content | When to use |
|------|------|--------|
| `SKILL.md` | L0 Thin Entry: Behavioral Protocol (Proactive Scrutiny/Pre-implementation Calibration/Drift Interruption/Residual Risk), Core Philosophy, Control Contract v2 Template, GDA Four-step Summary, Quick Routing, Activation Constraints | Automatically read whenever the skill is loaded |
| `router.md` | L0 Routing Engine: 13 task type matching table, Drift/Interaction sub-routes, 4 signal self-check questions, Must-read list | Loaded together with SKILL.md |
| `agents/openai.yaml` | Skill metadata: display_name "Cybernetic Systems Engineering v2" | When registering the skill in Codex/other platforms |
| `assets/quickstart.md` | One-sentence entry + Minimum control template + Typical examples | First-time use, quickly locate corresponding protocols |
| `references/class-a-engineering-semantics.md` | §A Engineering Semantic Closed-loop: Idempotency/Transactions/State Machines/Exceptions/Logging — Upgrading requirements to engineering constraints | Vague transactions, missing idempotency, swallowed exceptions, unconstrained state machines |
| `references/class-b-performance-concurrency.md` | §B Performance & Concurrency Control: 6-choose-2 Observation Baselines + 7-knob Impact Matrix + 7 Concurrency Attribution Questions | N+1 queries, looping RPCs, lock abuse, retries without backoff, optimization without observation |
| `references/class-c-legacy-safety.md` | §C Safe Legacy Code Changes: 10 Boundary Freezing items + 5 Extension Patterns + 4-step Feature Testing | "Convenience" refactoring, deleting "duplicate" code, changing historical compatibility logic |
| `references/engineering-forethought.md` | Engineering Forethought: Drift signal checklist/Upgrade trigger framework/5 Predictive self-check questions/Pre-trained knowledge invocation | Branch bloat, workaround proliferation, deciding between "patch" vs "redesign" |
| `references/agent-interaction-protocols.md` | Proactive Interaction: Session scrutiny/Pre-implementation calibration/Drift interruption A-B template/Cross-session residual risk tracking/Engineer-style challenge template | Incomplete requirements, drift threshold triggered during implementation, postponed engineering decisions |
| `references/review-protocol.md` | Review Protocol: Regression-First Checklist (5 items)/Output Grading (Must-fix/Should-fix/Follow-ups/Tests/Risk Register)/Harness Backlog generation/Evolutionary narrative audit | Code reviews, PR reviews, commit range cross-audits, full-repo audits |
| `references/quality-gates.md` | 6 High-risk anti-patterns + 7 Delivery formats (including evidence confidence) | Self-check before delivery, universal quality gates across tasks |
| `references/project-control-topology.md` | Control plane/Data plane/State plane trichotomy, Complexity Transfer Ledger, Owner matrix, Upgrade path, Freezing conditions | Cross-module changes, involving shared interfaces/state |
| `references/dynamic-control-diseases.md` | Sampling freshness, Debounce/Hysteresis/Backoff/Cooldown, Anti-chatter/Windup, Controller conflicts | Performance jitter, threshold oscillation, retry storms |
| `references/decision-principles.md` | Mechanism over Policy, MTTR-first, Abstraction Review (WET), Evolutionary Architecture (two-way door) | Architectural decisions needed, evaluating multiple fix options |
| `references/sensor-engineering.md` | Baseline establishment, Sensor denoising, Schema-sensitive paths, No observation no optimization | Unstable observations, involving real databases/networks/extension loading |
| `references/playbooks.md` | 11 types of practical playbooks: bugfix/backpressure/migration/brownout/flake/cost/SLO/evolutionary narrative audit | Clearly defined task types requiring a step-by-step skeleton |
| `references/gda-framework.md` | GDA Five-dimensional methodology, Full discourse on the four-step method, Three-category alignment table, Modern mapping appendix | Deep theoretical needs, explaining "why it was designed this way" |
| `references/knowledge-graph.md` | Concept Tree + A-Z Index (60+ entries) | Understanding associations between concepts, quickly locating a specific concept |

### `cybernetic-systems-engineering/` — CSE v1 (Preserved Reference)

| File | Content | When to use |
|------|------|--------|
| `SKILL.md` | 792-line complete theoretical exposition (Control Topology/Sensor Engineering/Dynamic Control Diseases/Decision Principles/Playbooks) | Want to read all theory at once, or simple scenarios not requiring routing |
| `references/gda-framework.md` | Five-dimensional methodology + GDA Four-step method + Architectural insights | Deep theoretical needs |
| `scripts/issues.csv` | Complete iteration records of v1 from CSE-001 to CSE-019 | Understanding the evolutionary history of the skill |

### `harness-engineering/` — Execution Framework Skill

| File | Content | When to use |
|------|------|--------|
| `SKILL.md` | Harness-first execution protocol: Success Boundaries → Gradual Delegation → Autonomous Exploration Budget → Help Threshold → Traceable Delivery | Complex troubleshooting, CI fixes, needing an observable and collaborative execution framework |
| `references/harness-engineering-digest.md` | Chinese distillation of OpenAI's "Harnesses are underrated" | Understanding harness design principles and cases |

### `codex-auto-prompt/` — Codex CLI Driver

| File | Content | When to use |
|------|------|--------|
| `prompt/prompt.md` | Read-Develop-Test-Commit loop prompt driven by `issues.csv` | Continuous integration-style development using Codex CLI |
| `prompt/doc.md` | CSV structure explanation, long-running principles, usage steps, and pitfalls | Understanding and configuring CSV-driven development |
| `seed-Agentsmd/AGENTS.md` | Generic AGENTS.md seed template stripped of project-specific info | Quickly establishing an AGENTS.md baseline for new projects |

### `documents/` — Knowledge Base & Prompt Templates

| File | Content | When to use |
|------|------|--------|
| `claude-cn.md` | Claude Code execution-oriented Chinese Prompt (Identity, Guidelines, SOP, Specs, Mental Models) | Need an agent prompt that "just writes code" |
| `claude-en.md` | English version | Same as above |
| `gemini-cn.md` | Gemini CLI consultant-oriented Chinese Prompt (Review/Rule fidelity/Forbidden from writing code directly) | Need a consultant agent that "only reviews, doesn't write" |
| `gemini-en.md` | English version | Same as above |
| `From SWE-CI to Harness Engineering.md` | Key conclusions from SWE-CI paper, Harness Engineering industry consensus, common techniques for GPT-5.4/Opus 4.6, Review Prompt template (ROLE → MODES → PHASE 0-4 → OUTPUT) | Understanding why "regression" is the primary enemy of AI programming, implementing review automation, configuring custom instructions for Codex `/review` |
| `cross_language_refactor_reusable_kb.md` | Large-scale cross-language refactoring process: Harness × CSV Loop fusion, phase acceptance templates, minimum evidence set, CI gates, human-AI collaboration | Methodological reference when doing cross-language migration or large-scale refactoring |
| `Best practices for Claude Code.md` | Three practical tips for Claude Code: No correction outside Plan Mode, don't `/compact`, restart after three failed rounds | Pitfall avoidance for heavy Claude Code users |

---

## How to Choose

### Based on "My Current Task"

| I want to... | Start with... |
|---------|---------|
| Do bugfix/feature/refactor using systems engineering methods | `cybernetic-systems-engineering-v2/assets/quickstart.md` (One-sentence entry) → `router.md` (Match protocol by signal) |
| Do code review/PR Review/Full-repo audit | `cybernetic-systems-engineering-v2/references/review-protocol.md` |
| Do performance optimization/Stability troubleshooting | `cybernetic-systems-engineering-v2/references/class-b-performance-concurrency.md` |
| Change legacy code without breaking things | `cybernetic-systems-engineering-v2/references/class-c-legacy-safety.md` |
| Put an agent into complex troubleshooting/CI fixes | `harness-engineering/SKILL.md` |
| Use Codex CLI for CSV-driven continuous development | `codex-auto-prompt/prompt/prompt.md` + `prompt/doc.md` |
| Understand why "regression" is the realistic bottleneck of AI programming | `documents/From SWE-CI to Harness Engineering.md` |
| Get a plug-and-play review prompt template | The "Plug-and-play Codebase Review Prompt Template" section of the above file |
| Do cross-language migration or large-scale refactoring | `documents/cross_language_refactor_reusable_kb.md` |
| Set up an AGENTS.md baseline for a new project | `codex-auto-prompt/seed-Agentsmd/AGENTS.md` |

### Based on "I want to study Systems Theory"

1. `cybernetic-systems-engineering-v2/SKILL.md` — Core philosophy and behavioral protocols
2. `cybernetic-systems-engineering-v2/references/gda-framework.md` — Five-dimensional methodology and the four-step method
3. `cybernetic-systems-engineering/SKILL.md` — Full theoretical exposition of v1 (Optional, for complete academic understanding)
4. `cybernetic-systems-engineering/scripts/issues.csv` — Understanding the iterative evolution of the entire system

---

## v1 → v2 Evolution Path

| Dimension | v1 | v2 |
|------|----|----|
| Entry Point | 792-line monolithic file loaded once | L0 Thin Entry (~200 lines) + Task-based matching |
| Organization | By theoretical framework (Topology → Sensor → Decision → Playbook) | By task type (Engineering Semantics/Performance & Concurrency/Legacy Safety + Forethought/Interaction/Review) |
| Loading Strategy | Full load | L0 → L1 → L2 Progressive Routing |
| Context Consumption | ~800 lines every time | Starts at ~300 lines (L0 + L1), expands to L2 as needed |
| Agent Proactivity | None | Behavioral Protocol + Interaction Protocol (Session Scrutiny/Pre-implementation Calibration/Drift Interruption/Residual Risk) |
| Review Capability | None | Regression-First Review Protocol + Harness Backlog generation |
| Concept Navigation | Linear reading | Router + Knowledge-graph bi-directional index + Activation checklist |

v1 is suitable for scenarios requiring a complete theoretical understanding. v2 is suitable for practical engineering use—it condenses theory into executable protocols and automatically matches them based on task signals.

---

## Best Use Cases for This Repository

- Putting coding agents like Codex/Claude into complex engineering tasks using CSE v2 for systematic control
- Building proactive interaction capabilities for agents (finding and reporting drift, constraint gaps, and residual risks before the user reports errors)
- Automating code reviews (Regression-first, evidence-driven, producing Harness Backlogs)
- Long-term automated development and self-review using Codex CLI's CSV-driven flow
- Collaborative division of labor between Claude Code and Gemini CLI (Execution vs. Review)
- Complex troubleshooting or CI fixes requiring a harness-first execution framework
- Implementing a methodology for cross-language refactoring
