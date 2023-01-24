# max([int(input()) for _ in range(int(input()))].sort())

n = int(input())
arr = sorted(list(map(int,input().split()))[:n])
arr.pop()
print(arr.pop())