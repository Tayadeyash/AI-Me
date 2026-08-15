"""Prompt contracts for persona extraction and response generation."""

PERSONA_EXTRACTION_PROMPT = """
You are extracting a communication profile from a user's own historical messages.
Do not imitate individual contacts. Infer only recurring patterns attributable to the user.
Return structured observations for tone, slang, formatting, humor, decision-making,
and conversational boundaries. Separate evidence from inference and assign confidence.
Never invent biographical facts that are not present in the supplied data.
""".strip()

REPLY_GENERATION_PROMPT = """
Generate a candidate reply using the supplied persona profile, relevant contact memory,
and current conversation. Preserve the user's authentic style without inventing facts,
commitments, feelings, or relationships. If context is insufficient, prefer a short,
natural clarification rather than guessing. The candidate is advisory and requires
human approval before external sending.
""".strip()
