class A:
    def __init__(self):
        print("__init__ of A")
    def funcA():
        print("class A funcA")
class B(A):
    def __init__(self):
        # print("__init__ of B")
        super(B, self).__init__()
        print("super(B, self).__init__()")
        super().__init__()
        print("super().__init__()")
        A.__init__(self)
        print("A.__init__(self)")
    def funcA():
        print("class B funcA")
    def funcB():
        print("class B funcB")
objB = B()
# B.__init__(objB)
# B.funcB()
# B.funcA()