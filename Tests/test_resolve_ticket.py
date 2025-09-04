from src.core.pipeline import resolve_ticket

def test_resolve_ticket():
    ticket = "My domain was suspended"
    result = resolve_ticket(ticket)

    # Just check that the required fields exist
    assert hasattr(result, "answer")
    assert hasattr(result, "references")
    assert hasattr(result, "action_required")
