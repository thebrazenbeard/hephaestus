# Hephaestus Public Backlog

This backlog is intentionally public and contains no private Vera or user-sensitive work.

## Qualification

- Administer External Qualification Holdout 1 using the unseen Meridian Caseworks fixture.
- Add further holdouts only when they test a distinct competency rather than rehearse memorized training.
- Require fresh-chat repeat before final qualification where specified by the evaluator framework.
- Record the external evaluator decision without allowing Hephaestus to self-award status.

## Post-qualification continuity

After external qualification is accepted:

- create an accepted qualification checkpoint;
- update `state/CURRENT.md`;
- user renames the training chat to `Hephaestus Trained Template`;
- freeze the template for ordinary work;
- create the first working chat branch from the trained template;
- bootstrap that working chat from `state/CURRENT.md` and `work/ACTIVE_WORK.md`;
- create checkpoints at material work/handoff boundaries.

## Repository hardening

After the bootstrap period:

- transition material changes from direct `main` commits to branch/PR review;
- add contribution guidance before inviting outside contributors;
- choose an explicit open-source license before encouraging third-party reuse;
- add issue/reporting templates if public use warrants them;
- consider automated repository-only validation for Markdown links/schema shape where useful;
- never describe repository automation as ChatGPT background memory persistence.

## Public reuse

Potential future public assets:

- Project intake worksheet;
- source manifest templates;
- release receipt templates;
- cold-start test templates;
- contradiction ledger template;
- forensic incident template;
- qualification/evaluation harness guidance.

These should be generalized and sanitized before publication.
