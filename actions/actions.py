from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from scripts.database import get_inventory, update_inventory  # Adjusted for correct import
from scripts.characters import get_guide_interaction  # Assuming this function exists

class ActionInteractGuide(Action):

    def name(self) -> Text:
        return "action_interact_guide"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        inventory = get_inventory(tracker.sender_id)  # Fetch user-specific inventory
        interaction_text = get_guide_interaction()  # Assuming a function to get guide interaction
        dispatcher.utter_message(text=f"{interaction_text} Your inventory: {inventory}")
        return []

class ActionChoosePath(Action):

    def name(self) -> Text:
        return "action_choose_path"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response="utter_explore_path")
        return []

class ActionChooseThicket(Action):

    def name(self) -> Text:
        return "action_choose_thicket"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(response="utter_explore_thicket")
        return []

