from utils import operations_read, operations_filter, operations_sorted, operations_formated


def main():
    operations = operations_read("operations.json")
    operations = operations_filter(operations)
    operations = operations_sorted(operations)
    operations = operations_formated(operations)




if __name__ == "__main__":
    main()