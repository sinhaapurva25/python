class Parent1:
	def show(self):
		print("Inside Parent1 class")

class Parent2:
	def show(self):
		print("Inside Parent2 class")

class Child(Parent1,Parent2):
    def disp(self):
        print("")
apurva = Child()
apurva.show()
apurva.show()