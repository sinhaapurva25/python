# this python file contains the minimum changes needed in the code to get the code running with the correct outputs
from sys import argv

def main():
    sX = 0
    sY = 0
    dX = 0
    dY = 0
    dir = ""

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    
    for line in lines:
        tokens = line.split()
        if tokens[0]== "SOURCE":
            sX = int(tokens[1])
            sY =int(tokens[2])
            dir = tokens[3]

        if tokens[0]== "DESTINATION":
            dX = int(tokens[1])
            dY = int(tokens[2])
        
        if tokens[0]== "PRINT_POWER":
            p  = calculatePower(sX, sY, dX, dY, dir)
            print("POWER %3d" %  (p))
        

def calculatePower(sX, sY, dX, dY, dir):
    xt=0 
    yt =0
    tot=0
    r=0
    turns=0 
 
    if dX== sX:
        turns = turns
    if dX > sX:
        xt = dX - sX
        if dir == "N":
            turns += 1
        elif dir == "E":
            turns+=0    
        elif dir == "S":
            turns += 1
        elif dir == "W":
            turns += 1

    else:
        xt = sX - dX
        if dir == "N":
            turns += 1
        elif dir == "E":
            turns += 1
        elif dir == "S":
            turns += 1
        elif dir == "W":
            turns+=0

    if dY == sY:
        turns = turns
    if dY > sY:
        yt = dY - sY  
        if dir == "N":
            turns+=0
        elif dir == "E":
            turns+=1
        elif dir == "S":
            turns+=1
        elif dir ==  "W":
            turns+=1
    else:
        yt = sY - dY
        if dir == "N":
            turns+=1
        elif dir == "E":
            turns+=1
        elif dir == "S":
            turns+=0
        elif dir == "W":
            turns+=1

    tot = xt+yt
    r = 200 - ((tot*10) + (turns*5))
    return r

if __name__ == "__main__":
    main()