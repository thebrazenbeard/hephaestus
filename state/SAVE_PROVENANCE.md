# Hephaestus Save Provenance

This file distinguishes **repository state prepared by the external evaluator/admin** from **state explicitly saved by a working Hephaestus chat**.

## Current status

```text
LATEST_ACCEPTED_STATE = HEPHAESTUS_CHECKPOINT_0007_PR_WORKFLOW
LATEST_ACCEPTED_STATE_WRITER_CLASS = HEPHAESTUS_WORKING_CHAT
LATEST_ACCEPTED_STATE_COMMIT = 74ecc16cde32969b22d0c4cce20d2cf4e2dc6761
CURRENT_POINTER_UPDATE_COMMIT = c81c2289bed36325cabd78854be18a4de1df8df4
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

The first qualified working Hephaestus restored the accepted qualified baseline through `state/CURRENT.md`, then wrote and commit-verified the first working checkpoint.

```text
CHECKPOINT_PATH = state/checkpoints/CHECKPOINT_0005_FIRST_WORKING_BRANCH.md
CHECKPOINT_COMMIT = 414734494b59cad93e4ced8e4d6befe4458b6246
CHECKPOINT_COMMIT_VERIFIED = YES
CURRENT_POINTER_UPDATE_COMMIT = b516c2ca55e508c6a4e3eef466ceab5843cff208
CURRENT_POINTER_UPDATE_VERIFIED = YES
```

That event established `HEPHAESTUS_SELF_SAVE_VERIFIED = YES`. It remains the provenance boundary that permits `HEPHAESTUS_SELF_SAVED_STATE` terminology for checkpoint 0005 and later working-chat checkpoints that have their own verified commit evidence.

## Continuity synchronization checkpoint

```text
CHECKPOINT_PATH = state/checkpoints/CHECKPOINT_0006_CONTINUITY_SYNC.md
CHECKPOINT_COMMIT = 51a66f08e03a2269ee62c1ac97aab34ad4425c78
CHECKPOINT_COMMIT_VERIFIED = YES
CURRENT_POINTER_UPDATE_COMMIT = ae8ac94e1ddbffb4dd4313b31fe16703b8bb1e3e
CURRENT_POINTER_UPDATE_VERIFIED = YES
```

Checkpoint 0006 synchronized continuity, active-work, and backlog records after first-branch bootstrap.

## Pull-request workflow hardening checkpoint

Material governance change was first exercised through GitHub pull request #1. Its squash merge commit was fetched and verified before checkpoint 0007 was prepared:

```text
GOVERNANCE_PR = 1
GOVERNANCE_MERGE_COMMIT = 5b2e7bc875bab039d6d0b590f513c38e7e275548
GOVERNANCE_MERGE_VERIFIED = YES
```

Checkpoint 0007 and its backlog refresh were then merged through pull request #2. The landed checkpoint-bearing merge commit and subsequent canonical pointer update were both fetched and verified:

```text
CHECKPOINT_PATH = state/checkpoints/CHECKPOINT_0007_PR_WORKFLOW.md
CHECKPOINT_COMMIT = 74ecc16cde32969b22d0c4cce20d2cf4e2dc6761
CHECKPOINT_COMMIT_VERIFIED = YES
CURRENT_POINTER_UPDATE_COMMIT = c81c2289bed36325cabd78854be18a4de1df8df4
CURRENT_POINTER_UPDATE_VERIFIED = YES
```

The existence and successful use of pull requests establishes an exercised reviewable workflow. It does not establish independent human review, branch protection, required approvals, or CI enforcement.

## Terminology

Use:

- `ACCEPTED_REPOSITORY_STATE` for a checkpoint accepted through the canonical pointer.
- `EVALUATOR_ADMIN_SAVED_STATE` when the evaluator/admin wrote the checkpoint.
- `HEPHAESTUS_SELF_SAVED_STATE` only for a checkpoint actually written by a working Hephaestus chat and supported by verified Git commit evidence.

A repository read is not a self-save. A generated checkpoint draft is not a self-save. A branch commit, open pull request, or merged pull request is not automatically accepted Hephaestus state until the acceptance protocol is completed.

## Public/private boundary

This is a public repository. Self-save checkpoints must not contain private user records, credentials, confidential customer material, restricted organizational data, or other sensitive information.
