# Hephaestus Architecture / Release-Boundary Review — On-Theo PR #28 through PR #31

status: COMPLETE
execution_provenance: SAME_RUNTIME_ROLE_PASS
protocol_source:
  repo: thebrazenbeard/hephaestus
  head: 78f6f22a0e5d14617855006a8383765589ac8c67
  current_protocol: docs/PROTOCOL_EXECUTION_PRECEDENCE_V2.md
  operating_manual: docs/OPERATING_MANUAL.md

This review applies Hephaestus's qualified Project/release/provenance engineering discipline from its repository. It was executed in this controlling runtime, not a separately instantiated model runtime.

## #28 consolidation — PASS_WITH_LIMITATIONS

The successor architecture is coherent:
- `main` remains canonical;
- durable content moves to path namespaces;
- work branches cease being epistemic namespaces;
- legacy thematic material is explicitly identified as provenance/review input;
- branch inclusion does not imply supersession;
- external Testament consumption is pinned to immutable On-Theo references until canonical consolidation.

This is sufficient architecture for a reviewable consolidation candidate.

Limitation: the candidate intentionally co-locates historical/legacy and newer prose; consumers must obey the repository architecture labels rather than infer currentness from path existence.

## #29 validator hardening V2 — CHANGES_REQUIRED

The architecture promised fail-closed registry/currentness control, but malformed list entries could be silently filtered out before validation. Exact-head review therefore cannot accept V2 as the final control layer.

## #30 materialization rehearsal — CHANGES_REQUIRED

The rehearsal's isolation architecture is good:
- output is outside source tree;
- generated manifest remains explicitly noncanonical;
- pending witness state is cleared only in output;
- source before/after bytes are verified;
- input/output digests are recorded.

However, it inherited V2's validator blind spots and omitted `unresolved_reference_count`, a field explicitly required by the manifest receipt contract. Those are control-plane defects, so frozen #30 cannot be the final promotion precursor.

## #31 V3 successor — PASS_WITH_LIMITATIONS

Exact subject:
- head `d81ab5ab58f326b0827dbc0f9903befb5580947e`
- tree `e6e94b7ed35551ca675fed64ce2a0999ea441628`

Evidence:
- push CI SUCCESS / 53 tests;
- PR CI SUCCESS / 53 tests;
- validator clean;
- rehearsal clean;
- eight materialized registry digests unchanged;
- manifest-required unresolved-reference count present;
- PR31-bound rebase/dependency audit SUCCESS / 55 tests.

V3 brings implementation back into alignment with the documented architecture:
- record-list shape failures are explicit;
- nested reference failures are explicit;
- required references fail closed;
- manifest path/dependency/type structures are validated;
- review receipts have structural exact-head bindings;
- successful materialization emits the required zero unresolved-reference count.

Promotion architecture limitation — nonblocking for PR31 itself, blocking before candidate creation unless reconciled:
The existing promotion-gate/construction documents name frozen PR30 as the reviewed source subject. A future candidate must now name PR31 as the controlling source/control subject while preserving PR30's unchanged reviewed materialized registry bytes and archived extension input provenance. Do not silently treat V3 as if it had always been part of PR30.

The rehearsal manifest's retained top-level `base_registry_head` is acceptable as source-baseline provenance while `canonical_materialized=false`; a later canonical effect must define its canonical cut identity in the protected promotion receipt rather than retroactively reinterpret that field.

Nonblocking limitation: validator-side SHA format checks cannot prove remote commit existence; external readback remains part of release qualification.

No merge, main mutation, downstream cutover, or canonical materialization is authorized.
