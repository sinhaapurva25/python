import numpy
numpy.set_printoptions(legacy='1.13')
user_input = [int(i) for i in input().split()]
print(numpy.eye(user_input[0], user_input[1]))