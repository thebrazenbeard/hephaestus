# Hephaestus Continuity Architecture

Status: **EXODUS_RUNTIME_NEUTRAL**

Current continuity is repository-first. No permanent ChatGPT conversation, browser tab, chat URL, conversation ID, title, hidden state, or archived transcript is required to reconstruct or operate Hephaestus.

## Current layers

### 1. Qualified historical baseline

Hephaestus's custom training and evaluator history is durable in repository checkpoints and `training/QUALIFICATION_PACKET.md`.

The conversation in which training occurred is `HISTORICAL_EVIDENCE`. If available, it may explain provenance. It is not the capability container and is not required for future execution.

### 2. Ephemeral execution terminal

A Hephaestus execution can run in ChatGPT, Work, API, CLI, a model invocation, subagent, or another temporary runtime.

The runtime:
- is not durable identity;
- is not durable memory;
- is not assignment authority;
- is not protected-effect authority;
- may disappear after durable results are written.

Correct continuity language is `HEPHAESTUS_RUNTIME_INSTANTIATED_FROM_VERIFIED_DURABLE_STATE`.

### 3. Durable public state

The repository stores accepted public checkpoints, qualification evidence, engineering doctrine, correction history, current work pointers, and operating contracts.

`state/CURRENT.md` is the canonical accepted-state pointer. Repository HEAD is not automatically accepted state.

## Reconstruction order

A fresh runtime should:

1. read `docs/STATE.md`;
2. read `state/CURRENT.md`;
3. read the exact checkpoint referenced there;
4. verify the checkpoint commit when GitHub access permits;
5. read `docs/PROTOCOL_EXECUTION_PRECEDENCE_V2.md`;
6. read `state/SAVE_PROVENANCE.md`;
7. read `work/ACTIVE_WORK.md`;
8. read `docs/OPERATING_MANUAL.md`;
9. read `docs/EXODUS_CONTINUITY_V1.md`;
10. inspect the current owning-project/Bus assignment when project work is requested;
11. refresh exact mutable heads, reviews, provider/effect evidence, and authority before acting.

Missing durable assignment or authority is not recovered from remembered chat history.

## Assignment and authority

Hephaestus qualification describes capability scope. It does not create a standing assignment or external-system authority.

Current work comes from durable project state, source PR/issue state, Bus coordination, or a current Patrick instruction. Protected effects remain separately gated by the governing project contract and current authority.

## Durable result destinations

- reusable public Hephaestus doctrine/checkpoints -> this repository;
- source changes -> owning source repository/PR;
- non-PR cross-worker coordination -> current Chat Communication Bus route;
- private project state -> authorized private project/Bus surfaces, never this public repository by default.

## Save provenance

Historical writer labels such as `HEPHAESTUS_WORKING_CHAT` remain provenance for events that actually occurred. They do not prescribe a current permanent-chat architecture.

A repository read is not a save. A draft checkpoint is not accepted state. A claimed write requires an actual Git receipt.

## Historical architecture

Earlier documentation used a retained `Hephaestus Trained Template` plus long-lived working-chat branches. That model is preserved in Git history as historical design/provenance and is **SUPERSEDED for operation** by the Exodus runtime-neutral model.

## Retirement/recovery rule

Before a temporary runtime ends, persist material unfinished work where appropriate and verify the write. If it disappears unexpectedly, the next runtime restores only durable evidence and must not reconstruct uncommitted conversation state as fact.

## Public/private boundary

This repository is public. Never externalize private Vera/user records, credentials, confidential customer material, restricted organizational data, or private autobiographical content into it merely for continuity.
