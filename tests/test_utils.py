from path import DATA_PATH
from utils import operations_read, operations_filter, operations_sorted, operations_formated


def test_operations_read():
    assert isinstance(operations_read(DATA_PATH), list)


def test_operations_filter():
    test_data = [{'state': 'EXECUTED'}, {'state': 'CANCELED'}, {}]
    assert operations_filter(test_data) == [{'state': 'EXECUTED'}]


def test_operations_sorted():
    test_data = [{"date": "2018-09-12T21:27:25.241689"}, {"date": "2018-10-14T08:21:33.419441"}, {"date": "2018-01-26T15:40:13.413061"}, {"date": "2018-04-14T19:35:28.978265"}, {"date": "2019-09-11T17:30:34.445824"}]
    assert operations_sorted(test_data) == [{"date": "2018-01-26T15:40:13.413061"}, {"date": "2018-04-14T19:35:28.978265"}, {"date": "2018-09-12T21:27:25.241689"}, {"date": "2018-10-14T08:21:33.419441"}, {"date": "2019-09-11T17:30:34.445824"}]


def test_operations_formated():
    test_data = [{
    "id": 801684332,
    "state": "EXECUTED",
    "date": "2019-11-05T12:04:13.781725",
    "operationAmount": {
      "amount": "21344.35",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 77613226829885488381"
  }]
    assert operations_formated(test_data) == """05.11.2019 Открытие вклада
    -> Счет **8381
    21344.35 руб."""