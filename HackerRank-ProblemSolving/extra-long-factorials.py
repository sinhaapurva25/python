def extraLongFactorials(n):
    f = 1
    for i in range(n):
        f = f*(i+1)
    return f
print(extraLongFactorials(25))

def fact(n):
    if(n==1):
        return 1
    prod=n*fact(n-1)
    return prod
print(fact(25))