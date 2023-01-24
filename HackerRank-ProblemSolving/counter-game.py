import math
def counterGame(n):
    # Write your code here
    l = 1
    # print(n)
    while not(n<=2):
        p = math.log2(n)
        z = str(p).split('.')
        if z[1] == 0:
            n //= 2
        else:
            n -= 2**int(z[0])
        # print(n)
        l += 1
    if l%2==1: return 'Louis'
    else: return 'Richard'

print(counterGame(1560834904))
print(counterGame(1768820483))
print(counterGame(1533726144))
print(counterGame(1620434450))
print(counterGame(1463674015))