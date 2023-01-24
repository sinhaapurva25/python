# https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


a = 10
b = 15
print("gcd(", a, ",", b, ") = ", gcd(a, b))
a = 35
b = 10
print("gcd(", a, ",", b, ") = ", gcd(a, b))

a = 31
b = 2
print("gcd(", a, ",", b, ") = ", gcd(a, b))

def gcd(a,b):
    if a ==0:
        return b
    return gcd(b%a,a)
print((15*10)/gcd(10,15))
print(gcd(10,15))