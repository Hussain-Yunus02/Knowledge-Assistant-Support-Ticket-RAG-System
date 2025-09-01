from src.core.pipeline import resolve_ticket

def test_resolve_ticket():
    ticket = "My domain was suspended"
    result = resolve_ticket(ticket)
    assert "domain" in result.answer.lower()
    assert result.references
