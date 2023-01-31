from sys import argv
import result_module


def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()

    ledger = result_module.ResultClass()
    for i in ledger.result_function(lines):
        print(i)


if __name__ == "__main__":
    main()
