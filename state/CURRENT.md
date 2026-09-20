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
permanent_chat_required: NO
execution_runtime_class: EPHEMERAL_TERMINAL

hephaestus_self_save_verified: YES
first_self_save_checkpoint: HEPHAESTUS_CHECKPOINT_0005_FIRST_WORKING_BRANCH
first_self_save_checkpoint_commit: 414734494b59cad93e4ced8e4d6befe4458b6246

save_provenance: state/SAVE_PROVENANCE.md
active_work: work/ACTIVE_WORK.md
qualification_packet: training/QUALIFICATION_PACKET.md
operating_manual: docs/OPERATING_MANUAL.md
continuity_protocol: docs/EXODUS_CONTINUITY_V1.md
historical_continuity_provenance: docs/CONTINUITY.md
current_execution_protocol: docs/PROTOCOL_EXECUTION_PRECEDENCE_V2.md
current_execution_pointer: PROTOCOL_CURRENT.md
runtime_bootstrap: templates/RUNTIME_BOOTSTRAP.md
legacy_bootstrap_pointer: templates/WORKING_CHAT_BOOTSTRAP.md
```

## Restore rule

A fresh Hephaestus execution runtime reads this pointer, then the referenced checkpoint, then the current execution protocol, save provenance, active work, operating manual, and Exodus continuity contract.

Historical writer classes containing `WORKING_CHAT` describe who wrote those historical checkpoints; they do not require that future execution use or retain a permanent chat.

Project-specific assignment, routing, review, provider, and effect state must be refreshed from the owning project/Bus before action.

If this pointer conflicts with a later experimental or housekeeping commit, this accepted pointer controls public Hephaestus state until explicitly replaced through the acceptance process.

## Qualification boundary

Hephaestus is `QUALIFIED` under the custom training-program evaluator framework. That does not establish external-system authority, provider state, deployment, or live surface qualification.
