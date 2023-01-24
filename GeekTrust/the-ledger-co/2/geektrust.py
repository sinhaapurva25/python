from sys import argv
import ledger

def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()

    [print(i) for i in ledger.Result(Lines)]
    
if __name__ == "__main__":
    main()