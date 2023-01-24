A = set(map(int,input().split()))
N = int(input())
b = 1
for i in range(N):
    if A.issuperset(set(list(map(int,input().split())))):
        b = 1
    else:
        b = 0
        break
print(bool(b))