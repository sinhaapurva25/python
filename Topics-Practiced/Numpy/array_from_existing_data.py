import numpy as np 

x = [1,2,3] 
a = np.asarray(x) 
print(a)

x = [1,2,3]
a = np.asarray(np.arange(20,101,20), dtype = float)
print(a)

x = (1,2,3) 
a = np.asarray(x)
# print(a)

x = [(1,2,3),(4,5,6)] 
a = np.asarray(x)
# print(a.shape)

s = b'Hello World'
a = np.frombuffer(s, dtype = 'S1')
# print(a)
a = u'helló wörld from example'
# print(a.encode('utf-8'))

list = range(5)
# print(list)
it = iter(list)
x = np.fromiter(it, dtype = float) 
# print(x)