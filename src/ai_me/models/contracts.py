"""Shared typed contracts between agent components."""

from typing import Literal
from pydantic import BaseModel, Field

Platform = Literal["whatsapp", "instagram", "other"]


class IncomingMessage(BaseModel):
    platform: Platform
    contact_id: str
    contact_name: str | None = None
    text: str
    timestamp: str
    message_id: str | None = None


class CandidateReply(BaseModel):
    text: str = Field(min_length=1)
    confidence: float = Field(ge=0, le=1)
    rationale: str
    requires_approval: bool = True


class ContactMemory(BaseModel):
    contact_id: str
    relationship: str | None = None
    context_summary: str = ""
    preferences: list[str] = []
    boundaries: list[str] = []
