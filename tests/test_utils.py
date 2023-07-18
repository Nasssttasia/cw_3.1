from utils import operations_read, operations_filter


def test_operations_read():
    assert isinstance(operations_read('../operations.json'), list)


def test_operations_filter():
    test_data = [{'state': 'EXECUTED'}, {'state': 'CANCELED'}, {}]
    assert operations_filter(test_data) == [{'state': 'EXECUTED'}]