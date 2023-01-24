import datetime
print(datetime.datetime.now().strftime("%H:%M:%S"))

def my_function():
	'''Demonstrates triple double quotes
	docstrings and does nothing really.'''

	return None

print(my_function.__doc__)

# print(help(my_function))
# help(my_function)