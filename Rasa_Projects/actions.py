# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# custom action을 실행하기 위해 필요한 modules을 import 
from typing import Any, Text, Dict, List 

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


# class of custom action
class ActionFacilitySearch(Action): 
    
    def name(self) -> Text:
        return "action_facility_search" # action name을 지정. stories, domain에도 포함되어 있어야 함  
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        facility = tracker.get_slot("facility_type") # get_slot(A) 메소드를 통해 A slot에 저장된 정보를 가져옴 
                                                     # slot value 값을 'facility' 변수에 저장  
        address = "300 Hyde St, San Francisco" # 원래 facility 정보를 통해 address를 알아냄
                                               # 예시의 단순성을 위해 hardcoded
        dispatcher.utter_message("Here is the address of the {}:{}".format(facility, address))

        return [SlotSet("address", address)] # SlotSet(slot name, value)