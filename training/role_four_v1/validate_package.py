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
        "ordered_modules", "files", "qualification"
    ]
    for key in required:
        if key not in manifest:
            return fail(f"missing manifest key {key}")

    if manifest["package_version"] != "1.0.0":
        return fail("unexpected package version")

    ordered = manifest["ordered_modules"]
    if not ordered or ordered[-1] != "modules/09_final_qualification.md":
        return fail("final qualification must be last")

    declared = manifest["files"]
    if len(declared) != len(set(declared)):
        return fail("duplicate declared path")

    for rel, expected in declared.items():
        p = (ROOT / rel).resolve()
        if ROOT.resolve() not in p.parents and p != ROOT.resolve():
            return fail(f"path traversal: {rel}")
        if not p.is_file():
            return fail(f"missing file: {rel}")
        actual = sha256(p)
        if actual != expected:
            return fail(f"checksum mismatch: {rel}")

    for rel in ordered:
        if rel not in declared:
            return fail(f"ordered module not checksum-bound: {rel}")

    print(f"PASS: {manifest['package_id']} {manifest['package_version']} files={len(declared)} modules={len(ordered)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
