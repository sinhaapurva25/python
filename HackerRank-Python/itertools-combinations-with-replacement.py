from itertools import combinations_with_replacement
S,k = input().split()
S = sorted(S)
for i in list(list(combinations_with_replacement(S,int(k)))):
    w = ''
    for j in i:
        w += j
    print(w)