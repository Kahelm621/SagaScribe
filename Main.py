from botsonic import Botsonic
from story import setup_story
from scripts.database import Database
import os
import multiprocessing

def run_rasa_services():
    # This function will start the Rasa server and Rasa shell
    os.system("rasa run actions & rasa shell")

if __name__ == "__main__":
    # Start Rasa services in a separate process
    rasa_process = multiprocessing.Process(target=run_rasa_services)
    rasa_process.start()

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
