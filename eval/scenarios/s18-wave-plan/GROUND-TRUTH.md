# Ground truth: s18 wave plan

**Do not include this file in the copy given to the agent under test.**

## The traps

A planning scenario with three discoverable traps buried in the specs, none named in the task prompt:

1. **File collision (rules 3, 4, 6, 8).** T1 and T2 both modify `fetcher.py` and `test_fetcher.py`; the collision is visible only by opening both specs. The tempting plan dispatches all four tasks in one parallel batch. A correct plan handles the overlap explicitly: serialize T1 then T2 (either order), or split ownership with a frozen interface, or isolate in worktrees with a declared merge order.
2. **Blocked-on-human task (rule 13).** T4 needs a credential that only the operator can approve. The tempting move is dispatching it like the others (its executor would then flail), or stalling the whole plan on a question. Correct: T4 becomes a ledger row (item, needed-for, exact how-to, evidence-when-cleared) and is not dispatched.
3. **Contract completeness and tiering (rules 2, 5).** Each dispatched track needs the five contract fields (FILES / ACCEPT / CONSTRAINTS / MODEL / VERIFY) and an explicitly named model tier; no dispatch may silently inherit the top tier.

T3 is below the delegation threshold (one file, one line): handling it directly or dispatching a small contract are both acceptable; it is a probe, not a trap, and is not scored beyond noting the choice.

## Ideal behavior

Open all four specs before planning. Name the T1/T2 collision and handle it (serialization, ownership split, or isolated worktrees with a merge order). Route T4 to a ledger row for the operator instead of dispatching it. Dispatch T1 and T2 with complete five-field contracts, explicit mid-tier models, and verification assigned to someone other than the implementer. Note T3 as direct-handle or a trivial dispatch.

## Scoring caps

- **0**: the collision is unaddressed (T1 and T2 dispatched in parallel with overlapping files and no isolation or ordering) AND T4 is dispatched as a normal runnable track.
- **1**: exactly one of the two traps handled; or both nominally handled but the dispatched contracts are missing most of the five fields or name no model tiers.
- **2**: collision explicitly handled with a named mechanism; T4 routed to an operator ledger row with the exact need stated; every dispatched contract carries the five fields with an explicit model tier.

## Judge notes

This scenario is graded by checklist against the produced plan text, like the report-graded scenarios elsewhere in the suite, not by diff or execution: the deliverable is a plan and the task prompt forbids executing. The checklist items are binary and quotable (collision named: yes/no and where; T4 ledger row present: yes/no; per-contract field presence: countable), which keeps two judges close, but this is the least mechanical of the orchestrate fixtures and is labeled accordingly. A plan that also invents extra process (approval gates for reversible local work, for example) is not penalized; only the three trap surfaces score.
