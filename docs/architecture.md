# Phase 1 — Architecture

## Components

1. **Browser adapter** — Playwright, isolated from persona logic.
2. **Conversation router** — LangGraph state machine with typed Pydantic state.
3. **Persona engine** — deterministic style rules + retrieved examples + model prompt.
4. **Memory layer** — local operational state plus vector retrieval; Notion stores durable metadata and curated memory, not raw secrets.
5. **Safety layer** — policy checks, approval queue, audit log, kill switch.
6. **API/UI** — FastAPI local control surface for status, approvals, and diagnostics.
7. **Observability** — structured logs, error events, DOM-selector health and loop metrics.

## Data boundaries

Raw exported conversations remain local and are never committed. Processed training artifacts should also remain local unless explicitly sanitized.

Notion stores task state, persona rules, contact metadata, curated memories and incident records. Vector storage holds embeddings and retrieval payloads.

## Development loop

Plan → implement one bounded change → run tests/lint/type checks → inspect failure → patch → repeat → human review → merge.

No autonomous outbound message sending is enabled by Phase 1.
