import numpy
numpy.set_printoptions(legacy='1.13')
arr = [float(i) for i in input().split()]
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))