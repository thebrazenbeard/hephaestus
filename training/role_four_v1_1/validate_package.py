#!/usr/bin/env python3
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
MANIFEST = ROOT / "manifest.json"

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def fail(msg):
    print(f"FAIL: {msg}")
    return 1

def main():
    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception as exc:
        return fail(f"manifest parse error: {exc}")

    required = [
        "schema_version", "package_id", "package_version", "role",
        "ordered_modules", "files", "qualification", "currentness_contract"
    ]
    for key in required:
        if key not in manifest:
            return fail(f"missing manifest key {key}")

    if manifest["package_version"] != "1.1.0":
        return fail("unexpected package version")

    ordered = manifest["ordered_modules"]
    if not ordered or ordered[-1] != "modules/09_final_qualification.md":
        return fail("final qualification must be last")

    declared = manifest["files"]
    if len(declared) != len(set(declared)):
        return fail("duplicate declared path")

    actual_files = {
        p.relative_to(ROOT).as_posix()
        for p in ROOT.rglob("*")
        if p.is_file() and p.name != "manifest.json" and "__pycache__" not in p.parts
    }
    if set(declared) != actual_files:
        return fail(f"declared file set mismatch: declared={sorted(declared)} actual={sorted(actual_files)}")

    for rel, expected in declared.items():
        p = (ROOT / rel).resolve()
        if ROOT.resolve() not in p.parents and p != ROOT.resolve():
            return fail(f"path traversal: {rel}")
        if sha256(p) != expected:
            return fail(f"checksum mismatch: {rel}")

    for rel in ordered:
        if rel not in declared:
            return fail(f"ordered module not checksum-bound: {rel}")

    if manifest["currentness_contract"].get("mutable_state_after_training") != "RETRIEVE_FRESH":
        return fail("mutable currentness must be retrieved after training")

    print(f"PASS: {manifest['package_id']} {manifest['package_version']} files={len(declared)} modules={len(ordered)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
