"""Persona representation used by retrieval and generation layers."""

from pydantic import BaseModel, Field


class PersonaProfile(BaseModel):
    tone: list[str] = []
    slang: list[str] = []
    formatting_rules: list[str] = []
    humor_patterns: list[str] = []
    decision_rules: list[str] = []
    boundaries: list[str] = []
    examples: list[str] = []
    version: str = "0.1.0"
    confidence: float = Field(default=0.0, ge=0, le=1)
