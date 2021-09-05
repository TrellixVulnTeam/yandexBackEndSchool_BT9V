import json
import copy
from typing import Dict, Any

with open("input.txt") as data:
    eventList = "".join(data.readlines())

eventList = json.loads(eventList)
answerDict = {}

for event in eventList:
    if event["order_id"] not in answerDict:
        answerDict[event["order_id"]] = {event["item_id"]: event}
    else:
        if event["item_id"] not in answerDict[event["order_id"]]:
            answerDict[event["order_id"]][event["item_id"]] = event
        else:
            if event["event_id"] > answerDict[event["order_id"]][event["item_id"]]["event_id"]:
                answerDict[event["order_id"]][event["item_id"]] = event

listToSend = []
dictToAdd: Dict[str, Any] = {}
for order_id in answerDict:
    dictToAdd.clear()
    dictToAdd["items"] = []
    dictToAdd["id"] = order_id
    order = answerDict[order_id]
    for (item_id, item) in order.items():
        if item["status"] == "OK" and (item["count"] - item["return_count"]) > 0:
            dictToAdd["items"].append({"count": (item["count"] - item["return_count"]), "id": item["item_id"]})
    if len(dictToAdd["items"]) != 0:
        listToSend.append(copy.deepcopy(dictToAdd))

with open("output.txt", "w") as o:
    o.write(json.dumps(listToSend))