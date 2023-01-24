n = int(input())
s = set(map(int, input().split()))
noOfCommands = int(input())

for i in range(noOfCommands):
    inp = input().split()
    try:
        if inp[0] == 'remove':
            s.remove(int(inp[1]))
        if inp[0] == 'discard':
            s.discard(int(inp[1]))
        if inp[0] == 'pop': s.pop()
    except Exception as e: pass
print(sum(s))