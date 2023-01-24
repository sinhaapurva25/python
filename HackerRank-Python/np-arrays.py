import numpy

def arrays(arr):
    return numpy.array(arr[::-1],dtype='float')

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
