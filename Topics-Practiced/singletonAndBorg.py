# http://foobarnbaz.com/2010/10/06/borg-pattern/

# Singleton
class Singleton(object):
    def __new__(type):
        if not '_the_instance' in type.__dict__:
            type._the_instance = object.__new__(type)
        return type._the_instance

class Foo1(Singleton):
    pass

foo1 = Foo1()
bar1 = Foo1()
print(id(foo1), id(bar1))


# Borg Pattern
class Borg:
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state
class Foo2(Borg):
    pass

foo2 = Foo2()
bar2 = Foo2()
print(id(foo2), id(bar2))