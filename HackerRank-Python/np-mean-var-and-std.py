import numpy
N,M = map(int,input().split())
my_array = list()
for i in range(N):
    my_array.append(list(map(int,input().split())))
# np_my_array = numpy.array(my_array)
print(numpy.mean(my_array,axis=1))
print(numpy.var(my_array,axis=0))
# numpy.set_printoptions(legacy='1.13')
# numpy.around(my_array,decimals=11)
# print(numpy.std(my_array))
print(round(numpy.std(my_array), 11))
