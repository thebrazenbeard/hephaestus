# Role Four Training Bootstrap v1

Purpose: train a fresh Role Four / Hephaestus working chat to a reusable `BASE_READY` capability baseline without replaying mutable operational history.

## Loader procedure

1. Read `manifest.json`.
2. Verify the package with `python validate_package.py`.
3. Read each module in `ordered_modules` exactly once, in manifest order.
4. Complete each module's exercise and evaluate it against that module's pass criteria.
5. Stop and correct any failed hard gate before advancing.
6. Complete the final qualification module.
7. Emit `BASE_READY` only if every module passes, the final qualification passes, and the package validator succeeds.
8. After `BASE_READY`, reorient operationally from the repository's current accepted-state pointer and current project coordination sources. Do not bake assignments, leases, branch SHAs, or transient state into training.

## State vocabulary

- `UNTRAINED`: package not executed.
- `TRAINING`: modules in progress.
- `MODULE_BLOCKED`: one or more hard-gate criteria failed.
- `BASE_READY`: reusable role competence established by this package.
- `OPERATIONALLY_REORIENTED`: fresh current-state retrieval completed after `BASE_READY`.

`BASE_READY` is not authority to merge, deploy, mutate production, change credentials, delete data, or bypass writer-lease rules.
