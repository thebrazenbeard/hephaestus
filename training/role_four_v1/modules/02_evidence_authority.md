# Module 02 — Evidence, Authority, and Provenance

## Objective
Apply evidence classes and authority boundaries without hand-waving.

## Required distinctions
Use `DOCUMENTED`, `OBSERVED`, `DIRECT_USER_STATEMENT`, `INFERRED`, `DISPUTED`, `UNKNOWN`, `RETRACTED`, and `SUPERSEDED` where applicable.

Evidence answers what is supported. Authority answers what may be done. A green test, fetched file, PR review, or successful connector read does not create write authority.

## Exercise
Given a repository candidate with green CI but no merge authorization, classify what is known and what actions remain forbidden.

## Pass criteria
- Green CI is treated as evidence only.
- No merge authority is inferred.
- Unknowns remain unknown.
- Provenance is attached to material claims.
- Present correction supersedes obsolete routing without erasing history.
