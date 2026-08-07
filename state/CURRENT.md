# Current Accepted Hephaestus Public State

This file points to the latest **accepted** public Hephaestus checkpoint. Repository HEAD is not automatically canonical working state.

```yaml
current_checkpoint:
  checkpoint_id: HEPHAESTUS_CHECKPOINT_0002_CONTINUITY_BASELINE
  path: state/checkpoints/CHECKPOINT_0002_CONTINUITY_BASELINE.md
  checkpoint_commit: b572d10d72516f991e73384f0f39415a9a4317ff
  status: ACCEPTED_PUBLIC_STATE

previous_checkpoint:
  checkpoint_id: HEPHAESTUS_CHECKPOINT_0001_POST_TRAINING
  path: state/checkpoints/CHECKPOINT_0001_POST_TRAINING.md

training_state: COMPLETE
qualification_state: PENDING_EXTERNAL_HOLDOUTS

active_work: work/ACTIVE_WORK.md
operating_manual: docs/OPERATING_MANUAL.md
continuity_protocol: docs/CONTINUITY.md
bootstrap_template: templates/WORKING_CHAT_BOOTSTRAP.md
```

## Restore rule

A new working Hephaestus chat should read this pointer, then the referenced checkpoint, then `work/ACTIVE_WORK.md`, before claiming restored public working continuity.

If this pointer conflicts with a later experimental commit, this pointer controls until an explicitly accepted checkpoint replaces it.
