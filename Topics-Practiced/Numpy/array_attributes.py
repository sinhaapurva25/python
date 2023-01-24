import numpy as np 
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)#[0],a.shape[1])
# a.shape = (3,2) 
# print(a)
print(a.reshape(3,2))
print(a.ndim)

a = np.arange(24)
print(a)
print(a.reshape(2,2,3,2))
print(a.itemsize)#4 bytes
print(a.flags)
x = np.ones(5) 
print(x)
x = np.ones([2,2], dtype = 'uint8') 
print(x.itemsize)
print(np.array([1.78,2.8888,3.03487878,4.3434454545454545],dtype='float'))