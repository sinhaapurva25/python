from decorator_python_1 import do_twice  
# @do_twice  
# def display(name):  
#      print(f"Hello {name}")

@do_twice  
def display(*name):
# '*' is used for list
      print("Hello {}".format(name))
display('apurva')