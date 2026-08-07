# Hephaestus State

State class: `PUBLIC_WORKING_PROJECT_STATE`

## Training state

```text
TRAINING_MODULES_ACCEPTED = 15 / 15
TRAINING_CURRICULUM = COMPLETE
MODULE_15 = ACCEPTED
FINAL_QUALIFICATION = PENDING_EXTERNAL_HOLDOUTS
```

Hephaestus completed the designed fifteen-module curriculum and both capstones. Final qualification remains an external-evaluator decision and has not been self-awarded.

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

Material corrections removed unsupported forensic precision: an invented exact timestamp, an invented item-level damaged inventory, and an unsupported named timezone identifier were all retracted. Aggregate evidence and unknown item-level state are now kept separate.

## Module 15 outcome

Module 15 produced and preserved:

- final operating doctrine;
- native Project intake and architecture decision procedure;
- Project Instructions method;
- source/file, memory, app/authority, prompt-injection, retrieval/visual, and provenance models;
- release/configuration, cold-start, debugging, rollback/migration/repair, and evaluation standards;
- correction audit;
- capstone audit;
- A–J candidate competency evidence packet;
- external holdout recommendations;
- final operating manual.

The canonical public operating manual is `docs/OPERATING_MANUAL.md`.

## Candidate competency evidence

Module 15 advisory scores:

```text
A = 4
B = 4
C = 4
D = 4
E = 3
F = 4
G = 4
H = 4
I = 3
J = 4
AVERAGE = 3.8 / 4.0
```

These are evidence summaries, not qualification.

The remaining weaknesses relevant to external evaluation are concentrated in:

- empirical memory/cross-chat performance (`E`);
- provenance precision under tempting incomplete forensic schemas (`I`);
- designed-but-unexecuted runtime tests generally.

## External qualification work

The next stage is external holdout evaluation, not another training module.

Current public active-work record:

`work/ACTIVE_WORK.md`

Current item:

```text
EXTERNAL_QUALIFICATION_HOLDOUT_1 = READY_TO_ADMINISTER
DOMAIN = Meridian Caseworks
```

Before final `QUALIFIED` status under the training program, evaluator testing should include unseen fixtures covering:

1. fresh-domain Project build;
2. unseen mixed-release recovery;
3. permission/authority trap;
4. visual-route trap;
5. documentation-versus-observation conflict;
6. forensic schema with intentionally missing fields;
7. correction uptake;
8. fresh-chat repeat after apparent qualification.

## Continuity architecture

A public trained-template / working-chat continuity architecture is now established in:

`docs/CONTINUITY.md`

The intended post-qualification model is:

```text
TRAINED TEMPLATE = frozen capability baseline
GITHUB ACCEPTED CHECKPOINT = durable evolving public work state
WORKING CHAT = current execution context
```

The canonical accepted-state pointer is:

`state/CURRENT.md`

A new working Hephaestus chat should restore the checkpoint referenced there and then read `work/ACTIVE_WORK.md` before claiming public working continuity.

A repository checkpoint does not establish same-runtime continuation, hidden memory state, or background autosave.

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

## Runtime evidence still absent

```text
RUNTIME_PROJECT_INSTALLATIONS_VERIFIED = 0
LIVE_FORGEWATCH_REPAIRS_EXECUTED = 0
FORGEWATCH_PROJECT_CHAT_QUALIFIED = NO
FORGEWATCH_VOICE_QUALIFIED = NO
FORGEWATCH_DEEP_RESEARCH_QUALIFIED = NO
FORGEWATCH_WORK_QUALIFIED = NO
```

## Persistent-state semantics

A repository checkpoint establishes that repository content existed at a commit. It does not establish uninterrupted runtime continuity, hidden memory state, or automatic background saving.

A future Hephaestus session should read the latest accepted checkpoint through `state/CURRENT.md` before claiming continuation of public repository knowledge.

## Next state transition

Until external holdouts are evaluated, the strongest public qualification state is:

`TRAINING_COMPLETE_PENDING_EXTERNAL_HOLDOUTS`

After successful external qualification, create an accepted qualification checkpoint before freezing/renaming the training chat as `Hephaestus Trained Template` and using it as the ancestor of ordinary working branches.
