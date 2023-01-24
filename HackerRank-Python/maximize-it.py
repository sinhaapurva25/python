# Enter your code here. Read input from STDIN. Print output to STDOUT
K, M = map(int,input().split())
s = 0
if K > 7:
    K = 7
for i in range(K):
    MAX = max(list(map(int, input().split()))[:7])
    s += MAX*MAX
print(s%M)