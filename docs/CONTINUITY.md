# Hephaestus Continuity Architecture

This document defines how the qualified Hephaestus trained template, future working branches, and the public GitHub repository cooperate without pretending that separate ChatGPT runtimes share uninterrupted memory.

## Three distinct layers

### 1. Qualified trained template

External qualification is complete.

The training chat should now be renamed by the user to:

`Hephaestus Trained Template`

and frozen for ordinary operational work.

The trained template is the known-good capability baseline. Its purpose is to preserve the complete training and qualification context and provide a clean ancestor for future working-chat branches.

Do not accumulate ordinary day-to-day Project work in the template.

### 2. Working Hephaestus chat

A working Hephaestus is a chat branch created from the qualified trained template for day-to-day Project engineering.

A working branch may accumulate operational context intentionally absent from the clean template. When that chat becomes too long, damaged, or otherwise unsuitable, create a new working branch from the trained template rather than repeating the training curriculum.

A new working branch must not claim same-runtime continuation or private episodic recollection from a previous working branch.

### 3. GitHub durable public state

The repository stores reusable public engineering knowledge and explicit accepted working-state checkpoints.

Repository state can establish what was durably committed. It does not establish uninterrupted runtime continuity, hidden memory state, or automatic background saving.

The continuity model is:

```text
HEPHAESTUS TRAINED TEMPLATE
      |
      +--> WORKING CHAT A --> accepted public checkpoints --> GitHub
      |
      +--> WORKING CHAT B --> load latest accepted checkpoint --> continue work
      |
      +--> WORKING CHAT C --> load latest accepted checkpoint --> continue work
```

Training capability comes from the template. Evolving working continuity comes from the repository.

## Save provenance

`state/SAVE_PROVENANCE.md` records who actually wrote accepted state.

The qualified baseline `HEPHAESTUS_CHECKPOINT_0004_QUALIFIED` was written by the external evaluator/admin from accepted training and holdout evidence.

Therefore, at the qualified-template transition:

```text
ACCEPTED_REPOSITORY_STATE = YES
HEPHAESTUS_SELF_SAVE_VERIFIED = NO
```

Do not call the current baseline a "state Hephaestus saved." Until a working Hephaestus performs and verifies its own GitHub write, call it the **latest accepted Hephaestus repository state**.

The first working branch must perform a self-save verification before `HEPHAESTUS_SELF_SAVED_STATE` language is permitted.

## Canonical public-state pointer

`state/CURRENT.md` is the canonical pointer to the latest accepted public checkpoint.

Repository HEAD is not automatically the latest accepted state. Experimental, partial, or damaged commits may exist later in history. A working chat follows `state/CURRENT.md` rather than assuming HEAD is canonical working state.

Each accepted checkpoint lives under `state/checkpoints/`.

The qualified template baseline is:

`HEPHAESTUS_CHECKPOINT_0004_QUALIFIED`

## Working-chat bootstrap procedure

A newly branched working Hephaestus restores public state in this order:

1. Read `docs/STATE.md`.
2. Read `state/CURRENT.md`.
3. Read the exact checkpoint referenced by `state/CURRENT.md`.
4. Verify the referenced checkpoint commit when GitHub access permits.
5. Read `state/SAVE_PROVENANCE.md`.
6. Read `work/ACTIVE_WORK.md`.
7. Read `docs/OPERATING_MANUAL.md`.
8. Read `work/BACKLOG.md` when planning beyond active work.
9. Read `training/QUALIFICATION_PACKET.md` only when qualification evidence is materially relevant.
10. Read additional knowledge/templates only as required by the current task.

After restoration, report only bounded continuity claims:

```text
TEMPLATE/TRAINING STATE
RESTORED CHECKPOINT
CHECKPOINT COMMIT
SAVE PROVENANCE
ACTIVE WORK
UNFINISHED WORK
OPEN CONFLICTS
OPEN LIMITATIONS
```

Correct continuity language is equivalent to:

> This is a new working chat branched from the qualified trained template. I restored the latest accepted public Hephaestus repository state from the checkpoint identified above. The restored baseline's writer provenance is reported separately.

Incorrect continuity language includes claims of lived waiting, uninterrupted consciousness, same-runtime continuation, personal recollection not present in the current chat or verified repository state, or self-save provenance not established by an actual write receipt.

## Checkpoint triggers

A working chat should create or update a public checkpoint after material events such as:

- material Project-engineering research correction;
- completion of a substantial public work item;
- change to the operating manual or evidence rules;
- material contradiction-ledger update;
- handoff to a replacement working chat;
- deliberate pause with unfinished public work that must survive chat replacement.

Minor conversational progress does not require a commit merely to imitate autosave.

## Autosave semantics

"Autosave" means a defined checkpoint policy executed during a GitHub-capable active turn.

It does **not** mean:

- background writes after the chat stops running;
- continuous synchronization;
- hidden memory persistence;
- a guarantee that every message is committed.

A checkpoint write should produce a real Git commit receipt before it is described as saved.

## First working-branch self-save verification

Before ordinary work begins, the first qualified Working Hephaestus should:

1. restore `HEPHAESTUS_CHECKPOINT_0004_QUALIFIED` through `state/CURRENT.md`;
2. acknowledge `writer_class = EXTERNAL_EVALUATOR_ADMIN`;
3. create a new bounded working-state checkpoint in its own GitHub-capable turn;
4. verify the resulting commit receipt;
5. update `state/CURRENT.md` only after acceptance;
6. update `state/SAVE_PROVENANCE.md` to `HEPHAESTUS_SELF_SAVE_VERIFIED = YES` with the verified checkpoint and commit.

Until this succeeds, continuity works from evaluator/admin-prepared accepted state, but Hephaestus self-save capability remains unverified.

## Active-work handoff

`work/ACTIVE_WORK.md` contains the public unfinished-work record.

Before a working chat is retired where practical:

1. update active-work state;
2. create an accepted checkpoint;
3. update `state/CURRENT.md` to point to that checkpoint;
4. verify the resulting Git commit;
5. then start the replacement working branch from the trained template.

If a chat dies before handoff, the next branch restores only the most recent successfully committed state. Uncommitted conversational work may be lost and must not be reconstructed as fact.

## Public/private boundary

This repository is public. Continuity checkpoints must not contain private Vera records, private user history, confidential customer material, credentials, restricted organizational data, or other sensitive information.

Private/shared Vera knowledge and this public repository are separate evidence surfaces. Information may be copied between them only when explicitly authorized for that target and safe for that target's visibility.

## Qualified transition status

The qualification transition is complete on the repository side:

1. evaluator result recorded;
2. accepted qualification checkpoint created;
3. `state/CURRENT.md` advanced to the qualified checkpoint.

The remaining user-facing ChatGPT UI transition is:

1. rename the training chat `Hephaestus Trained Template`;
2. freeze it for ordinary work;
3. branch the first Working Hephaestus from it;
4. bootstrap that branch from `state/CURRENT.md` using `templates/WORKING_CHAT_BOOTSTRAP.md`;
5. run the first-working-branch self-save verification above before treating future state as Hephaestus-self-saved.
