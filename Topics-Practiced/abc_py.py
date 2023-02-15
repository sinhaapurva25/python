import abc


class Shape(abc.ABC):

    @abc.abstractmethod
    def area(self): pass

    @abc.abstractmethod
    def perimeter(self): pass


class Square(Shape):

    def __init__(self, a):
        self.__a = a

    def area(self):
        return self.__a * self.__a

    def perimeter(self):
        return 4 * self.__a



class Circle(Shape):

    def __init__(self, a):
        self.__a = a

    def area(self):
        return 3.14 * self.__a * self.__a

    def perimeter(self):
        return 2 * 3.14 * self.__a


square = Square(5)
print(square.area(), square.perimeter(), square.__dict__, square.__class__)
circle = Circle(5)
print(circle.area(), circle.perimeter(), circle.__dict__, circle.__class__)
