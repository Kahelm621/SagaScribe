from botsonic import Story, Scene, Decision, Outcome
from scripts.characters import npc_guide
from scripts.scenes import intro_scene, glade_scene, stream_scene, combat_scene, puzzle_scene

def setup_story():
    # Initialize the story
    story = Story(
        title="SagaScribe Adventure",
        description="An interactive fiction game where your choices shape the story."
    )

    # Add characters
    story.add_character(npc_guide)

    # Add scenes
    story.add_scene(intro_scene)
    story.add_scene(glade_scene)
    story.add_scene(stream_scene)
    story.add_scene(combat_scene)
    story.add_scene(puzzle_scene)

    return story
