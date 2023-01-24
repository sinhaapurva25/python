a = -1
b = 1
s = 0
print("enter n: ",end='')
n = int(input())
while s!=n:
    c = a+b
    print(c)
    a = b
    b = c
    s += 1