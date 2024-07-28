from botsonic import Botsonic
from story import setup_story
from scripts.database import Database

# Initialize the bot
bot = Botsonic("SagaScribe")

# Setup the story
story = setup_story()
bot.set_story(story)

# Initialize the database
database = Database()

@bot.on_save
def save_progress(user_id, state):
    database.save(user_id, state)

@bot.on_load
def load_progress(user_id):
    return database.load(user_id)

# Deploy the bot
bot.deploy(platform="web", url="https://yourwebsite.com/sagascribe")

# Start the bot
bot.start()
