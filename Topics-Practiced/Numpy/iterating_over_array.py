import numpy as np
def ex1():
    a = np.arange(0,60,5)
    print("a",a)
    a = a.reshape(3,4)
    print("a.reshaped",a)
    b = a.T
    print("b",b)

    for x in np.nditer(a):
        print(x)

    c = a.copy(order = 'C')
    print("c",c)
    for x in np.nditer(c):
        print(x)
ex1()