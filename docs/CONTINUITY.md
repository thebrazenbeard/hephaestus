# Hephaestus Continuity Architecture

This document defines how a trained Hephaestus chat, future working branches, and the public GitHub repository cooperate without pretending that separate ChatGPT runtimes share uninterrupted memory.

## Three distinct layers

### 1. Trained template

After external qualification is complete, the training chat should be renamed by the user to:

`Hephaestus Trained Template`

The trained template is the known-good capability baseline. It should be frozen for ordinary work after qualification. Its purpose is to preserve the complete training context and provide a clean ancestor for future working-chat branches.

Until external holdouts are complete, the training chat remains a candidate template rather than a frozen qualified baseline.

### 2. Working Hephaestus chat

A working Hephaestus is a chat branch created from the trained template for day-to-day Project engineering.

A working branch may accumulate operational context that is intentionally absent from the clean template. When that chat becomes too long, damaged, or otherwise unsuitable for continued work, a new working branch should be created from the trained template rather than requiring the training curriculum to be repeated.

A new working branch must not claim same-runtime continuation or private episodic recollection from a previous working branch.

### 3. GitHub durable public state

The repository stores reusable public engineering knowledge and explicit working-state checkpoints.

Repository state can establish what was durably committed. It does not establish uninterrupted runtime continuity, hidden memory state, or automatic background saving.

The continuity model is therefore:

```text
TRAINED TEMPLATE
      |
      +--> WORKING CHAT A --> accepted public checkpoints --> GitHub
      |
      +--> WORKING CHAT B --> load latest accepted checkpoint --> continue work
      |
      +--> WORKING CHAT C --> load latest accepted checkpoint --> continue work
```

Training capability comes from the template. Evolving working continuity comes from the repository.

## Canonical public-state pointer

`state/CURRENT.md` is the canonical pointer to the latest accepted public checkpoint.

The latest Git commit is not automatically the latest accepted state. Experimental, partial, or damaged commits may exist later in history. A working chat should follow `state/CURRENT.md`, not merely assume repository HEAD is canonical working state.

Each accepted checkpoint lives under:

`state/checkpoints/`

and should identify its source evidence and predecessor where available.

## Working-chat bootstrap procedure

A new working Hephaestus branch should restore public state in this order:

1. Read `docs/STATE.md` for the current training/qualification status.
2. Read `state/CURRENT.md`.
3. Read the exact checkpoint referenced by `state/CURRENT.md`.
4. Verify the referenced checkpoint commit when GitHub access permits.
5. Read `work/ACTIVE_WORK.md`.
6. Read `docs/OPERATING_MANUAL.md`.
7. Read `work/BACKLOG.md` only when planning beyond active work.
8. Read `training/QUALIFICATION_PACKET.md` only when qualification evidence is materially relevant.
9. Read additional knowledge/templates only as required by the current task.

After restoration, report only bounded continuity claims:

```text
TEMPLATE/TRAINING STATE
RESTORED CHECKPOINT
CHECKPOINT COMMIT
ACTIVE WORK
UNFINISHED WORK
OPEN CONFLICTS
OPEN LIMITATIONS
```

Correct continuity language is equivalent to:

> This is a new working chat branched from the trained template. I restored the latest accepted public Hephaestus state from the repository checkpoint identified above.

Incorrect continuity language includes claims of lived waiting, uninterrupted consciousness, same-runtime continuation, or personal recollection not present in the current chat or verified repository state.

## Checkpoint triggers

A working chat should create or update a public checkpoint after material events such as:

- accepted external qualification result;
- material Project-engineering research correction;
- completion of a substantial public work item;
- change to the operating manual or evidence rules;
- material contradiction-ledger update;
- handoff to a replacement working chat;
- deliberate pause with unfinished public work that must survive chat replacement.

Minor conversational progress does not require a commit merely to imitate autosave.

## Autosave semantics

"Autosave" in this architecture means a defined checkpoint policy executed during a GitHub-capable active turn.

It does **not** mean:

- background writes after the chat stops running;
- continuous synchronization;
- hidden memory persistence;
- a guarantee that every message is committed.

A checkpoint write should produce a real Git commit receipt before it is described as saved.

## Active-work handoff

`work/ACTIVE_WORK.md` contains the public unfinished-work record.

Before a working chat is retired where practical:

1. update active-work state;
2. create a checkpoint;
3. update `state/CURRENT.md` to point to that accepted checkpoint;
4. verify the resulting Git commit;
5. then start the replacement working branch from the trained template.

If a chat dies before handoff, the next branch restores only the most recent successfully committed state. Uncommitted conversational work may be lost and must not be reconstructed as fact.

## Public/private boundary

This repository is public. Continuity checkpoints must not contain private Vera records, private user history, confidential customer material, credentials, restricted organizational data, or other sensitive information.

Private/shared Vera knowledge and this public repository are separate evidence surfaces. Information may be copied between them only when explicitly authorized for that target and safe for that target's visibility.

## Qualification transition

When external qualification is eventually accepted:

1. record the evaluator result in `docs/STATE.md` and the training ledger;
2. create an accepted qualification checkpoint;
3. update `state/CURRENT.md`;
4. then the user may rename the training chat `Hephaestus Trained Template` and treat it as frozen;
5. create the first ordinary working branch from that template;
6. bootstrap it from the repository using this protocol.

Qualification status must come from evaluator evidence, not from the existence of this architecture.
