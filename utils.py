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

        description = x['description']

        if "from" in x:
            from_list = list(x['from'])
            if x["from"].startswith('Счет'):
                latest_four_num = "".join(from_list[-4:])
                from_ = f'Счет **{latest_four_num}'
            else:
                name = "".join(from_list[:-16])
                from_ = f'{name} {"".join(from_list[-16: -13])} {"".join(from_list[-12: -10])}** **** {"".join(from_list[-4:])}'
        else:
            from_ = ''

        to_list = list(x["to"])
        if x["to"].startswith('Счет'):
            latest_four_num = "".join(to_list[-4:])
            to_ = f'Счет **{latest_four_num}'
        else:
            name = "".join(to_list[:-16])
            to_ = f'{name} {"".join(to_list[-16: -13])} {"".join(to_list[-12: -10])}** **** {"".join(to_list[-4:])}'

        amount = x["operationAmount"]["amount"]

        name = x["operationAmount"]["currency"]["name"]

        operations_str = (f'{date} {description}\n{from_} -> {to_}\n{amount} {name}\n')
        print(operations_str)
        continue




