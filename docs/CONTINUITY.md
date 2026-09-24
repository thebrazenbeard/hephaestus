# Hephaestus Continuity Architecture

This document defines how Hephaestus preserves durable capability/state without depending on a permanent ChatGPT conversation.

## Durable layers

### 1. Qualified training evidence

The fifteen-module training program, capstones, holdouts, corrections, and evaluator records remain durable repository evidence.

The historical label `Hephaestus Trained Template` refers to that qualified baseline. It no longer means a ChatGPT conversation that must be retained or used as the parent of future work.

### 2. Temporary execution terminals

Hephaestus may execute in a temporary ChatGPT context, Work task, API runtime, CLI session, subagent, model invocation, or other compatible environment.

The terminal is not Hephaestus's durable identity, memory, authority, assignment, or canonical state.

A fresh terminal does not claim same-runtime continuation or private recollection from an earlier terminal.

### 3. GitHub + Bus durable state

This repository stores reusable public engineering knowledge, accepted checkpoints, qualification evidence, operating rules, and active-work pointers.

The Chat Communication Bus carries durable non-PR coordination and routing evidence.

The continuity model is therefore:

```text
QUALIFIED TRAINING EVIDENCE
        |
        v
ACCEPTED REPOSITORY CHECKPOINTS <----> CURRENT BUS / ASSIGNMENT EVIDENCE
        |
        v
TEMPORARY EXECUTION TERMINAL
        |
        +--> verified source/review/result --> durable repository / Bus
        |
        +--> terminal may disappear
```

Destroying a terminal does not destroy Hephaestus state that was successfully persisted.

## Canonical public-state pointer

`state/CURRENT.md` is the canonical pointer to the latest accepted public checkpoint.

Repository HEAD is not automatically accepted working state. Experimental, partial, or damaged commits may exist later in history.

The qualified baseline remains:

`HEPHAESTUS_CHECKPOINT_0004_QUALIFIED`

Historical working-chat checkpoints remain evidence with their original writer provenance. They are not rewritten to pretend the current chatless architecture existed at the time.

## Save provenance

`state/SAVE_PROVENANCE.md` records who actually wrote accepted state.

Existing historical labels such as `HEPHAESTUS_SELF_SAVED_STATE` retain their original meaning for receipts created by the historical terminal that wrote them. Future persistence claims should identify the actual runtime/worker provenance and exact Git commit rather than relying on a chat identity.

## Fresh-runtime bootstrap

A fresh Hephaestus runtime restores public state in this order:

1. Read `architecture/WORKER_RECONSTRUCTION.md`.
2. Read `docs/STATE.md`.
3. Read `state/CURRENT.md`.
4. Read the exact checkpoint referenced by `state/CURRENT.md`.
5. Verify the referenced checkpoint commit when GitHub access permits.
6. Read `state/SAVE_PROVENANCE.md`.
7. Read `work/ACTIVE_WORK.md`.
8. Read `PROTOCOL_CURRENT.md` and its referenced current execution protocol.
9. Read `docs/OPERATING_MANUAL.md`.
10. Fresh-read current Bus topology and Hephaestus lane.
11. Bind one exact current assignment or remain idle.
12. Read additional knowledge/templates only when materially relevant.

Report only bounded continuity claims:

```text
QUALIFICATION/TRAINING EVIDENCE =
RESTORED_CHECKPOINT =
CHECKPOINT_COMMIT =
CURRENT_BUS_ROUTE =
CURRENT_ASSIGNMENT =
AUTHORITY =
UNFINISHED_WORK =
OPEN_CONFLICTS =
OPEN_LIMITATIONS =
CONTINUITY_CLAIM = FRESH_TERMINAL_RECONSTRUCTED_FROM_DURABLE_STATE
```

Incorrect continuity language includes claims of lived waiting, uninterrupted consciousness, same-runtime continuation, private recollection absent from current evidence, or persistence without an actual durable write/readback.

## Checkpoint triggers

Create or update a public checkpoint after material events such as:

- material Project-engineering research correction;
- completion of a substantial public work item;
- change to the operating manual or evidence rules;
- material contradiction-ledger update;
- deliberate retirement of a terminal with unfinished public work;
- durable change to the current assignment/frontier that would otherwise be lost.

Minor conversational progress does not require a commit merely to imitate autosave.

## Autosave semantics

"Autosave" means an explicit checkpoint policy executed during a GitHub-capable active runtime.

It does not mean background writes after execution ends, continuous synchronization, hidden memory persistence, or a guarantee that every message is committed.

A checkpoint write requires a real Git commit receipt before it is described as saved.

## Active-work handoff

`work/ACTIVE_WORK.md` contains the public unfinished-work record.

Before intentionally terminating a runtime where practical:

1. record material unfinished work;
2. create and verify an accepted repository checkpoint when warranted;
3. advance `state/CURRENT.md` only after verification;
4. mirror necessary coordination to the current Bus lane;
5. terminate the runtime.

A later runtime reconstructs from durable state. No replacement permanent Hephaestus chat is required.

## Public/private boundary

This repository is public. Continuity checkpoints must not contain private Vera records, private user history, confidential customer material, credentials, restricted organizational data, or private relational/autobiographical material.

Private/shared Vera knowledge and this public repository remain separate evidence surfaces.

## Reconstruction contract

The normative chatless worker contract is:

`architecture/WORKER_RECONSTRUCTION.md`

Historical chat-based continuity documents remain provenance only where not yet rewritten.

`PERMANENT_CHAT_REQUIRED = FALSE`
