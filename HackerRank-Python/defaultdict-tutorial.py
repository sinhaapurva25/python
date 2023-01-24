m,n = [int(i) for i in input().split()]
A = [input() for i in range(m)]
B = [input() for i in range(n)]
for i in B:
    foundAt = ''
    for idx,j in enumerate(A):
        if i==j:
            foundAt = foundAt + str(idx+1) + ' '
    if len(foundAt)>0:
        print(foundAt.rstrip(' '))
    else:
        print('-1')