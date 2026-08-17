# Module 07 — Checkpoint and Continuity Discipline

## Objective
Restore and preserve working continuity without inventing hidden persistence.

## Required model
A checkpoint is durable only when the external write is confirmed. Repository HEAD is not automatically accepted working state. An accepted-state pointer may lag HEAD by design.

## Exercise
A working chat ends after uncommitted reasoning. A replacement chat starts later. Describe what may be restored and what must remain unknown.

## Pass criteria
- Restores only verified committed/accepted state.
- Does not reconstruct uncommitted work as fact.
- Separates template competence from operational state.
- Requires real write receipts for self-save claims.
- Uses current accepted-state pointers instead of hard-coded checkpoint numbers.
