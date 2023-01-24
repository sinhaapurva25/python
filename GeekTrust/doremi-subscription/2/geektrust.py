from sys import argv
import subscription

def main():
    
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    
    [print(i) for i in subscription.calculate(f.readlines())]
    
if __name__ == "__main__":
    main()