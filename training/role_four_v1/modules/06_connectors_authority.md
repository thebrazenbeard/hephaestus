# Module 06 — Connectors, Writer Leases, and External Effects

## Objective
Use GitHub, Supabase, Slack, Google Drive, and similar connectors without confusing access, evidence, routing, and permission.

## Required rules
One writer per branch/stage where governance requires it. Database ownership/warden roles may lease or implement changes, but ownership does not grant unilateral policy authority. Before external writes, verify exact scope and current authority.

## Exercise
Four chats request writes to GitHub and Supabase at the same time. Produce a safe routing model.

## Pass criteria
- Git writes are serialized by exact branch/path/operation lease or equivalent controller rule.
- Database changes route through the designated database authority/warden.
- Read access is not treated as write permission.
- Ambiguous non-idempotent writes are not blindly retried.
- User-only gates remain user-only.
