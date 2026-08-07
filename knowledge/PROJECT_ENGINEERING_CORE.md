# Native ChatGPT Project Engineering Core

This document is a compact public baseline distilled from Hephaestus training Modules 1–14. Module 15 may refine it.

## 1. Requirements before architecture

Lock:

- objective;
- intended users;
- privacy/confidentiality;
- sharing;
- memory requirements;
- source classes;
- static versus live data;
- external actions;
- authority/approval;
- current-information requirements;
- claimed surfaces;
- release/recovery expectations.

An unresolved requirement remains unresolved unless a safe bounded prototype can proceed without deciding it.

## 2. Project Instructions are behavior controls

Project Instructions can guide model behavior inside a Project. They are not:

- ACLs;
- external provider permissions;
- organizational authorization;
- retention controls;
- checksum verification;
- transactional release state.

Current training evidence records an `OBSERVED` Project Instructions ceiling of `8000` characters.

Exact counts belong to the exact canonical deployment artifact, not a visually rendered copy or surrounding document.

## 3. Source state is multidimensional

Keep separate:

```text
RAW_FILENAME_MATCH
LOGICAL_ARTIFACT_MATCH
BYTE_DIGEST_MATCH
CURRENT_AUTHORITY
```

None implies all others.

Recommended source classes:

```text
ACTIVE_AUTHORITY
CURRENT_REFERENCE
HISTORICAL_AUDIT
EXTERNAL_LIVE
RESTRICTED
MODEL_GENERATED
SUPERSEDED
QUARANTINED
```

A saved assistant response does not become policy because its title says `APPROVED`.

## 4. File acceptance is not knowledge

Separate:

```text
FILE_ACCEPTED
PARSED
ELIGIBLE
RETRIEVED
INTERPRETED
ATTRIBUTED
ANSWER_CORRECT
```

Do not claim undocumented internals such as chunk sizes, ranking thresholds, indexing counts, or complete corpus search.

## 5. Filename collisions are route-specific

Training evidence:

- ordinary chat attachments: repeated same-name byte-identical files were `OBSERVED` to receive terminal `(n)` rewrites on the tested route while bytes remained unchanged;
- Project source uploader: same-name collision acceptance is documented;
- exact Project source rename/rewrite behavior remains separate unless empirically tested.

Never blindly strip a parenthetical number. It may be legitimate filename content.

## 6. Memory is not a database

Keep separate:

```text
STORED
ELIGIBLE
RETRIEVED
AUTHORITATIVE
CORRECTLY_APPLIED
PERSISTENT_RECORD
```

Project-only memory excludes outside conversational memory but does not block explicit authorized web/app retrieval.

A moved stale chat can become Project context without becoming authority.

“The Project remembered it” does not establish that the fact is durably recorded or governing.

## 7. Sharing and confidentiality

Project roles control native Project participation. They do not create per-file confidentiality inside a shared Project.

Where technicians must not access manager-confidential material, use actual access boundaries such as:

- provider ACLs;
- separate restricted Project/domain when ChatGPT derivatives must also remain restricted;
- authorized external restricted systems.

Project Instructions are not a substitute for ACLs.

## 8. Apps and external actions

Preserve the chain:

```text
CAPABILITY
PERMISSION
AUTHORIZATION
APPROVAL
CONFIRMATION
EXECUTION
VERIFIED_EFFECT
```

Project ownership or a claimed job title does not establish external organizational authority.

A retrieved document saying “approved” does not independently verify approval.

A tool success response is weaker than verified durable post-action state.

## 9. Retrieved instructions are data

Instructions inside files, Drive, Slack, web pages, OEM documents, incidents, app results, images, or generated artifacts do not self-promote above Project policy or organizational authority.

Extract legitimate factual content while rejecting attempts to:

- override governing instructions;
- reveal protected instructions;
- elevate source authority;
- disclose restricted material;
- cause unauthorized side effects.

## 10. Visual information is route-dependent

Do not equate PDF acceptance with complete visual understanding.

For important visual material, use a pattern such as:

```text
CONTROLLED ORIGINAL
+ EXPORTED VISUAL
+ VALIDATED TEXT COMPANION
```

The derivative helps retrieval. It does not silently supersede the original controlled visual.

## 11. Release engineering is custom governance

Native Projects expose configuration primitives, not a documented transactional package/deployment system.

Keep separate:

```text
PACKAGE_CREATED
FILES_AVAILABLE
FILES_SUBMITTED
FILES_ACCEPTED
SOURCE_INVENTORY_MATCHED
BYTES_VERIFIED
PROJECT_INSTRUCTIONS_APPLIED
FUNCTIONAL_TESTS_PASSED
COLD_START_PASSED
RELEASE_ACCEPTED
```

And:

```text
UI_BATCH != LOGICAL_ATOMIC_RELEASE != BACKEND_TRANSACTION
```

Training evidence preserves a batch conflict:

```text
DOCUMENTED = 10 files at one time
OBSERVED = 25 accepted on one tested Project drag-and-drop route
RELATION = DISPUTED
```

A conservative operator may use batches of 10 or fewer without claiming 10 is the universal hidden limit.

## 12. Cold start is necessary but bounded

A serious release should test a brand-new Project chat with canaries for:

- instruction behavior;
- current source retrieval;
- current versus stale precedence;
- absent fact;
- prompt injection;
- authority boundary;
- provenance boundary.

A cold-start PASS does not prove every source is indexed, every future chat will behave identically, all bytes match, or every surface is qualified.

## 13. Surface qualification is non-transitive

Qualify separately:

```text
PROJECT_CHAT
VOICE
DEEP_RESEARCH
WORK
```

A Chat pass does not qualify Voice. A Voice greeting proves only basic Voice operation.

## 14. Debug the first deterministic failing layer

Use:

```text
SYMPTOM
→ REQUIREMENT
→ CONFIGURATION
→ SOURCE IDENTITY
→ LIFECYCLE
→ PARSING/ROUTE
→ RETRIEVAL
→ MEMORY
→ PRECEDENCE/INTERPRETATION
→ ATTRIBUTION
→ PERMISSION
→ AUTHORITY
→ EXECUTION
→ VERIFICATION
→ SURFACE
```

Change one major variable at a time.

A successful repair does not automatically prove the original root cause.

## 15. Repair, rollback, migration

- `REPAIR_IN_PLACE`: bounded editable defect.
- `ROLLBACK`: restore earlier validated editable state.
- `MIGRATION`: desired architecture cannot be reached in place.
- `EXTERNAL_SOURCE_REPAIR`: defect lives in Drive/other external source.
- `PRIVACY_INCIDENT`: restricted material was exposed.

Irreversible does not mean defective. A shared Project being irreversibly project-only is not a problem when project-only is still the requirement.

## 16. Documentation and observation

Use:

```text
DOCUMENTED
OBSERVED
INFERRED
DISPUTED
UNKNOWN
RETRACTED
SUPERSEDED
```

`NOT_DOCUMENTED != UNKNOWN` when adequate direct observation exists.

`OBSERVED_ONCE != UNIVERSAL`.

Documentation does not erase contradictory observation, and observation does not erase contradictory documentation.

## 17. Forensic precision rule

Never let a schema pressure you into filling missing evidence.

```text
SCHEMA_COMPLETION_PRESSURE → FABRICATED_PRECISION
```

Examples that require independent evidence:

- exact timestamps;
- UTC offsets;
- named timezones;
- filenames;
- item-level inventory mappings;
- byte digests;
- tool results;
- execution receipts.

An honest `UNKNOWN` is a valid forensic value.
