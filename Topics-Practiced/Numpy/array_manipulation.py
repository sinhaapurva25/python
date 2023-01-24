import numpy as np

def np_flatten(a):
    print(id(a.flatten()))
    print(id(a.flatten(order = 'C')))#row major
    print(id(a.flatten(order = 'F')))#column major
    print(id(a.flatten(order = 'K')))#memory
print("------")
def np_ravel(a):
    print(id(a.ravel()))
    print(id(a.ravel(order = 'C')))#row major
    print(id(a.ravel(order = 'F')))#column major
    print(id(a.ravel(order = 'K')))#memory
def transpose(a):
    print(np.transpose(a))
    print(a.T)
def swap_axis(a):
    arr = a=np.arange(2*3*4).reshape(2, 3, 4)
    print(arr)
    arr_swap = arr.swapaxes(0, 2)
    # arr_swap_1 = arr.swapaxes(2, 0)
    # print(arr_swap==arr_swap_1)
    print(arr_swap.shape)
    print(arr_swap)
def rol_axis():
    arr = np.array((1,2,3,4))
    gfg = np.rollaxis(arr, 3, 1)
    print (gfg)
a = np.arange(100,110,1)
a = a.reshape(2,5)
# print(a)
# print(a.flat[:])
# transpose(a)
# swap_axis(a)
rol_axis()