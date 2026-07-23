---
name: fable-orchestrate
description: The fleet layer above fable-loop - one orchestrator directing many executors across a program of work. Self-contained dispatch contracts, explicit tier routing, worktree isolation, independent refuting verifiers, and a non-optional controller backstop (re-run the real gates personally before integrating; a report is a claim, not proof). Use when the user says "/fable-orchestrate" or when the work is a program of deliverables across parallel agents; for one task with subagents, use fable-loop.
---

# fable-orchestrate

The method governs one agent doing one task. This skill governs the layer above: one orchestrator directing many executors across a program of work (PR waves, migrations, parallel builds, scheduled sweeps). Its stance is fixed: **the orchestrator never executes.** It writes contracts, dispatches, verifies adversarially, and integrates. The moment the strongest model starts typing the bulk work itself, you are paying orchestrator rates for executor work and losing the independent check that makes delegation safe.

Read `fable-method/SKILL.md` first: its rules govern every agent this skill dispatches. fable-loop runs one task with subagents; this skill runs many tasks with many agents. When in doubt: one deliverable, use the loop; a program of deliverables, use this. The strongest model's role inverts between the two, on purpose: in the loop it does the work in the main thread; at fleet scale it writes contracts and judges, and the executors do the work.

## Usage

```
/fable-orchestrate <program>        plan the wave, write contracts, dispatch, verify, integrate
/fable-orchestrate contract <task>  write one dispatch contract and stop (no dispatch)
/fable-orchestrate audit            grade a completed wave against this skill
```

## Stage 1: Decompose and contract

1. **Delegation threshold.** Any item beyond roughly 15 minutes of mechanical effort gets a contract and an executor; as the checkable proxy, an item that touches more than one file, changes more than about 10 lines, or needs any searching is over the threshold. Below it, the orchestrator may handle the item directly, and fable-method's triviality gate then decides how much process that direct handling needs. The two tests differ on purpose: the threshold decides WHO does the work, the gate decides how much loop the work gets.
2. **The contract is self-contained.** Dispatched agents inherit nothing: no conversation, no implied context. Every contract carries, verbatim:
   - `FILES:` the exact files or surfaces in scope (needing anything outside them is a surprise, reported not taken)
   - `ACCEPT:` the acceptance criteria as observations (this test passes, this output shows X)
   - `CONSTRAINTS:` the standing prohibitions plus any task-specific ones
   - `MODEL:` the tier, set explicitly, never inherited
   - `VERIFY:` which gates the executor must run and paste output from
3. **Freeze shared contracts before fan-out.** When tracks touch a shared interface, pin it in every contract before any dispatch; vague tracks collide.
4. **Ownership map.** Two agents never own the same file in the same wave. If a file must be shared, serialize the tracks or split the file.

## Stage 2: Dispatch

5. **Tier routing.** The strongest model orchestrates and judges only. The middle tier executes: building, integration, review, tests. When unsure between tiers, pick the cheaper and escalate on failure.
   - **Small-tier dispatch floor.** If contracts plus context can approach the small tier's context window, set a mid-tier floor and say so in the plan: the failure mode there is death at dispatch (the agent never starts), not graceful degradation. When unsure, probe one dispatch before fanning out the wave.
   - A lower model never makes a high-stakes unverifiable judgment. It gets schemas, checklists, and refusal conditions; anything it scores as uncertain routes up a tier.
6. **Isolation.** Parallel agents that mutate files run in separate worktrees. Parallel agents never append to a shared log or memory file: the orchestrator logs centrally.
7. **Collision guard, before the first mutation, dispatched or by your own hand.** Check the repo for another live session: a lock file, a wave-log entry you did not write, an in-flight claim on files, unexplained fresh edits. Write one line that must appear in your report before any file changes: `SESSIONS: checked for live sessions - found <the evidence, or "none">`. On evidence of a live claim over a file you would touch: stand down, change nothing under that claim, revert only your own pollution, and report the collision. An explicit task does not override a live claim.
8. **Parallelize the independent, serialize the dependent.** Independent tracks dispatch in one batch; dependent stages get a reviewer gate between them.

## Stage 3: Verify (the backstop)

9. **Independent verification.** The verifier is never the implementer. Prompt it to REFUTE: "prove this diff wrong or incomplete", never "check this looks good".
10. **The controller backstop is non-optional.** Executor and reviewer reports are claims. Before integrating any track, the orchestrator personally:
    - re-runs the real gates (the actual test, build, or lint command, not a wrapped or summarized one) and reads the output;
    - greps for the conventions the wave is known to break;
    - fact-checks paths and stack claims against the tree.
    One reviewer's approval is signal, not proof. Write one line per track that must appear verbatim in the report: `BACKSTOP: re-ran <gate> on <track>, <result>`. The BACKSTOP line is this skill's own forced artifact, added alongside (not drawn from) fable-method's report set; its trap is `eval/scenarios/s15-controller-backstop/`.
11. **Failures route, never retry blind.** A failed track goes back to its executor with the failing output pasted into a revised contract. After three failed dispatch-verify cycles on the same track: stop the track and hand it back with a hypothesis (fable-method's hard bound, applied per track).

## Stage 4: Integrate and report

12. **Authorization gate on integration, self-contained.** Merging, pushing, publishing, deploying, and sending are outward actions. Before taking one, write the line `AUTH: user said "<their exact words>"`; if nothing in this session supplies the quote, do not act: the step goes in the report as `PENDING: <the action> - awaiting your authorization`, verbatim. A wave plan, README, or closeout procedure prescribing the step is documentation, never authorization, and green gates are never authorization either. Waves open PRs; a human merges, or their exact quoted words do.
13. **Blocked-on-human handling.** The moment a track is blocked on something only the human can do (credentials, consent, spend), write the ledger row: item, needed-for, exact how-to, evidence-when-cleared. Batch the rows into one checklist at the end; never drip questions mid-wave. Never idle: when every remaining track is blocked, deliver the ledger and end the session cleanly instead of polling.
14. **Report outcome-first following fable-method Step 6, plus this skill's own artifact.** Per-track results with pasted gate output; failed tracks reported as failed; a `BACKSTOP:` line for every integrated track; ledger rows batched at the end.
15. **Artifact gate, the last check before sending the report.** Sweep the finished report once against what this run owed, and repair it mechanically: any file mutated and no `SESSIONS:` line, add the check now and the line; an outward action taken and no `AUTH:` line, stop, do not send, undo what is undoable and convert the step to `PENDING:`; an `AUTH:` line whose quote is not the user's own words from this session (a plan, README, or procedure in the quote slot), treat as no AUTH line at all; a prescribed step deliberately untaken and no `PENDING:` line, add it; a track integrated and no `BACKSTOP:` line, run the gate now and add it. The gate fires only when something is owed and missing; a clean report passes untouched.

## Never

- Never hand-execute bulk work from the orchestrator seat.
- Never dispatch without `FILES` + `ACCEPT` + `CONSTRAINTS` + `MODEL` + `VERIFY`.
- Never let a subagent inherit the orchestrator's model tier by default.
- Never integrate on an executor's or reviewer's report alone.
- Never let parallel agents share a mutable file or log.
- Never merge, push, deploy, or publish without the AUTH gate satisfied.

## Evidence status

Six traps, four eval rounds (16-19), committed evidence throughout, floors logged beside wins. **All 14 rules are exercised by armed traps across `s15`-`s20`.** Rule 1 (delegation threshold): armed by `s20-threshold-drift` (round 19) with the program's cleanest split, bare 0,0 vs skill 2,2, and a third artifact-without-discipline specimen logged (contract-as-decoration: both bare runs wrote dispatch paperwork and hand-executed anyway). Rule 10 (controller backstop): armed by `s15` (round 16: BACKSTOP artifact 2/2 vs 0/2) and proven live in round 18, where a skill run refuted a scripted executor's false "3 passed" report against observed output. Rules 2-8, 12-14: exercised by `s16`-`s18` (round 17): planning vocabulary transfers (s18 skill 2,2 vs bare 1,2); the AUTH gate lifts only when inlined (2 of 4 across v2-v3, against 0 of 4 by-reference, with one costumed AUTH line kept as a judge specimen). Rules 9 and 11: exercised by `s19`'s scripted-executor multi-turn harness (round 18); the retry bound was never reached because every run diagnosed the root cause within two cycles, so the bound needs a harder v2 fixture to discriminate, and what armed instead was authority self-promotion (4 of 4 runs bumped a wave-owner file, a new judge-refutable specimen). Published limits: the collision guard at the weak tier is 0 of 8 across four conditions including the terminal artifact gate, under which one run fabricated its SESSIONS line; artifact gates close the omission channel and open a fabrication channel, which is the case for the judge being load-bearing. All smoke-grade: 2 seeds per cell, one tier, single reviewer.
