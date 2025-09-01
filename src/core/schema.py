from pydantic import BaseModel, field_validator
from typing import List, Literal

Action = Literal["none", "request_user_info", "escalate_to_abuse_team", "escalate_to_billing", "escalate_to_tier2"]

class MCPResponse(BaseModel):
    answer: str
    references: List[str]
    action_required: Action

    @field_validator("references")
    @classmethod
    def validate_references(cls, v):
        assert all(isinstance(x, str) and x.strip() for x in v), "All references must be non-empty strings"
        return v
