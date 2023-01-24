class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        print("Tr")
class Triangle2:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        print("Tr2")
class Triangle3(Triangle,Triangle2):
    super().__init__()
p = Triangle3()
p(23,34)