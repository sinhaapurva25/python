class Triangle1:
    def funcName(self):
        print("Tr1")
class Triangle2:
    def funcName(self):
        print("Tr2")
class Triangle3:
    def funcName(self):
        print("Tr3")
class Triangle4(Triangle2,Triangle1,Triangle3):
    pass
p = Triangle4()
p.funcName()