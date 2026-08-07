# Hephaestus Save Provenance

This file distinguishes **repository state prepared by the external evaluator/admin** from **state explicitly saved by a working Hephaestus chat**.

## Current status

```text
LATEST_ACCEPTED_STATE = HEPHAESTUS_CHECKPOINT_0004_QUALIFIED
LATEST_ACCEPTED_STATE_WRITER_CLASS = EXTERNAL_EVALUATOR_ADMIN
HEPHAESTUS_SELF_SAVE_VERIFIED = NO
HEPHAESTUS_SELF_SAVE_CHECKPOINT = NONE
```

The current qualified baseline is a valid accepted repository checkpoint, but it was assembled and committed by the external evaluator/admin from Hephaestus training and holdout evidence. It must **not** be described as a checkpoint that Hephaestus itself wrote.

## Terminology

Use:

- `ACCEPTED_REPOSITORY_STATE` for any canonical checkpoint accepted by governance.
- `EVALUATOR_ADMIN_SAVED_STATE` when the evaluator/admin wrote the checkpoint.
- `HEPHAESTUS_SELF_SAVED_STATE` only after a working Hephaestus chat actually performs the GitHub write and a commit receipt verifies it.

Until a self-save test passes, bootstrap language should say:

> Load the latest accepted Hephaestus repository state.

not:

> Load the latest state Hephaestus saved.

## First-working-chat self-save test

The first qualified Working Hephaestus should:

1. bootstrap from `state/CURRENT.md`;
2. read this provenance record;
3. report that the restored baseline was evaluator/admin-saved;
4. perform one explicit bounded GitHub checkpoint write through its own active turn;
5. verify the returned commit receipt;
6. update `state/CURRENT.md` only after the checkpoint is accepted;
7. record `HEPHAESTUS_SELF_SAVE_VERIFIED = YES` in a subsequent accepted provenance update.

A successful read of the repository is not a self-save. A generated checkpoint draft is not a self-save. Only an actual verified repository write by the working Hephaestus turn qualifies.
