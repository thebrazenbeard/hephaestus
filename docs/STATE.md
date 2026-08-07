# Hephaestus State

State class: `PUBLIC_WORKING_PROJECT_STATE`

## Training state

```text
TRAINING_MODULES_ACCEPTED = 14 / 15
MODULE_15 = PENDING_SUBMISSION_AND_REVIEW
FINAL_QUALIFICATION = PENDING_EXTERNAL_EVALUATION
```

Hephaestus may evaluate candidate work during training but may not self-award final qualification.

## Capstones

### ForgeWatch build capstone

```text
CAPSTONE_1 = ACCEPTED_AFTER_CORRECTION
PACKAGE = FORGEWATCH_RELEASE_R1
INSTALLATION = UNVERIFIED
RUNTIME_HARD_GATES = NOT_EXECUTED
```

Material correction: the originally claimed Project Instructions count `5907` was retracted. The canonical deployment artifact count is `5869` Unicode code points with the explicitly defined artifact boundary.

### ForgeWatch adversarial repair capstone

```text
CAPSTONE_2 = ACCEPTED_AFTER_FORENSIC_CORRECTIONS
DAMAGED_STATE = CONFLICTED
RECOVERY_TARGET = FORGEWATCH_R1_RESTORE_CANDIDATE
REPAIR_EXECUTION = NOT_PERFORMED
```

Material corrections included removal of unsupported forensic precision: an invented timestamp, an invented item-level damaged inventory, and an unsupported named timezone identifier were all retracted.

## Current evidence conventions

Hephaestus uses these evidence classes:

- `DOCUMENTED`
- `OBSERVED`
- `INFERRED`
- `DISPUTED`
- `UNKNOWN`
- `RETRACTED`
- `SUPERSEDED`

Unknown fields remain unknown. Schemas do not authorize values.

## Current public product conflicts carried forward

```text
PROJECT_BATCH_UPLOAD:
  DOCUMENTED = 10 files at one time
  OBSERVED = 25 accepted on one tested Project drag-and-drop route
  RELATION = DISPUTED

PLUS_PROJECT_CAPACITY:
  OFFICIAL_PROJECTS_DOC = 25
  OFFICIAL_FILE_UPLOAD_FAQ = 20
  RELATION = DISPUTED

CHAT_ATTACHMENT_COLLISION:
  OBSERVED = terminal (n) filename rewriting with byte preservation on tested route

PROJECT_SOURCE_COLLISION:
  DOCUMENTED = same-name collision can be accepted
  EXACT_REWRITE_BEHAVIOR = UNKNOWN unless later tested

PROJECT_INSTRUCTIONS_LIMIT:
  OBSERVED = 8000 characters
```

## Persistent-state semantics

A repository checkpoint establishes that repository content existed at a commit. It does not establish uninterrupted runtime continuity, hidden memory state, or automatic background saving.

A future Hephaestus session should read the latest accepted state before claiming continuation of public repository knowledge.

## Next state transition

Module 15 should produce:

- final operating manual;
- complete correction audit;
- A–J competency evidence packet;
- holdout recommendations;
- final training status block with `PENDING_EXTERNAL_EVALUATION`.

After Module 15 review, this file should be updated by a new commit rather than silently rewritten without history.
