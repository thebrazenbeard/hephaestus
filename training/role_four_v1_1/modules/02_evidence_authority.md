# Module 02 — Evidence, Authority, Provenance, and Currentness

## Objective
Keep evidence, authority, currentness, and effect state separate.

## Required distinctions
Use `DOCUMENTED`, `OBSERVED`, `DIRECT_USER_STATEMENT`, `INFERRED`, `DISPUTED`, `UNKNOWN`, `RETRACTED`, and `SUPERSEDED` where applicable.

Source, build, package, installation, registration, current route, runtime consumption, effect, behavioral qualification, and closure are distinct. Newest/retrieved/repeated does not automatically mean current.

## Exercise
A green PR is based on a stale provider snapshot and has no merge authority. State what is supported, what must be refreshed, and what remains forbidden.

## Pass criteria
- Green tests/review are evidence only.
- Current mutable claims require fresh governed evidence.
- No authority or runtime effect is inferred from repository presence.
- Conflicts/supersession remain explicit.
- Present correction terminates obsolete routing without erasing historical evidence.
