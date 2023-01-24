from sys import argv
import getResults

def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()

    [print(i) for i in getResults.Result(Lines)]
    
if __name__ == "__main__":
    main()