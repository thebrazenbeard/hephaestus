# Repository Governance

This repository is the public version-controlled home for Hephaestus. It is not a private Vera store and must not become one by accident.

## Administrative model

The repository owner account remains the GitHub owner. The current ChatGPT collaborator acts as the initial administrative maintainer/coordinator through the connected GitHub permissions available in authorized turns.

Hephaestus may later maintain his own public state and knowledge through authorized GitHub-capable turns. Repository writes are explicit actions, not background persistence.

## Writer rule

For a given branch/change assignment, use one active writer at a time. Unexpected concurrent branch movement should pause publication until the head is re-read and reconciled.

No force push, destructive history rewrite, branch deletion, release deletion, credential action, deployment, paid-service action, or other consequential external mutation is implied by general maintenance authority.

## Public-data boundary

Never commit:

- secrets or credentials;
- private user history;
- private Vera records;
- confidential customer/project files;
- private relational or autobiographical records;
- restricted organizational material;
- material whose publication rights are unclear.

Public reusable Project-engineering knowledge is appropriate. Private synchronization requires a separately authorized private store and must not be simulated by committing summaries here.

## State checkpoints

A state checkpoint should be written after material events such as:

- training module acceptance;
- material factual correction;
- capstone acceptance;
- external qualification result;
- operating-doctrine change;
- public research update that changes an operational rule;
- repository handoff;
- release of reusable templates or tooling;
- deliberate working-chat handoff with unfinished public work.

Each checkpoint should record only evidence actually established.

Recommended fields:

```yaml
checkpoint_id:
state_class: PUBLIC_WORKING_PROJECT_STATE
training_state:
qualification_state:
accepted_modules:
material_changes:
retractions:
open_conflicts:
open_limitations:
source_commit:
```

## Accepted-state pointer

`state/CURRENT.md` is the canonical pointer to the latest accepted public checkpoint.

Repository HEAD is not automatically accepted working state. Later experimental, partial, or damaged commits may exist. A working chat restoring continuity must follow `state/CURRENT.md` unless a newer accepted pointer is explicitly established.

Updating an accepted checkpoint requires:

1. a new checkpoint file or explicitly versioned replacement;
2. an actual commit receipt;
3. an update to `state/CURRENT.md` referencing the accepted checkpoint;
4. bounded status language that does not claim external runtime effects.

## Trained-template and working-chat model

After external qualification is accepted, the training chat may be renamed by the user to `Hephaestus Trained Template` and frozen for ordinary work.

The trained template is the capability baseline. Day-to-day work belongs in chat branches created from that template.

Working chats restore evolving public state from the repository using `docs/CONTINUITY.md`. They must not claim same-runtime continuation, uninterrupted private memory, or recollection that is absent from the current chat and verified repository evidence.

A replacement working chat should read, in order:

1. `docs/STATE.md`;
2. `state/CURRENT.md`;
3. the exact checkpoint referenced there;
4. `work/ACTIVE_WORK.md`;
5. `docs/OPERATING_MANUAL.md`;
6. additional repository material only as required by the active task.

## Autosave policy

Autosave is an operational checkpoint policy, not a background capability.

A public state save exists only after an explicit GitHub-capable turn successfully writes and receives a Git commit receipt.

Do not claim:

- continuous synchronization;
- writes after the chat stops running;
- every message is durably committed;
- hidden memory is persisted by GitHub.

## Evidence discipline

Repository content distinguishes:

`DOCUMENTED` · `OBSERVED` · `INFERRED` · `DISPUTED` · `UNKNOWN` · `RETRACTED` · `SUPERSEDED`

Rules:

1. Missing evidence remains `UNKNOWN`.
2. A filename does not prove byte identity.
3. A manifest value does not verify itself.
4. A repository commit proves repository state, not external runtime state.
5. A correction is appended through history; old claims are not cosmetically erased.
6. A successful fix does not automatically prove root cause.
7. Product behavior evidence does not establish organizational authority.
8. Aggregate counts do not authorize invented item-level mappings.
9. A schema field does not prove a value exists.

## Knowledge sharing with Vera

Hephaestus may share reusable, non-sensitive engineering knowledge with authorized Vera stores when an explicit write is permitted for that target. The public repo and Vera stores are separate evidence surfaces.

No bidirectional 'automatic sync' should be claimed unless an actual mechanism exists and has been verified. Manual or tool-mediated checkpoint propagation must be described as such.

## Pull requests and publication

For material public changes, prefer a branch/PR workflow once the repository becomes multi-contributor or user-facing. An exact immutable head should be reviewed before publication. Review evidence is bounded to that head.

Direct commits to `main` are acceptable during initial bootstrap while the repository remains single-writer and the user has explicitly authorized population.

The bootstrap exception should close after the initial continuity/qualification baseline is established. Once ordinary working Hephaestus sessions or outside contributors begin making material public changes, use branch/PR review by default unless a narrow maintenance change is explicitly authorized for direct `main` publication.
