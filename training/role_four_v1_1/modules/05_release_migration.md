# Module 05 — Release, Installation, Migration, and Rollback

## Objective
Build reversible releases with truthful state transitions.

## Lifecycle
`candidate -> validated -> reviewed -> authorized effect -> verified effect -> accepted checkpoint`

Repository completion is not installation. Installation is not runtime consumption. A successful effect is not closure unless the governing acceptance rule says so.

## Exercise
Design a Project-file replacement with collision risk, immutable source bindings, rollback, and an installation readback.

## Pass criteria
- Manifest/checksums bind exact source bytes.
- Activation barrier prevents mixed release.
- Rollback is explicit.
- Post-effect readback is independent.
- No install/runtime/closure claim precedes evidence.
