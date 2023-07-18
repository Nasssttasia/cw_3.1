from datetime import datetime
import json


def operations_read(file_name):
    with open(file_name, "r", encoding='utf-8') as file:
        operations = json.load(file)
        return operations


def operations_filter(operations):
    operations = [x for x in operations if "state" in x and x["state"] == "EXECUTED"]
    return operations


def operations_sorted(operations):
    operations = sorted(operations, key=lambda x: x['date'])
    return operations[-5:]


def operations_formated(operations):
    for x in operations:
        date = datetime.strptime(x['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")





