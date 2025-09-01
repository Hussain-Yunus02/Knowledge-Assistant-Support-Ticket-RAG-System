from src.core.retriever import search
from src.core.generator import generate_response

def resolve_ticket(ticket_text: str):
    docs = search(ticket_text, k=5)
    response = generate_response(ticket_text, docs)
    return response
