import numpy as np
arr = np.arange(10)
print(arr[2:7:2])# same as arr[slice(2,7,2)]

a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a)
print(a[1:,1:])
print(a[1:])

a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
print("\na\n",a)
print("\na[...,1]\n",a[...,1])
# print("\na[1,...]\n",a[1,...])
print("\na[1,:]\n",a[1,:])
print("\na[...,1:]\n",a[...,1])
print("\na[1:,1:]\n",a[1:,1:])