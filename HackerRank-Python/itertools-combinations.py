from itertools import combinations
S,k = input().split()
S = sorted(S)
for j in range(1,int(k)+1):
    for i in list(combinations(S,j)):
        w = ''
        for j in i:
            w += j
        print(w)