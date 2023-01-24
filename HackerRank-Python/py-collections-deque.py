from collections import deque
d = deque()
for i in range(int(input())):
    command = input().split()
    if command[0]=='append':
        d.append(int(command[1]))
    elif command[0]=='appendleft':
        d.appendleft(int(command[1]))
    elif command[0]=='pop':
        d.pop()
    elif command[0]=='popleft':
        d.popleft()
    else:
        pass
print(*d)