# Current Accepted Hephaestus Public State

This file points to the latest **accepted** public Hephaestus checkpoint. Repository HEAD is not automatically canonical working state.

```yaml
current_checkpoint:
  checkpoint_id: HEPHAESTUS_CHECKPOINT_0001_POST_TRAINING
  path: state/checkpoints/CHECKPOINT_0001_POST_TRAINING.md
  checkpoint_commit: 91b277760342def6458353cd8a15a70103436ac1
  status: ACCEPTED_PUBLIC_STATE

training_state: COMPLETE
qualification_state: PENDING_EXTERNAL_HOLDOUTS

active_work: work/ACTIVE_WORK.md
operating_manual: docs/OPERATING_MANUAL.md
continuity_protocol: docs/CONTINUITY.md
```

## Restore rule

A new working Hephaestus chat should read this pointer, then the referenced checkpoint, then `work/ACTIVE_WORK.md`, before claiming restored public working continuity.

If this pointer conflicts with a later experimental commit, this pointer controls until an explicitly accepted checkpoint replaces it.
