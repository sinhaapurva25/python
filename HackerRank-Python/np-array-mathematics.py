import numpy
numpy.set_printoptions(legacy='1.13')
N,M = [int(i) for i in input().split()]

A  = []
for i in range(0,N):
    row_elements = [int(i) for i in input().split()]
    row = []
    for j in range(0,M):
        row.append(row_elements[j])
    A.append(row)

B  = []
for i in range(0,N):
    row_elements = [int(i) for i in input().split()]
    row = []
    for j in range(0,M):
        row.append(row_elements[j])
    B.append(row)

A = numpy.array(A, float)
B = numpy.array(B, float)

print(numpy.array(A + B,int))
# print(numpy.add(A, B))

print(numpy.array(A - B,int))
# print (numpy.subtract(A, B))

print (numpy.array(A * B,int))
# print (numpy.multiply(A, B))

print (numpy.array(A / B,int))
# print (numpy.divide(A, B))

print (numpy.array(A % B,int))
# print (numpy.mod(A, B))

print (numpy.array(A**B,int))
# print (numpy.power(A, B))