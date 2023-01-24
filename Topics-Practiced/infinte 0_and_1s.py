arr = [0,0,0,0,0,0,0,0,1,1,1,1,1,1]
i = 0
k = True
while(True):
    if arr[i]==1:
        print("first index of 1 at",i)
        break
    i += 1

import numpy
k = lambda x: x+3
print(k(6))
print('   surname   '.join(['apurva', 'sinha']))
print(numpy.add([1,2,3],[3]))
print([3,2,4].index(3,0))

# class Beer:
#     func1input1 = 0
#     func1input2 = 'apurva'
#     def __init__(self,input1,input2):
#         self.input1 = input1
#         self.input2 = input2
#     def func1(self,func1input1,func1input2):
#         self.func1input1 = 1
#         self.func1input2 = 'sinha'
#         return [func1input1,func1input2]
# a = Beer(12,78).func1()
# print(a)

# print(list(map(lambda x,y: x[0:5]+'_'+y,['apurva','sinha','qwertyu','iopuyklh'],'asqi')))
print(list(filter(lambda x: True if x>17 else False,[1,15,17,18,0,-1,34,78])))
print(list(map(lambda x: str(ord(x))+'_'+str(ord(x.upper())),'abcdefghijklmnopqrstuvwxyz')))
print(r'\t \n 42 \n'.strip())
print('\t \n 42 \n'.strip())
print(sorted([8,3,2,42,5]))
print(sorted(['8','3','2','42','5']))
print(sorted([8,3,2,42,5],key=lambda x: 0 if x==42 else x))
print(help(''))
print(list(enumerate(['apurva','sinha','qwerty','uiop'])))
# import antigravity
# import this
def func(arr):
    sum = 0
    for i in arr: sum += i
    return sum
print(func([1,2,3]))

## merginf dicts
x = {'Apurva':0}
y = {'Sinha':1,'Phone':91}
print({**x,**y})

##extended unpacking
a,*b = [0,1,2,3,4,5,6]
print(a,b)