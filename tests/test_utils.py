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
    "id": 122284694,
    "state": "EXECUTED",
    "date": "2019-08-08T21:58:06.688541",
    "operationAmount": {
      "amount": "98657.83",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 99668626339273709694",
    "to": "Счет 27219929444683698245"
  }]
    assert operations_formated(test_data) == """08.08.2019 Перевод организации\nСчет **9694 -> Счет **8245\n98657.83 руб.\n\n"""