from itertools import permutations
S,k = input().split()
S = sorted(S)
for i in list(list(permutations(S,int(k)))):
    w = ''
    for j in i:
        w += j
    print(w)