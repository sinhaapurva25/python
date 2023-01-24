def jumpingOnClouds(c, k):
    e = 100
    i = k % len(c)
    e -= c[i] * 2 + 1
    while i != 0:
        e -= c[(i + k) % len(c)] * 2 + 1
    return e
k = 2
c = [0, 0, 1, 0, 0, 1, 1, 0]
print(jumpingOnClouds(c,k))
# m = list(map(int,input().split()))
# print(m)

def jumpingOnClouds(c, k):
    energy = 100
    n = len(c)
    i = 0
    while i in range(n):
        energy -= 1 + c[(i+k) % n]*2
        i += k
        return energy