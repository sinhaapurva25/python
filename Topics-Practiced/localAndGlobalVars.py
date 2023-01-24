a = 5
class myClass():
    def func():
        a = 10
        return a
    def checkA():
        return a
print(a)
obj = myClass
print(myClass.func())
print(myClass.checkA())


'''
printf("%d", 5/2);
print(5//2)
print(5/2)
'''

# import functools
# print(functools.reduce(lambda a, b: a+b, [3,4,5]))