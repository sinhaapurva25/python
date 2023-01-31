from sys import argv
import get_results

def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()

    [print(i) for i in get_results.result(lines)]
    
if __name__ == "__main__":
    main()