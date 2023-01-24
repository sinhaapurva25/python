import numpy
import time
# print(numpy.array([1.1, 2.2, -1]).astype('intc'))


# dt = numpy.dtype('i4')
# print(dt)
# #or

# dt = numpy.dtype('int32')
# print(dt)

# dt = numpy.dtype([('age',numpy.int8)]) 
# print(dt)

dt = numpy.dtype([('age',numpy.int8)]) 
a = numpy.array([i for i in range(256)], dtype = dt) #if i > 25
print(a)