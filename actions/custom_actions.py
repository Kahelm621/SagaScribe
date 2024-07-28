from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# Ensure these imports are correct and the modules exist
from scripts.database import get_inventory, update_inventory  
from scripts.characters import get_guide_interaction  

class ActionInteractGuide(Action):

    def name(self) -> Text:
        return "action_interact_guide"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        inventory = get_inventory(tracker.sender_id)  
        interaction_text = get_guide_interaction()  
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
