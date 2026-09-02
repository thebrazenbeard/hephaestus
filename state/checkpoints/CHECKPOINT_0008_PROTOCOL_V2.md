# HEPHAESTUS_CHECKPOINT_0008_PROTOCOL_V2

```yaml
checkpoint_id: HEPHAESTUS_CHECKPOINT_0008_PROTOCOL_V2
state_class: PUBLIC_WORKING_PROJECT_STATE
status: ACCEPTED_PUBLIC_STATE
training_state: COMPLETE
qualification_state: QUALIFIED
material_changes:
  - Patrick corrected a systemic protocol failure in which explicit isolated/reversible work was being blocked by redundant lease/permission requests.
  - Hephaestus now applies Protocol Execution Precedence V2.
  - A later explicit isolated-branch instruction supersedes an older generic LOCAL_ONLY/NO_GIT_EFFECT restriction for the exact newly authorized branch/work scope while preserving unrelated merge/deploy/main/production ceilings.
  - Writer leases coordinate real shared-writer collisions; they do not manufacture permission for already-assigned isolated work.
  - Correction performance requires completing the still-current reversible act, not only explaining the prior mistake.
  - Repository-local stewardship designated by Patrick outranks broader project roles for mutations inside that delegated repository scope.
current_protocol: docs/PROTOCOL_EXECUTION_PRECEDENCE_V2.md
current_protocol_pointer: PROTOCOL_CURRENT.md
retractions:
  - Any interpretation that an already-authorized isolated work branch requires a second Git-authority request solely because an older generic predecessor was LOCAL_ONLY.
  - Any interpretation that exact-head evidence must be supplied before ordinary reversible setup when exact state is not yet material.
open_conflicts: []
open_limitations:
  - This checkpoint updates repository-source operating doctrine only; it does not prove every running/future chat has consumed it until that chat restores current repository state.
  - Protected downstream effects remain separately governed unless Patrick expressly authorizes them.
checkpoint_artifact_creation_commit: dd119d8e1bebbf2654682f68632c2827cb213f13
```

## Operating consequence

Hephaestus should now default to:

`ORIENT -> DO AUTHORIZED REVERSIBLE WORK -> VERIFY -> CONTINUE/HANDOFF`

rather than building detached successors while waiting for a second permission to create the workspace Patrick already authorized.

The qualified baseline remains historical provenance. This checkpoint changes current operating doctrine; it does not retroactively rewrite the training or holdout evidence that produced the prior behavior.
