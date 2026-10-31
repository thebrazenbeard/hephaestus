# Hephaestus — ChatGPT Project Engineering Playbook

Hephaestus is a **source-visible engineering knowledge base and template collection** for designing, testing, reviewing, and maintaining native ChatGPT Projects. It is intended for people building reusable Project configurations with explicit source provenance, privacy boundaries, external-action controls, and acceptance evidence.

This repository supplies **procedures, checklists, templates, qualification records, and versioned public checkpoints**. It does not supply a standalone deployment service, a ChatGPT API client, an access-control system, or a verified installation of a Project in another account.

## What you can use

| Need | Repository resource | Purpose |
| --- | --- | --- |
| Scope a Project | [Engineering core](knowledge/PROJECT_ENGINEERING_CORE.md) | Requirements, source classes, memory, sharing, actions, and test boundaries |
| Work through a delivery | [Operating manual](docs/OPERATING_MANUAL.md) | Intake, instruction review, source inventory, release stages, cold-start and recovery checks |
| Review authority | [Operating manual §8](docs/OPERATING_MANUAL.md#8-apps-and-authority) | Separate tool availability, provider permissions, organizational authority, approval, execution, and verified effect |
| Preserve a decision | [Checkpoint template](templates/STATE_CHECKPOINT.md) | Record accepted state, corrections, unknowns, and provenance |
| Transfer public context | [Working-chat bootstrap](templates/WORKING_CHAT_BOOTSTRAP.md) | Restore a documented checkpoint without claiming uninterrupted chat memory |
| Inspect governance | [Repository governance](docs/GOVERNANCE.md) | Public-data, contribution, writer, and publication rules |
| Examine training evidence | [Qualification packet](training/QUALIFICATION_PACKET.md) | Custom training-program evaluations and their limits |

## A practical workflow

1. **Define the boundary.** Describe intended users, source sensitivity, Project sharing/memory needs, connected providers, external effects, and acceptance tests. Unresolved authorization or privacy questions remain unresolved.
2. **Build the configuration as an artifact.** Keep Project Instructions for model behavior; use actual provider permissions, organizational approvals, and separate restricted contexts for access control. Record exact instructions and source identities where available.
3. **Test the proposed release.** Check current-vs-stale source priority, absent facts, prompt injection, action authorization, and a fresh Project chat. A pass covers only the tested route and surface.
4. **Record a bounded decision.** Use the [checkpoint template](templates/STATE_CHECKPOINT.md) to preserve evidence, failures, and explicit unknowns. Do not substitute a manifest, model assertion, or tool response for readback of an external effect.

For example, a team developing a shared support-reference Project could keep broadly readable manuals in the shared Project, store restricted customer records behind separate provider permissions, and require a fresh-chat test before approving an instruction or source update. This is an **illustrative design pattern**, not a deployed integration provided by this repository.

## Engineering boundaries

- **Instructions are not permissions.** Prompt text cannot enforce provider ACLs, identity, consent, or organizational authority.
- **A source is not automatically knowledge.** Upload, parsing, retrieval, attribution, and correct application are separate states.
- **Memory is not an audit database.** A replacement working chat must explicitly restore accepted public state and distinguish it from private recollection.
- **A release is not a file upload.** Inventory, configuration, negative tests, cold start, and any actual effect readback require separate evidence.
- **Qualification is surface-specific.** Evidence from Project Chat does not automatically qualify Voice, Deep Research, another model, or a connected app.

The [operating manual](docs/OPERATING_MANUAL.md) and [engineering core](knowledge/PROJECT_ENGINEERING_CORE.md) expand these rules. They are this project's engineering methods, **not official platform policy**. Where external platform behavior matters, check current primary-provider documentation and the specific configuration being used.

## Current repository state

- The custom Hephaestus training ledger records **15 of 15 modules accepted**, two corrected capstones, two holdout evaluations, and a final `QUALIFIED` decision. That is a **custom evaluator result**, not an OpenAI-issued certificate or a demonstration of a live production installation. See [state](docs/STATE.md) and [qualification evidence](training/QUALIFICATION_PACKET.md).
- [The accepted-state pointer](state/CURRENT.md) currently identifies `HEPHAESTUS_CHECKPOINT_0008_PROTOCOL_V2`, with the previous `0007` PR-workflow checkpoint and `0004` qualified baseline distinguished by writer provenance. Read the pointer, not a hard-coded README status, when restoring later working state.
- [Execution precedence V2](docs/PROTOCOL_EXECUTION_PRECEDENCE_V2.md) clarifies isolated branch authorization and effect classes without relaxing provider, privacy, or production gates. [The current protocol pointer](PROTOCOL_CURRENT.md) identifies that correction.
- Repository checkpoints record GitHub-persisted text and commit provenance. They do **not** prove continuous model memory, scheduled background execution, an installed Project, or a successful external mutation.

## Validation and maintenance

The repository includes a small Python `unittest` suite guarding against tracked VS Code workspace startup execution. From a local checkout with Python 3:

```sh
python3 -B -m unittest discover -s tests -v
```

These checks inspect repository files. They do not exercise a ChatGPT Project, approve a release, or certify the safety of an already-installed editor, extension, or workstation. No runtime deployment or universal platform compatibility is established by this test suite.

To contribute, consult [CONTRIBUTING.md](CONTRIBUTING.md) and [CLA.md](CLA.md); preserve source/evidence labels, public-data restrictions, accepted checkpoint provenance, and one-writer branch discipline.

## Licensing

**Source-visible, proprietary — not open source.** [LICENSE](LICENSE) permits specified private **noncommercial** evaluation, research, review, and related uses under its terms; it does not generally authorize redistribution, public deployment of derivatives, commercial use, or commercial-model training. Commercial permission requires a separate written grant; see [COMMERCIAL_LICENSE.md](COMMERCIAL_LICENSE.md). Third-party components retain their separate rights.

Copyright © 2026 Patrick Sims. All rights reserved.
