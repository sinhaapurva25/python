def add(x, to=1):
  return x + to

def divide(x, by=2):
  return x/by

def square(x):
  return x**2

def invalid_op(x):
  raise Exception("Invalid operation")

def perform_operation(line, case):
  # If operation_args wasn't provided (i.e. it is None), set it to be an empty dictionary
  
  ops = {
    "add": add,
    "divide": divide,
    "square": square
  }
  
  chosen_operation_function = ops.get(case, invalid_op)
  
  return chosen_operation_function(line)
  
def example_usage():

  line = 1
  print(perform_operation(line, "add"))

  line = 1
  print(perform_operation(line, "add"))

  line = 1
  print(perform_operation(line, "divide"))

  line = 1
  print(perform_operation(line, "square"))


example_usage()