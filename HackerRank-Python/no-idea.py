# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int,input().split())
arr = list(map(int,input().split()))
A = set(map(int,input().split()[:n]))
B = set(map(int,input().split()[:m]))

# a = sum([1 for i in arr if i in A])
# b = sum([1 for i in arr if i in B])

happiness = sum([(i in A)-(i in B) for i in arr])
print(happiness)