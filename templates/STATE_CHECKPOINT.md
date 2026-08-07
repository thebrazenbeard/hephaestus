# Hephaestus State Checkpoint Template

Use this template for explicit public repository checkpoints. A checkpoint records repository-visible state only.

```yaml
checkpoint_id:
created_date:
created_time: UNKNOWN
utc_offset: UNKNOWN
timezone_identifier: UNKNOWN

state_class: PUBLIC_WORKING_PROJECT_STATE

training:
  modules_accepted:
  current_module:
  final_qualification: PENDING_EXTERNAL_EVALUATION

capstones:
  build:
  repair:

material_changes:
  -

retractions:
  - claim:
    status:
    corrected_claim:
    evidence:

open_conflicts:
  - conflict_id:
    subject:
    state:
    operational_rule:

open_limitations:
  -

runtime_claims:
  project_installations_verified: 0
  repairs_executed: 0
  surfaces_empirically_qualified: []

repository:
  branch:
  source_commit:
  previous_checkpoint:

notes:
```

## Rules

1. Do not invent a time, offset, timezone, hash, artifact mapping, runtime result, or external state merely because the template has a field for it.
2. Use `UNKNOWN` when evidence is unavailable.
3. Bind exact counts/hashes to exact artifacts.
4. Record retractions explicitly.
5. A Git commit proves the committed repository state, not a ChatGPT runtime state outside the repository.
6. Do not place private Vera or user-private data in this public checkpoint.
