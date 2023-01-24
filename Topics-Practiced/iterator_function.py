class Test:

	def __init__(self, limit):
		self.limit = limit

	def __iter__(self):
		self.x = 10
		return self

	def __next__(self):

		x = self.x

		if x > self.limit:
			raise StopIteration

		self.x = x + 1;
		return x

# Prints numbers from 10 to 15
for i in Test(15):
	print(i)

# Prints nothing
for i in Test(5):
	print(i)

class Human:
    m = 0
    n = 9
    pass