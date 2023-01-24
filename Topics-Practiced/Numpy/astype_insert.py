import numpy
import time
def astype():
    print(numpy.array([1.1, 2.2, 3.3]).astype('int'))
    # print(numpy.asarray([1.1, 2.2, 3.3],astype('int')))
    print(int(3.14))
def insert():
    arr = numpy.array([[1,2],[3,4],[5,6],[7,8]])
    print(numpy.insert(arr,1,11))
    print(numpy.insert(arr,-4,[11],axis=0))
    print(numpy.insert(arr,1,[11],axis=1))

    a = numpy.array([1,2,3,4,5,6,7,8,9,10])
    print(a[::2])
    print(numpy.delete(a, numpy.s_[::2]))
    print(numpy.delete(a, ~a[::2]))
astype()