import json
from src.core.mcp_prompt import MCP_PROMPT_TEMPLATE
from src.core.schema import MCPResponse

def call_llm(prompt: str) -> str:
    """
    Stub for LLM call. Replace with OpenAI or local LLM call.
    """
    # For now, return a fixed JSON
    return json.dumps({
        "answer": "Your domain may have been suspended due to missing WHOIS info. Please update it and contact support.",
        "references": ["Policy: Domain Suspension Guidelines, Section 4.2"],
        "action_required": "escalate_to_abuse_team"
    })

def generate_response(ticket_text: str, docs: list) -> MCPResponse:
    context = "\n".join([f"[{i}] {d['source']}: {d['text']}" for i, d in enumerate(docs, 1)])
    prompt = MCP_PROMPT_TEMPLATE.format(context=context, ticket=ticket_text)
    raw = call_llm(prompt)
    return MCPResponse.model_validate_json(raw)
