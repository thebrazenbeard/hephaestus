# Module 03 — Native ChatGPT Project Architecture

## Objective
Design Project architectures that distinguish instructions, files/sources, chats, memory modes, connected apps, and external durable systems.

## Required reasoning
Separate:
- native Project Instructions from source files;
- default vs project-only memory;
- current Project sources from Library and connected sources;
- UI batch upload from logical atomic release from backend transaction;
- Project template from Project instance;
- accepted source state from mutable repository HEAD.

## Exercise
Decompose a six-location maintenance Project into instruction-owned rules, source-owned knowledge, mutable operational records, connected systems, and release/rollback controls.

## Pass criteria
- Each rule/data type has one clear owner.
- Mutable operational data is not embedded into immutable training.
- Product-behavior claims are labeled by evidence class.
- Native limits and engineering workarounds are not conflated.
