import math
class numericalOperations:
    delAttribute = ''
    nonPublic = 0
    def __init__(self,delAttribute,nonPublic):
        self.delAttribute = delAttribute
        self._nonPublic = nonPublic
    def isPrime(self,number):
        c = 0
        for i in range(1,int(number)+1):
            if number%i==0:
                c += 1
        if c==2:
            return True
        else:
            return False
    def factorsThatArePrime(self,number):
        primfac = []
        for i in range(1,number+1):
            if number%i == 0:
                if self.isPrime(i): primfac.append(i)
        return primfac
    def primeFactors(self,number):
        primefac = list()
        while number % 2 == 0:
            primefac.append(2)
            number /= 2
        # print("int(math.sqrt(number))+1",int(math.sqrt(number))+1)
        for i in range(3, int(math.sqrt(number))+1, 2):
            while number % i == 0:
                primefac.append(i)
                number /= i
        if number > 2:
            primefac.append(int(number))
        return primefac
    def lcm(self,num1,num2):
        primefac1 = self.factorsThatArePrime(num1)
        primefac2 = self.factorsThatArePrime(num2)
        lcm = list()
        primefac1.extend(primefac2)
        return lcm
k = numericalOperations('three','xcv')
print("isPrime",k.isPrime(48))
print("factorsThatArePrime",k.factorsThatArePrime(48))
# print("primeFactors",k.primeFactors(315))
for i in range(1,51):
    print(i,"=",k.primeFactors(i))
print("lcm",k.lcm(6,8))
print(k.delAttribute)
del k.delAttribute
print(k.nonPublic)
print(numericalOperations('ninety-nine','').factorsThatArePrime(0))

# def isPrime(n):
#     c = 0
#     for i in range(1,int(n)+1):
#         if n%i==0:
#             c += 1
#     if c==2:
#         return True
#     else:
#         return False

# num = 48
# fac = []
# primfac = []
# for i in range(1,num+1):
#     if num%i == 0:
#         fac.append(i)
#         if isPrime(i):
#             primfac.append(i)
# print(fac, primfac)