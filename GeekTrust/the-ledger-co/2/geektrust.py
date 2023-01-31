from sys import argv
import ledger_module

def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()

    ledger = ledger_module.LedgerClass()
    for i in ledger.result(lines):
        print(i)

    
if __name__ == "__main__":
    main()