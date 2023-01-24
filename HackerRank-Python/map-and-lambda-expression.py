cube = lambda x: x*x*x # complete the lambda function 

def fibonacci(n):
    a = -1
    b = 1
    lst = list()
    for i in range(n):
        lst.append(a+b)
        temp = a+b
        a = b
        b = temp
    return lst

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))