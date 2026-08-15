"""Human-in-the-loop boundary for outbound communication."""

from ai_me.models.contracts import CandidateReply


def requires_human_approval(candidate: CandidateReply) -> bool:
    """Outbound messages remain approval-gated during development."""
    return True
