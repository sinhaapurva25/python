K = int(input())
lst = list(map(int,input().split()))

s = set(lst)
print(((sum(s)*K)-(sum(lst)))//(K-1))