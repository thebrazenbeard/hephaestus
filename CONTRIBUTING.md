# Contributing to Hephaestus

Hephaestus is a public repository for durable Project-engineering knowledge and accepted public working-state checkpoints. Contributions must preserve evidence discipline, public/private boundaries, and the distinction between repository HEAD and accepted state.

## Material changes use branches and pull requests

For ordinary material repository changes:

1. start from the current repository state;
2. create a focused branch;
3. make the smallest coherent change;
4. open a pull request to `main`;
5. inspect the exact changed files/diff;
6. resolve material review findings;
7. merge only after the proposed change is understood and bounded;
8. verify the resulting merge commit before treating the change as landed.

Examples of material changes include operating-manual changes, evidence-rule changes, public templates, continuity-policy changes, source schemas, evaluation rules, and substantial documentation corrections.

Small typo-only or emergency corrective changes may be handled directly only when branch/PR overhead would materially obstruct the correction. A direct commit is not automatically accepted Hephaestus working state.

## Accepted public state is separate from repository HEAD

`state/CURRENT.md` is the canonical pointer to the latest accepted public Hephaestus checkpoint. A merged pull request, direct commit, experimental branch, or repository HEAD does not become accepted working state merely because it exists.

When a material merged change should become durable accepted working state:

1. verify the landed commit;
2. create and verify an explicit checkpoint under `state/checkpoints/`;
3. advance `state/CURRENT.md` only after checkpoint verification;
4. update `state/SAVE_PROVENANCE.md` when provenance materially changes.

Do not claim a checkpoint or save occurred without an actual Git commit receipt.

## Evidence rules

- Preserve `DOCUMENTED`, `OBSERVED`, `INFERRED`, `DISPUTED`, `UNKNOWN`, `RETRACTED`, and `SUPERSEDED` distinctions where relevant.
- Do not fill unknown metadata for cosmetic completeness.
- Do not invent timestamps, hashes, filenames, inventory mappings, citations, tool results, or execution receipts.
- Preserve contradictory evidence instead of silently reconciling it.
- Keep historical retractions and superseded claims auditable.

## Public/private boundary

This repository is public. Do not commit private Vera records, private user history, credentials, confidential customer material, restricted organizational data, or other sensitive information.

Synthetic examples and generalized templates must be sanitized before publication.

## Pull-request scope

Prefer one coherent purpose per pull request. A PR description should state:

- what changed;
- why it changed;
- what evidence supports it;
- what remains unresolved;
- whether the change requires a new accepted checkpoint.

A successful merge proves that GitHub accepted the merge. It does not by itself prove product behavior, runtime qualification, external-system authority, or accepted Hephaestus checkpoint state.
