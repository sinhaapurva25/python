if __name__ == '__main__':
    N = int(input())
    
    lst = []

    commandarray = []
    for i in range(N):
        command = input().split()
        commandarray.append(command)
        
    for i in range(N):
        command = commandarray[i]
        operand1 = None
        operand2 = None
        if len(command)==1:
            pass
        elif len(command)==2:
            operand1 = int(command[1])
        else:
            operand1 = int(command[1])
            operand2 = int(command[2])
        if command[0] == 'insert': lst.insert(operand1,operand2)
        if command[0] == 'print': print(lst)
        if command[0] == 'remove':lst.remove(operand1)
        if command[0] == 'append': lst.append(operand1)
        if command[0] == 'sort': lst.sort()
        if command[0] == 'pop': lst.pop()
        if command[0] == 'reverse':lst.reverse()