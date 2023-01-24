class Pizza(object):
    def __init__(self):
        self.toppings = []

    def __call__(self, topping):
        # When using '@instance_of_pizza' before a function definition
        # the function gets passed onto 'topping'.
        self.toppings.append(topping())

    def __repr__(self):
        return str(self.toppings)


@Pizza()
def cheese():
    return 'cheese'
@Pizza()
def sauce():
    return 'sauce'

pizza = Pizza()
print(pizza)
# ['cheese', 'sauce']