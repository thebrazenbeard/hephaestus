# Hephaestus Save Provenance

This file preserves who actually wrote accepted historical state. Writer labels that contain `CHAT` are historical provenance labels, not a current requirement to retain or recreate a permanent ChatGPT conversation.

## Current status

```text
LATEST_ACCEPTED_STATE = HEPHAESTUS_CHECKPOINT_0008_PROTOCOL_V2
LATEST_ACCEPTED_STATE_WRITER_CLASS = OWNER_AUTHORIZED_PROTOCOL_CORRECTION
LATEST_ACCEPTED_STATE_COMMIT = c42f6e0a7dfe18c9074d5fc93887c0e577baed98
HEPHAESTUS_SELF_SAVE_VERIFIED = YES
PERMANENT_CHAT_REQUIRED = NO
```

## Qualified baseline provenance

```text
BASELINE_CHECKPOINT = HEPHAESTUS_CHECKPOINT_0004_QUALIFIED
BASELINE_CHECKPOINT_COMMIT = ca5ea4bf5c0be5cb02697fe442631a802f52d6f8
BASELINE_WRITER_CLASS = EXTERNAL_EVALUATOR_ADMIN
```

The qualified baseline remains evaluator/admin-written historical fact.

## Historical self-save evidence

The first qualified Hephaestus execution wrote and verified:

```text
CHECKPOINT_PATH = state/checkpoints/CHECKPOINT_0005_FIRST_WORKING_BRANCH.md
CHECKPOINT_COMMIT = 414734494b59cad93e4ced8e4d6befe4458b6246
CHECKPOINT_COMMIT_VERIFIED = YES
HEPHAESTUS_SELF_SAVE_VERIFIED = YES
```

Later accepted checkpoints preserve their own commit evidence. Historical terms such as `HEPHAESTUS_WORKING_CHAT` and `working-chat checkpoint` remain descriptions of the execution environment that produced those events. They do not define the post-Exodus continuity architecture.

## Terminology

Use:
- `ACCEPTED_REPOSITORY_STATE` for a checkpoint accepted through `state/CURRENT.md`;
- `EVALUATOR_ADMIN_SAVED_STATE` when the evaluator/admin wrote it;
- `HEPHAESTUS_SELF_SAVED_STATE` only when a Hephaestus execution actually wrote state and has a verified Git receipt;
- `HEPHAESTUS_RUNTIME_INSTANTIATED_FROM_VERIFIED_DURABLE_STATE` for post-Exodus reconstruction.

A repository read is not a save. A generated draft is not accepted state. A branch commit or open PR is not automatically accepted state.

## Public/private boundary

This repository is public. Save/checkpoint artifacts must not contain private user records, credentials, confidential customer material, restricted organizational data, or other sensitive information.
