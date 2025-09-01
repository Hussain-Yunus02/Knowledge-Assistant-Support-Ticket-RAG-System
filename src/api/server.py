from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.core.pipeline import resolve_ticket
from src.core.schema import MCPResponse

app = FastAPI(title="Knowledge Assistant", version="1.0.0")

class Ticket(BaseModel):
    ticket_text: str

@app.post("/resolve-ticket", response_model=MCPResponse)
def resolve_ticket_endpoint(ticket: Ticket):
    try:
        return resolve_ticket(ticket.ticket_text)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
