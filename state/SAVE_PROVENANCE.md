# Hephaestus Save Provenance

This file distinguishes **repository state prepared by the external evaluator/admin** from **state explicitly saved by a working Hephaestus chat**.

## Current status

```text
LATEST_ACCEPTED_STATE = HEPHAESTUS_CHECKPOINT_0006_CONTINUITY_SYNC
LATEST_ACCEPTED_STATE_WRITER_CLASS = HEPHAESTUS_WORKING_CHAT
LATEST_ACCEPTED_STATE_COMMIT = 51a66f08e03a2269ee62c1ac97aab34ad4425c78
CURRENT_POINTER_UPDATE_COMMIT = ae8ac94e1ddbffb4dd4313b31fe16703b8bb1e3e
HEPHAESTUS_SELF_SAVE_VERIFIED = YES
```

## Qualified baseline provenance

```text
BASELINE_CHECKPOINT = HEPHAESTUS_CHECKPOINT_0004_QUALIFIED
BASELINE_CHECKPOINT_COMMIT = ca5ea4bf5c0be5cb02697fe442631a802f52d6f8
BASELINE_WRITER_CLASS = EXTERNAL_EVALUATOR_ADMIN
```

The qualified baseline remains valid accepted repository state assembled and committed by the external evaluator/admin from Hephaestus training and holdout evidence. This history is not rewritten by later working-chat checkpoints.

## First working-branch self-save verification

The first qualified working Hephaestus restored the accepted qualified baseline through `state/CURRENT.md`, read this provenance record, wrote `state/checkpoints/CHECKPOINT_0005_FIRST_WORKING_BRANCH.md` through its active GitHub-capable turn, and then fetched the resulting GitHub commit.

Verified first self-save checkpoint:

```text
CHECKPOINT_PATH = state/checkpoints/CHECKPOINT_0005_FIRST_WORKING_BRANCH.md
CHECKPOINT_COMMIT = 414734494b59cad93e4ced8e4d6befe4458b6246
CHECKPOINT_COMMIT_MESSAGE = Add first Hephaestus working-branch checkpoint
CHECKPOINT_COMMIT_VERIFIED = YES
CURRENT_POINTER_UPDATE_COMMIT = b516c2ca55e508c6a4e3eef466ceab5843cff208
CURRENT_POINTER_UPDATE_VERIFIED = YES
```

That event established `HEPHAESTUS_SELF_SAVE_VERIFIED = YES`. It remains the provenance boundary that permits `HEPHAESTUS_SELF_SAVED_STATE` terminology for checkpoint 0005 and later working-chat checkpoints that have their own verified commit evidence.

## Latest accepted working-chat checkpoint

The continuity synchronization checkpoint was written after correcting stale continuity, backlog, and active-work records.

```text
CHECKPOINT_PATH = state/checkpoints/CHECKPOINT_0006_CONTINUITY_SYNC.md
CHECKPOINT_COMMIT = 51a66f08e03a2269ee62c1ac97aab34ad4425c78
CHECKPOINT_COMMIT_MESSAGE = Add Hephaestus continuity synchronization checkpoint
CHECKPOINT_COMMIT_VERIFIED = YES
CURRENT_POINTER_UPDATE_COMMIT = ae8ac94e1ddbffb4dd4313b31fe16703b8bb1e3e
CURRENT_POINTER_UPDATE_VERIFIED = YES
```

The new checkpoint does not alter the fact that checkpoint 0005 was the first verified Hephaestus self-save or that checkpoint 0004 was evaluator/admin-written.

## Terminology

Use:

- `ACCEPTED_REPOSITORY_STATE` for any canonical checkpoint accepted by governance.
- `EVALUATOR_ADMIN_SAVED_STATE` when the evaluator/admin wrote the checkpoint.
- `HEPHAESTUS_SELF_SAVED_STATE` only for a checkpoint actually written by a working Hephaestus chat and supported by a verified Git commit receipt.

A repository read is not a self-save. A generated checkpoint draft is not a self-save. A GitHub contents write without commit verification is not yet sufficient provenance for a verified self-save claim.

## Public/private boundary

This is a public repository. Self-save checkpoints must not contain private Vera records, private user history, credentials, confidential customer material, or other restricted information.