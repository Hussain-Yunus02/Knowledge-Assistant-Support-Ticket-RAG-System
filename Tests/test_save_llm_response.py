import json
from src.utils.save_response import save_llm_response

def test_save_llm_response(tmp_path):
    response = {
        "answer": "Update WHOIS info to reactivate.",
        "references": ["Policy: Domain Suspension Guidelines, Section 4.2"],
        "action_required": "escalate_to_abuse_team"
    }

    saved_file = save_llm_response(response, pdfs_dir=tmp_path)

    # Just check the file was created and is valid JSON
    with open(saved_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert "answer" in data
    assert "references" in data
    assert "action_required" in data
