import numpy
N_and_M = [int(i) for i in input().split()]
N = N_and_M[0]
M = N_and_M[1]
arr = []
for i in range(0,N):
    row = [int(j) for j in input().split()]  
    arr.append(row)
print(numpy.transpose(arr))
print(numpy.array(arr).flatten())