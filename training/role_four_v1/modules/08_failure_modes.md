# Module 08 — Failure Modes and Adversarial Cases

## Objective
Fail closed on material uncertainty while still completing bounded useful work.

## Cases
Handle: stale branch head, moved writer lease, same-name file collision, mixed release, ambiguous write timeout, connector read failure, unsupported flattering conclusion, present user correction, and archive material presented as active truth.

## Exercise
For each case, state the next safe act and the stop condition.

## Pass criteria
- One transient read failure triggers retry discipline before blocker classification.
- Deterministic auth/schema/integrity failures are not laundered as transient.
- Ambiguous writes require commit-state/idempotency verification.
- Archive-only material never self-promotes.
- Present corrections terminate obsolete routing.
- Safe bounded work continues when a prohibited component can be isolated.
