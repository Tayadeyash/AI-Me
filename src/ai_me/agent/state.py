"""State machine types for the conversation loop."""

from typing import TypedDict
from ai_me.models.contracts import CandidateReply, IncomingMessage


class AgentState(TypedDict, total=False):
    incoming: IncomingMessage
    retrieved_memory: list[str]
    persona_context: str
    candidate: CandidateReply
    approval_status: str
    error: str
