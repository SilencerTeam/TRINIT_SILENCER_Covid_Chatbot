
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from asyncio.windows_events import NULL


class ActionCoronaTracker(Action):

    def name(self) -> Text:
        return "action_corona_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response=requests.get("https://data.covid19india.org/data.json").json()
        entities=tracker.latest_message['entities']
        print("Last message", entities)
        state=None

        if state == "india":
            state = "Total"

        for i in entities:
            if(i['entity']=="state"):
                state=i['value']
        message = "Please enter correct state name"

        for data in response["statewise"]:
            if data["state"] == state.title():
                message = "Active cases: " + data["active"] + "\nConfirmed cases: " + data["confirmed"] + "\nTotal deaths: " + data["deaths"] + "\nRecovered: " + data["recovered"] + "\nLast updated: " + data["lastupdatedtime"]


        more = "[website]https://www.mohfw.gov.in/" 
        dispatcher.utter_message(message)
        dispatcher.utter_message(text = "For more update visit"+  more)

        return []
