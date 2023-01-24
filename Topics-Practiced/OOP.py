class A:
    def __init__(self):
        print("classA().init()")
    def funcA(self):
        print("classA().funcA()")
class C:
    def __init__(self):
        print("classC().init()")
class B(A,C):
    c = 0
    def __init__(self):
        print("classB().init()")
        self.c = 0
        # super().__init__()
        super(B,self).__init__()
    def funcB(self):
        print("classB().funcB()")
        ## self.funcB()
        ## self.c += 1
        ## print(self.c)
obj = B
B().funcB()
# print(isinstance("Hello",(float,int,str,list,dict,tuple)))