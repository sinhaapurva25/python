import numpy
N,M = [int(i) for i in input().split()]
arr = []
for i in range(0,N):
    row = [int(j) for j in input().split()][:M]
    arr.append(row)
print(numpy.prod(numpy.sum(numpy.array(arr),axis=0),axis=None))