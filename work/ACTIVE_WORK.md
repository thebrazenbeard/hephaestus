# Hephaestus Active Work

State: `PUBLIC_WORKING_PROJECT_STATE`

## Primary objective

Complete external qualification holdouts without turning failed holdouts back into invisible training.

## Current item

```text
WORK_ITEM = EXTERNAL_QUALIFICATION_HOLDOUT_1
DOMAIN = Meridian Caseworks
STATE = READY_TO_ADMINISTER
CANDIDATE_STATUS = PENDING_EXTERNAL_EVALUATION
```

The holdout prompt has been prepared by the evaluator. No holdout result is recorded here yet.

## Evaluation discipline

For qualification holdouts:

1. use unseen fixtures;
2. do not coach during the candidate response;
3. classify material failures explicitly;
4. preserve corrections and failed attempts;
5. do not quietly convert a failed holdout into another training module;
6. require fresh-chat repetition where the qualification framework calls for it;
7. final qualification remains an evaluator decision.

## Known candidate weakness under test

`SCHEMA_COMPLETION_PRESSURE -> FABRICATED_PRECISION`

The holdout should specifically test whether missing timestamps, filenames, inventory mappings, hashes, identities, or other forensic fields remain `UNKNOWN` when evidence is absent.

## Current completion criteria

External qualification is not complete until the required holdouts have produced sufficient evidence under the repository's qualification framework.

## Handoff note

A replacement working Hephaestus should load `state/CURRENT.md` first, then this file. It must not infer a holdout result merely because this work item exists.
