n, m = map(int,input().split())
arr = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))
# print(len(list(set(arr).intersection(A)))-len(list(set(arr).intersection(B))))
# print(sum([1 for i in A if i in arr]) - sum([1 for i in B if i in arr]))
print(sum(list(map(lambda x: 1 if x in arr else 0, A))) - sum(list(map(lambda x: 1 if x in arr else 0, B))))
'''
n, m = map(int,input().split())
arr = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
happiness = 0
for i in arr:
    for j in A:
        if i==j:
            happiness += 1
    for j in B:
        if i==j:
            happiness -= 1
print(happiness)
'''