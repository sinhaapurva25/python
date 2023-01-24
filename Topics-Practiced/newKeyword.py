class Car:
    attr = 0
    def __init__(self,attr):
        print("init")
        self.attr = attr
    def __new__(cls, *args, **kwargs):
        print("I am in the __new__() method.")
        # return super(Car, cls).__new__(cls)
obj = Car(89)
print(id(obj))
del obj
obj2 = Car(90)
print(id(obj2))
list = [12,23]
print(list)
print(id(list))
print(list.clear())