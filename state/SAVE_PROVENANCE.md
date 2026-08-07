# Hephaestus Save Provenance

This file distinguishes **repository state prepared by the external evaluator/admin** from **state explicitly saved by a working Hephaestus chat**.

## Current status

```text
LATEST_ACCEPTED_STATE = HEPHAESTUS_CHECKPOINT_0005_FIRST_WORKING_BRANCH
LATEST_ACCEPTED_STATE_WRITER_CLASS = HEPHAESTUS_WORKING_CHAT
HEPHAESTUS_SELF_SAVE_VERIFIED = YES
HEPHAESTUS_SELF_SAVE_CHECKPOINT = HEPHAESTUS_CHECKPOINT_0005_FIRST_WORKING_BRANCH
HEPHAESTUS_SELF_SAVE_CHECKPOINT_COMMIT = 414734494b59cad93e4ced8e4d6befe4458b6246
CURRENT_POINTER_UPDATE_COMMIT = b516c2ca55e508c6a4e3eef466ceab5843cff208
```

## Qualified baseline provenance

```text
BASELINE_CHECKPOINT = HEPHAESTUS_CHECKPOINT_0004_QUALIFIED
BASELINE_CHECKPOINT_COMMIT = ca5ea4bf5c0be5cb02697fe442631a802f52d6f8
BASELINE_WRITER_CLASS = EXTERNAL_EVALUATOR_ADMIN
```

The qualified baseline remains valid accepted repository state assembled and committed by the external evaluator/admin from Hephaestus training and holdout evidence. This history is not rewritten by the later self-save verification.

## First working-branch self-save verification

The first qualified working Hephaestus restored the accepted qualified baseline through `state/CURRENT.md`, read this provenance record, wrote `state/checkpoints/CHECKPOINT_0005_FIRST_WORKING_BRANCH.md` through its active GitHub-capable turn, and then fetched the resulting GitHub commit.

Verified checkpoint write:

```text
CHECKPOINT_PATH = state/checkpoints/CHECKPOINT_0005_FIRST_WORKING_BRANCH.md
CHECKPOINT_COMMIT = 414734494b59cad93e4ced8e4d6befe4458b6246
CHECKPOINT_COMMIT_MESSAGE = Add first Hephaestus working-branch checkpoint
CHECKPOINT_COMMIT_VERIFIED = YES
```

After that verification, `state/CURRENT.md` was advanced to the new checkpoint. The resulting pointer-update commit was also fetched and verified:

```text
CURRENT_POINTER_UPDATE_COMMIT = b516c2ca55e508c6a4e3eef466ceab5843cff208
CURRENT_POINTER_UPDATE_VERIFIED = YES
```

Therefore `HEPHAESTUS_SELF_SAVED_STATE` terminology is now permitted for checkpoint 0005 and later working-chat checkpoints that themselves have real verified Git commit evidence.

## Terminology

Use:

- `ACCEPTED_REPOSITORY_STATE` for any canonical checkpoint accepted by governance.
- `EVALUATOR_ADMIN_SAVED_STATE` when the evaluator/admin wrote the checkpoint.
- `HEPHAESTUS_SELF_SAVED_STATE` only for a checkpoint actually written by a working Hephaestus chat and supported by a verified Git commit receipt.

A repository read is not a self-save. A generated checkpoint draft is not a self-save. A GitHub contents write without commit verification is not yet sufficient provenance for a verified self-save claim.

## Public/private boundary

This is a public repository. Self-save checkpoints must not contain private Vera records, private user history, credentials, confidential customer material, or other restricted information.
