# https://www.programiz.com/python-programming/methods/built-in/super
# https://rhettinger.wordpress.com/2011/05/26/super-considered-super/
class Parent1:
	def __init__(self):
		print("Inside Parent1 class")

class Parent2:
	def __init__(self):
		print("Inside Parent2 class")

class Child(Parent2,Parent1):
    def __init__(self):
        super().__init__()
        ## is equivalent to:
        # super(Child, self).__init__()
        print('Apurva')
apurva = Child()

class Animal(object):
  def __init__(self, animal_type):
    print('Animal Type:', animal_type)
    
class Mammal(Animal):
    # pass
  def __init__(self):

    # call superclass
    super().__init__('Mammal')
    print('Mammals give birth directly')    
# dog = Mammal()