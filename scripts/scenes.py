from botsonic import Scene, Decision, Outcome

# Introduction scene
intro_scene = Scene(
    id="intro",
    description="Welcome, adventurer! You find yourself in a dark forest. To your left, there’s a dense thicket, and to your right, a narrow path leads deeper into the woods. What do you do?"
)

# Define decisions in the introduction scene
decision_intro = Decision(
    prompt="Choose your action:",
    options=[
        {"text": "Explore the thicket", "outcome": "thicket"},
        {"text": "Follow the path", "outcome": "path"}
    ]
)

# Add the decision to the introduction scene
intro_scene.add_decision(decision_intro)

# Define outcomes for the first decision
outcome_thicket = Outcome(
    description="You push through the thicket and discover a hidden glade with an ancient altar. What do you do?",
    next_scene="glade"
)

outcome_path = Outcome(
    description="You follow the path and hear the sound of running water. You soon find a sparkling stream. What do you do?",
    next_scene="stream"
)

# Add outcomes to the decision
decision_intro.add_outcome("thicket", outcome_thicket)
decision_intro.add_outcome("path", outcome_path)

# Other scenes
glade_scene = Scene(
    id="glade",
    description="You are in a hidden glade with an ancient altar. Eldrin the Guide appears and offers you a choice."
)

stream_scene = Scene(
    id="stream",
    description="You are by a sparkling stream. You notice some berries growing nearby and hear rustling in the bushes."
)

combat_scene = Scene(
    id="combat",
    description="You encounter a fierce goblin. Prepare for combat!",
    event="combat_event"
)

puzzle_scene = Scene(
    id="puzzle",
    description="You find a locked door with a complex puzzle. Solve the puzzle to proceed.",
    decisions=[
        Decision(
            prompt="What is the correct sequence of levers?",
            options=[
                {"text": "123", "outcome": "puzzle_fail"},
                {"text": "231", "outcome": "puzzle_success"},
                {"text": "312", "outcome": "puzzle_fail"}
            ]
        )
    ]
)
