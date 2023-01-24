# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
N = int(input())
arr = [i.lower() for i in input().split(" ")][:N]
K = int(input())
combs = list(combinations(arr,K))
c = 0
for i in combs:
    if 'a' in i:
        c += 1
print(c/len(combs))