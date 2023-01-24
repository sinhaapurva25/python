import numpy as np

# def ex1():
#     print("ex1()")
#     x = np.array([[1, 2], [3, 4], [5, 6],[7,8],[9,10]])
#     print(x)
#     y = x[[2,3,0,1,1,1,2], [0,1,0,0,1,0,1]]
#     print(y)
# ex1()
# def ex2():
#     print("ex2()")
#     x = np.array([[ '00',  '01',  '02'],[ '10',  '11',  '12'],[ '20',  '21', '22'],[ '30', '31', '32']])
#     rows = np.array([[0,0],[3,3]])
#     cols = np.array([[0,2],[0,2]]) 
#     y = x[rows,cols]
#     print(x)
#     print(y)
#     z = x[[[0,0],[3,3]],[[0,2],[0,2]]]
#     print(z)
# ex2()
# def ex3():
#     x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])
#     print(x[1:4,1:3])
#     print(x[1:4,[1,2]])
# ex3()
# def boolean_array_indexing():
#     x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])
#     print(x > 5)
#     print(x[x > 5])
# boolean_array_indexing()
# def isnan_func():
#     a = np.array([np.nan, 1,2,np.nan,3,4,5])
#     print(~np.isnan(a))
#     print (a[~np.isnan(a)])
# # isnan_func()
# def iscomplex_func():
#     a = np.array([1, 2+6j, 5, 3.5+5j]) 
#     a = np.array([1+1j, 2+6j, 5+1j, 3.5+5j])
#     print(a)
#     print(a[~np.iscomplex(a)])
# # iscomplex_func()

# k = lambda x: x+5
# print(k(5))
# print(list(map(lambda x: x+5,[1,2,3,4,5])))
# print(map(lambda x: x+5,[1,2,3,4,5]))
# import numpy as np
# print(np.lcm.reduce(np.array([4, 1, 3, 5, 2])))

# a = []
# b = []
# k=l=[]
# print(id(k),id(l))
# print(a==b,id(a),id(b))
# print(a==k,a==l,b==k,b==l,id(k),id(l))
# a = []
# a.append(a)
# a.append(a)
# a.append(a)
# print(a)
# print(a[1])

import numpy
import time

def jpmorgan():
    x = 100000
    l1 = range(x)
    l2 = range(x)
    a1 = numpy.arange(x)
    a2 = numpy.arange(x)
    start = time.time()
    result = [(x,y) for x,y in zip(l1,l2)]
    print((time.time()-start)*1000)

    start = time.time()
    result = [a1+a2]
    print((time.time()-start)*1000)

# jpmorgan()

print([i for i in range(10)])
print([i for i in np.arange(10)])
print(list(zip(range(10),range(11,21))))
print([(x,y) for x,y in zip(range(10),range(11,21))])

def apurva():
    x=1000000
    l1 = range(x)
    l2 = range(x)
    np1 = numpy.arange(x)
    np2 = numpy.arange(x)

    start = time.time()
    l = [l1[i]+l2[i] for i in range(x)]#l = [l1[i]+l2[i] for i in l1]
    # print(l)
    lt = time.time()-start

    start = time.time()
    np = np1+np2
    # print(np)
    npt = time.time()-start

    print(lt/npt)

    l1 = [i for i in range(5)]
    l2 = [i for i in range(5,10)]
    for i in range(len(l2)):
        l1.append(l2[i])
    print(l1)

# apurva()
print(type(range(5)))
print(len(numpy.arange(5)))
numpy.random.seed(0)
print(numpy.random.randint(7,90))

# k = 5
# while(k>0):
#     k -= 1
#     continue
# print(k)

print(42 in [45,42,42,56,78,42])
k = [3]
print('u are here',id(k), id(k), [3] is [3])


def func(x):
	return x % 7
L = [15, 3, 11, 7]
print("Normal sort :", sorted(L))
print("modulus :", [func(i) for i in L])
print("Sorted with key:", sorted(L, key=func))