# Current Accepted Hephaestus Public State

This file points to the latest **accepted** public Hephaestus checkpoint. Repository HEAD is not automatically canonical working state.

```yaml
current_checkpoint:
  checkpoint_id: HEPHAESTUS_CHECKPOINT_0004_QUALIFIED
  path: state/checkpoints/CHECKPOINT_0004_QUALIFIED.md
  checkpoint_commit: ca5ea4bf5c0be5cb02697fe442631a802f52d6f8
  status: ACCEPTED_PUBLIC_STATE
  writer_class: EXTERNAL_EVALUATOR_ADMIN

previous_checkpoint:
  checkpoint_id: HEPHAESTUS_CHECKPOINT_0003_HOLDOUT1_PASS
  path: state/checkpoints/CHECKPOINT_0003_HOLDOUT1_PASS.md

training_state: COMPLETE
qualification_state: QUALIFIED

hephaestus_self_save_verified: NO
save_provenance: state/SAVE_PROVENANCE.md

template_state: READY_TO_FREEZE_AS_HEPHAESTUS_TRAINED_TEMPLATE
working_branch_state: READY_TO_CREATE_AFTER_TEMPLATE_FREEZE

active_work: work/ACTIVE_WORK.md
qualification_packet: training/QUALIFICATION_PACKET.md
holdout_1_evaluation: training/HOLDOUT_1_EVALUATION.md
holdout_2_evaluation: training/HOLDOUT_2_EVALUATION.md
operating_manual: docs/OPERATING_MANUAL.md
continuity_protocol: docs/CONTINUITY.md
bootstrap_template: templates/WORKING_CHAT_BOOTSTRAP.md
```

## Restore rule

A new working Hephaestus chat should read this pointer, then the referenced checkpoint, then `state/SAVE_PROVENANCE.md`, then `work/ACTIVE_WORK.md`, before claiming restored public working continuity.

The current qualified baseline is an accepted repository state written by the external evaluator/admin. It is **not yet evidence that Hephaestus itself has performed a repository self-save**.

If this pointer conflicts with a later experimental commit, this pointer controls until an explicitly accepted checkpoint replaces it.

## Qualification boundary

Hephaestus is `QUALIFIED` under the custom training-program evaluator framework. This does not claim live installation, repair, or surface qualification of the fictional capstone Projects.
