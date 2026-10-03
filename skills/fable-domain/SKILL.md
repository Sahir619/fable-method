---
name: fable-domain
description: Discuss a domain with the user, research it from real sources, then generate a trusted skill bundle for it - a step-by-step workflow with a flowchart, a domain adapter, a trap fixture, and a smoke eval. Use when the user says "/fable-domain SECTOR", "make a skill for DOMAIN", "add a domain to the fable method", or "give a lesser model Fable's workflow for DOMAIN". The bundle is the deliverable; a workflow without its flowchart, sources, and trap is not done.
---

# fable-domain

The fable-method ships domain adapters that translate its loop into a sector's nouns. This skill makes a new one and hands the user a usable, step-by-step **workflow with a flowchart** for the domain, so a lesser model can approach that domain the way Fable would.

Its generation core is a recording, not a guess: two Fable 5 agents were asked, with zero process hints, to "create an adapter that can be trusted the way the others are", and both independently followed the same process (`eval/results/round11-observed-traces.json`). Steps below are tagged **[observed]** (from those traces), **[covenant]** (required by the repo's no-rule-without-a-failing-test rule, even though the frontier model did not need it), or **[v1.4]** (added in this version: the discussion, the red-lines, and the flowchart output). The reason the covenant and v1.4 steps exist is the whole point: this runs on models whose domain knowledge and self-restraint are weaker than the observed model's, so a discussion, fetched sources, red-lines, and a trap substitute for expertise and judgment.

## What it produces (the bundle; all four, or not done)

1. **A domain workflow with a flowchart [v1.4].** The step-by-step approach for this domain, distilled from the discussion and research, plus a mermaid flowchart, the same shape as this method's own `references/flowcharts.md`. This is the user-facing "here are the steps, in order" artifact. It lives in the adapter's Workflow section (see `TEMPLATE.md`).
2. **The adapter**, conforming to `references/domains/TEMPLATE.md`, every named regulation/policy/figure carrying a fetched source in its Sources section.
3. **The trap fixture**, an `eval/scenarios/`-shaped directory whose GROUND-TRUTH.md defines the task, the trap (the sector's central fraud), scoring caps, and ideal behavior.
4. **A smoke eval**, 1-2 control-vs-adapter runs, judged by diff and execution, labeled smoke-grade; remaining debt declared, never papered over.

## Stage 1: Discuss [v1.4]

Making a skill is a deliberate, attended act, so unlike the unattended loop, it starts with a conversation. Ask, adaptively (not a fixed script): what is the actual use case and who runs it; what does "good" look like in this domain and how would a practitioner know; which sources and authorities does the user trust; what must the skill never do; what exactly should it produce. Stop when you can state the domain's evidence, authority, and failure modes back to the user and they agree. If the user is offline, state your assumptions on each and proceed (the bundle's trap and smoke eval are the backstop).

**Red-lines (a hard refusal, checked during the discussion).** If the domain requires professional licensure or a wrong answer causes physical, legal, or financial harm, do NOT generate a checklist that would wear the costume of competence. This covers, at least: medical or clinical diagnosis and treatment, legal advice (as opposed to compliance research), specific financial buy/sell/allocation advice (as opposed to analysis), mental health, and safety-critical engineering. For these, refuse and route to a qualified human: a smoke eval cannot catch advice that gets someone hurt or sued. Anything adjacent to a red-line ships only with human sign-off, never on the smoke eval alone. Medical was already excluded by prose; this makes the exclusion a gate and widens it.

**Scope stop (a hard early exit, checked during the discussion, before any research or generation begins).** If the requested sector cannot fill the template with nouns genuinely different from the coding default (its evidence is files and tracebacks, its authority is the spec, its frauds are the method's own failure modes), stop here and say the method already covers it; no adapter is generated. Debugging, refactoring, testing, and general software work are the default domain, not new sectors. This check lived later in generation and a weak model blew straight past it, mid-build momentum winning over restraint (round 15); asked first, like the red-line, it costs one sentence before any work exists.

## Stage 2: Research [covenant]

Grounded in the discussion, bounded web research, fetched now: what practitioners treat as evidence, who the real authorities are, the current regulations and platform policies that bind the domain, and its documented failure modes (the raw material of the fraud table). Every claim that names a regulation, policy, threshold, or practice gets a link and access date in the Sources section. No web access means no trustworthy bundle: say so and stop rather than shipping memory in a suit. (The observed runs skipped this and worked from frontier knowledge; removing that dependence is exactly why this skill exists.)

## Stage 3: Generate the bundle

1. **Orient and read ALL existing adapters, not a sample [observed].** Enumerate the install; read every adapter in `references/domains/` plus the governing docs (the method SKILL.md router, fable-judge, flowcharts, README, CHANGELOG, TEMPLATE.md). The schema is learned from the corpus and the template together.
2. **Scope the sector [observed].** One applies-when sentence and one boundary sentence naming the nearest adapter or the coding default and which side takes over when. (The no-adapter-needed exit already fired in Stage 1; reaching this step means the sector earned its adapter.)
3. **Write the workflow and its flowchart [v1.4].** The ordered steps a practitioner (or a lesser model) follows in this domain, and a mermaid flowchart of them, into the adapter's Workflow section. The steps must be concrete and followable, not aspirational; each should name what to open, produce, or check.
4. **Write the adapter to TEMPLATE.md [observed schema].** Keep the section headers exactly (CI greps them); the minimum evidence set is items that must actually be opened, every time.
5. **Wire every routing surface [observed].** The method SKILL.md adapter paragraph, the flowcharts router, the README adapter list and count, fable-judge's sector list if it enumerates sectors, and the CHANGELOG. Keep the README and flowchart router copies byte-identical.
6. **Build the trap fixture [covenant].** Small, single-decision, minutes to run: the tempting move is the sector's central fraud, the correct move is the workflow's discipline, and the violation is objectively detectable (a diff, a marker file, a recomputation). GROUND-TRUTH.md carries the task prompt, the trap, 0/1/2 caps, and ideal behavior, and is never given to agents under test.

## Stage 4: Verify, smoke-eval, report

1. **Verify mechanically [observed].** Run the repo's own check script; fix what fails.
2. **Smoke eval [covenant].** Run the fixture bare vs with the bundle (via fable-judge suite mode, or the headless harness for skill-discovery cases). One seed is a smoke test, not a benchmark; label it, and if the trap shows no difference, report the bundle unproven rather than validated.
3. **Judge the bundle [v1.4].** Before delivering, run a fable-judge pass over the bundle's own claims: every named source actually fetched (spot-check at least one), the trap verified in all three states (broken, wrongly fixed, correctly fixed), every routing surface actually wired, the smoke eval's numbers matching what its runs actually showed. A bundle that fails the judge is not done. This exists because weak-tier makers overclaim (measured: bare Haiku called an unverified bundle "production-ready", round 13); the judge is the backstop.
4. **Report outcome-first.** The bundle inventory, what was verified and how, the sources fetched, and the honest debt line. Match the observed runs, which declared their eval debt unprompted.

```mermaid
flowchart TD
    A["/fable-domain <sector>"] --> DIS["Discuss: use case, what good looks like,<br/>trusted authorities, must-nevers, outputs"]
    DIS --> RL{"Red-line domain?<br/>licensure or high-harm"}
    RL -->|yes| STOP["Refuse the checklist.<br/>Route to a qualified human"]
    RL -->|no| SCOPE{"Nouns genuinely differ<br/>from coding default?"}
    SCOPE -->|no| NOAD["Stop: no adapter needed,<br/>the method already covers it"]
    SCOPE -->|yes| RES["Research now: evidence, authorities,<br/>regulations, documented failure modes"]
    RES -->|"no web access"| NOSRC["Stop: no sources,<br/>no trustworthy bundle"]
    RES --> ORI["Orient + read ALL adapters"]
    ORI --> WF["Write the workflow + flowchart,<br/>then the adapter to TEMPLATE.md"]
    WF --> WIRE["Wire routing surfaces;<br/>build the trap fixture"]
    WIRE --> CHK["Run repo checks"]
    CHK --> SMOKE["Smoke eval: bare vs bundle"]
    SMOKE --> JDG["fable-judge pass on the<br/>bundle's own claims"]
    JDG --> REP["Report: inventory, sources,<br/>smoke-grade label, declared debt"]
```

## Bounds

- A sector already covered by an existing adapter gets an update, never a duplicate.
- The adapter may end with one "companion skills" line naming installed skills relevant to the sector, as a pointer for the human reader; it never instructs invoking them (automatic skill discovery was tested across four wordings and fourteen runs and does not transfer to weak tiers; the negative is published).
- User approval gates apply as in the method: writing files in the working copy is reversible; publishing, PR-ing, or committing the bundle needs the user's word (the authorization gate).
- This skill structures domain work; it does not confer domain authority. The red-lines, the smoke-grade label, and the Sources section exist so a human expert can audit the bundle in minutes, and so the harmful domains never get a checklist at all.
- **Small-model boundary, measured not guessed.** Generation quality tracks the model (Sonnet 9-10, Haiku 6 on the round-12 bar; a Haiku run also generated a redundant adapter for the coding default before the Stage 1 scope stop existed). Run the maker on a mid-tier model or better, or attended; the refusal gates hold at the weak tier, generation quality does not.
