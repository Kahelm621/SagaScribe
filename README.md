# SagaScribe

![SagaScribe Dungeon Master bot](Dungeon%20Master%20Bot%20app.jpg)

SagaScribe is an early-stage, text-based fantasy adventure chatbot that acts as a "Dungeon Master." Players type what they want to do, and the bot guides them through scenes, choices and outcomes, with an NPC guide and a simple inventory.

> **Status:** learning prototype / work in progress. Some modules are stubs and the project does not run end to end yet.

## What I practiced
- Designing a branching story as data (scenes, decisions, outcomes)
- Conversational AI with [Rasa](https://rasa.com/): intents, NLU training examples, stories, rules and custom actions
- Organizing a Python project into modules
- A first attempt at CI/CD with GitHub Actions

## How it works
1. **NLU** (`data/nlu.yml`) teaches the bot to recognize intents such as `greet`, `explore`, `interact` and `choose`.
2. **Stories and rules** (`data/stories.yml`, `data/rules.yml`) define how the conversation flows.
3. **Custom actions** (`actions/custom_actions.py`) run Python code, such as talking to the guide or updating inventory.
4. **Story engine** (`scripts/`) holds the scenes, characters, events, outcomes and save/load database.

## Project structure
```
SagaScribe/
├── Main.py                 # Entry point: starts Rasa services and the story bot
├── decisions.py            # Decision helpers
├── domain.yml              # Rasa domain: intents, responses, actions
├── config.yml              # Rasa NLU pipeline and policies
├── endpoints.yml           # Action server endpoint
├── credentials.yml         # Rasa channel settings (no secrets)
├── data/                   # nlu.yml, stories.yml, rules.yml
├── actions/                # Rasa custom actions
├── scripts/                # Story, scenes, characters, events, inventory, outcomes, database
└── .github/workflows/      # Deploy workflow (experimental)
```

## Running locally (experimental)
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install rasa rasa-sdk
rasa train
rasa run actions &   # in one terminal
rasa shell           # in another
```

## Roadmap
- [ ] Finish the story engine modules and connect them to Rasa actions
- [ ] Add full dependencies to `requirements.txt`
- [ ] Replace the experimental deploy workflow
- [ ] Add tests for scenes and decisions

## License
MIT. See [LICENSE](LICENSE).
