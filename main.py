from path import DATA_PATH
from utils import operations_read, operations_filter, operations_sorted, operations_formated


def main():
    operations = operations_read(DATA_PATH)
    operations = operations_filter(operations)
    operations = operations_sorted(operations)
    operations = operations_formated(operations)
    return print(operations)




if __name__ == "__main__":
    main()