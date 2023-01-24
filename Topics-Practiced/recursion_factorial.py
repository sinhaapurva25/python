def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def find_power(a, b):
    if b == 0:
        return 1
    else:
        return a * find_power(a, b-1)

fact = factorial(4)
fib = fibonacci(4)
fin_pow = find_power(2,2)
print(fact,fib,fin_pow)