from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_current_state_is_runtime_neutral():
    current = read("state/CURRENT.md")
    exodus = read("docs/EXODUS_CONTINUITY_V1.md")
    assert "permanent_chat_required: NO" in current
    assert "EPHEMERAL_TERMINAL" in current
    assert "No archived chat is an assignment source." in exodus


def test_runtime_bootstrap_reconstructs_without_chat_locator():
    bootstrap = read("templates/RUNTIME_BOOTSTRAP.md")
    for forbidden in ("chatgpt.com/", "conversation ID is required", "branch from the trained"):
        assert forbidden not in bootstrap
    for required in (
        "state/CURRENT.md",
        "training/QUALIFICATION_PACKET.md",
        "CURRENT_ASSIGNMENT_SOURCE",
        "PROTECTED_EFFECT_BOUNDARY",
        "HEPHAESTUS_RUNTIME_INSTANTIATED_FROM_VERIFIED_DURABLE_STATE",
    ):
        assert required in bootstrap or required in read("docs/EXODUS_CONTINUITY_V1.md")


def test_legacy_bootstrap_is_non_operational_redirect():
    legacy = read("templates/WORKING_CHAT_BOOTSTRAP.md")
    assert "SUPERSEDED_OPERATIONAL_INTERFACE" in legacy
    assert "templates/RUNTIME_BOOTSTRAP.md" in legacy
    assert "no chat title, URL, conversation ID" in legacy


def test_current_operating_docs_do_not_require_permanent_hephaestus_chat():
    state = read("docs/STATE.md")
    active = read("work/ACTIVE_WORK.md")
    continuity = read("docs/CONTINUITY.md")
    assert "PERMANENT HEPHAESTUS CHAT REQUIRED = NO" in state
    assert "PERMANENT_CHAT_REQUIRED = NO" in active
    assert "No permanent ChatGPT conversation" in continuity
