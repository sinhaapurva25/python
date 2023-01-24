import numpy
N,M = [int(i) for i in input().split()][0:2]
arr = []
for i in range(N):
    row = [int(j) for j in input().split()][:M]
    arr.append(row)
print(numpy.max(numpy.min(numpy.array(arr),axis=1)))