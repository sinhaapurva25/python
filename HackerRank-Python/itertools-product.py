from itertools import product
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
res = ''
for i in list(product(*[A,B])):
    res += str(i)+' '
print(res.rstrip())