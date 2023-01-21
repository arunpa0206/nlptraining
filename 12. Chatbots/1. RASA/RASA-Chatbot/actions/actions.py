# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import mysql.connector


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print(tracker.latest_message['text'])

        db=mysql.connector.connect(host='localhost',user='root',passwd='password',database='telecom' )
        cursor = db.cursor(buffered=True)
        cursor.execute( "SELECT * FROM test where month_name=%s" , (tracker.latest_message['text'], ))
        account = cursor.fetchone()
        cursor.close()
        db.close()
        dispatcher.utter_message(text=str(account[2]))

        return []
