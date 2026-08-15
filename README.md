# AI-Me

Personalized AI agent for conversational assistance and browser-based social interaction.

## Phase 1 status

- Architecture defined
- Repository scaffolded
- Notion workspace schema defined
- Browser automation is planned for visible, user-authorized sessions
- Human-in-the-loop approval is mandatory before any outbound message in the testing phase

## Architecture

```text
                +----------------------+
                |   Browser / UI       |
                | WhatsApp / Instagram |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Browser Adapter      |
                | Playwright           |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Conversation Router  |
                | LangGraph + Pydantic |
                +----+-------------+---+
                     |             |
          +----------+             +-----------+
          v                                    v
+----------------------+             +----------------------+
| Persona Engine       |             | Memory / Retrieval   |
| Style + decision     |             | Qdrant/Chroma        |
| rules + prompt       |             | + Notion metadata    |
+----------+-----------+             +----------+-----------+
           |                                    |
           +----------------+-------------------+
                            v
                   +------------------+
                   | HITL Gate        |
                   | approve/edit/deny|
                   +--------+---------+
                            |
                            v
                   +------------------+
                   | Browser Sender   |
                   +------------------+

Notion: project/task tracking, persona rules, contact metadata, memory index, incident log.
GitHub: source control, CI, tests, releases.
```

## Planned stack

- Python 3.12+
- FastAPI for local control/API surface
- Pydantic v2 for typed contracts
- LangGraph for stateful agent orchestration
- Playwright for browser automation
- SQLite for local operational state during development
- Qdrant as the production vector store; Chroma is acceptable for local experiments
- sentence-transformers for local embeddings where appropriate
- pytest + Ruff + mypy for quality gates
- GitHub Actions for CI

## Safety boundary

The project will not attempt to bypass CAPTCHAs, anti-bot controls, account security, or platform access restrictions. Browser automation will use a normal, user-authorized session. Autonomous sending stays disabled until the HITL phase explicitly enables it.
