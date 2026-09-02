# Current Accepted Hephaestus Public State

This file points to the latest **accepted** public Hephaestus checkpoint. Repository HEAD is not automatically canonical working state.

```yaml
current_checkpoint:
  checkpoint_id: HEPHAESTUS_CHECKPOINT_0008_PROTOCOL_V2
  path: state/checkpoints/CHECKPOINT_0008_PROTOCOL_V2.md
  checkpoint_commit: c42f6e0a7dfe18c9074d5fc93887c0e577baed98
  status: ACCEPTED_PUBLIC_STATE
  writer_class: OWNER_AUTHORIZED_PROTOCOL_CORRECTION

previous_checkpoint:
  checkpoint_id: HEPHAESTUS_CHECKPOINT_0007_PR_WORKFLOW
  path: state/checkpoints/CHECKPOINT_0007_PR_WORKFLOW.md
  checkpoint_commit: 74ecc16cde32969b22d0c4cce20d2cf4e2dc6761
  writer_class: HEPHAESTUS_WORKING_CHAT

qualified_baseline:
  checkpoint_id: HEPHAESTUS_CHECKPOINT_0004_QUALIFIED
  checkpoint_commit: ca5ea4bf5c0be5cb02697fe442631a802f52d6f8
  writer_class: EXTERNAL_EVALUATOR_ADMIN

training_state: COMPLETE
qualification_state: QUALIFIED

hephaestus_self_save_verified: YES
first_self_save_checkpoint: HEPHAESTUS_CHECKPOINT_0005_FIRST_WORKING_BRANCH
first_self_save_checkpoint_commit: 414734494b59cad93e4ced8e4d6befe4458b6246
save_provenance: state/SAVE_PROVENANCE.md

template_state: QUALIFIED_TRAINED_TEMPLATE_BASELINE
working_branch_state: ORDINARY_QUALIFIED_OPERATION

active_work: work/ACTIVE_WORK.md
backlog: work/BACKLOG.md
contribution_guidance: CONTRIBUTING.md
qualification_packet: training/QUALIFICATION_PACKET.md
holdout_1_evaluation: training/HOLDOUT_1_EVALUATION.md
holdout_2_evaluation: training/HOLDOUT_2_EVALUATION.md
operating_manual: docs/OPERATING_MANUAL.md
continuity_protocol: docs/CONTINUITY.md
current_execution_protocol: docs/PROTOCOL_EXECUTION_PRECEDENCE_V2.md
current_execution_pointer: PROTOCOL_CURRENT.md
bootstrap_template: templates/WORKING_CHAT_BOOTSTRAP.md
```

## Restore rule

A new working Hephaestus chat should read this pointer, then the referenced checkpoint, then `docs/PROTOCOL_EXECUTION_PRECEDENCE_V2.md`, then `state/SAVE_PROVENANCE.md`, then `work/ACTIVE_WORK.md`, before claiming restored public working continuity.

The qualified baseline `HEPHAESTUS_CHECKPOINT_0004_QUALIFIED` remains evaluator/admin-written historical provenance. `HEPHAESTUS_CHECKPOINT_0007_PR_WORKFLOW` remains historical evidence for the branch/PR workflow. `HEPHAESTUS_CHECKPOINT_0008_PROTOCOL_V2` is the current accepted operating correction and prevents that workflow from being over-read into redundant permission blocking.

If this pointer conflicts with a later experimental, merged, or housekeeping commit, this pointer controls until an explicitly accepted checkpoint replaces it.

## Qualification boundary

Hephaestus is `QUALIFIED` under the custom training-program evaluator framework. This does not claim live installation, repair, or surface qualification of the fictional capstone Projects.
