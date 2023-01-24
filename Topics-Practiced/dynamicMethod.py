from venv import create


class Robot:
    counter = 0
    def __init__(self, name):
        self.name = name
    def sayHello(self):
        return "Hi, I am " + self.name
def Rob_init(self, name):
    self.name = name
Robot2 = type("Robot2", 
              (), 
              {"counter":0, 
               "__init__": Rob_init,
               "sayHello": lambda self: "Hi, I am " + self.name})
"""
x = Robot2("Marvin")
print(x.name)
print(x.sayHello())

y = Robot("Marvin")
print(y.name)
print(y.sayHello())

print(x.__dict__)
print(y.__dict__)
"""
class Humans:
    x = 0
    y = 0
    def __init__(self) -> None:
        pass
    def create(self):
        print("create")
    def create2(self):
        print("create2")
Apurva = Humans()
Apurva.create
Apurva.create2
# delattr(Apurva,'x')
# setattr(Apurva, 'surname','Sinha')
# print(hasattr(Apurva,'surname'))

class Example(object):
	def __init__(self):
		print("Example Instance.")
	def __delete__(self, instance):
		print ("Deleted in Example object.")
class Foo(object):
	exp = Example()
f = Foo()
del f.exp

def f(x,y,z):
    print(x+y*z)
f(*[1,2,3])
f(**{'z':1,'x':2,'y':3})