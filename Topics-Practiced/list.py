from numpy import MAY_SHARE_BOUNDS
import random
import numpy as np

def my_function():
    fruits = [0, 1, 2]
    quantities = [5, 3, 4]
    prices = [1.50, 2.25, 0.89]
    
    # i = 0
    # output = []
    # for fruit in fruits:
    #     temp_qty = quantities[i]
    #     temp_price = prices[i]
    #     output.append((fruit, temp_qty, temp_price))
    #     i += 1

    print([*zip(fruits, quantities, prices)])
    print(list(zip(fruits,quantities, prices)))
    output = list(zip(fruits,quantities, prices))
    return output

print(my_function())

def func1():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    string_letters = str(letters)
    lists_letters = list(letters)
    tuples_letters = tuple(letters)
    sets_letters = set(letters)
    print("Sets: ", sets_letters)

    list_example = [0,'q',True,0.0]
    set_example = set(list_example)
    print(list_example,set_example)

class sorting:
    my_list = np.array([])
    def __init__(self):
        self.my_list = np.array([3,1,14,14,6,0,4,12,-1,7,20,14])
        self.my_list.shape = (3,4)
    def arr(self):
        return self.my_list
    def ax(self):
        self.my_list.sort()
        return self.my_list
    def ax0(self):
        self.my_list.sort(axis=0)
        return self.my_list
    def ax1(self):
        self.my_list.sort(axis=1)
        return self.my_list
    def setColor(self, color):
        self.color = color  
    def getColor(self):    
        return self.color
classCall = sorting()
## print(classCall.arr())
## print(classCall.ax())
## print(classCall.ax0())
# print(classCall.ax1())

# print("5<6") if 5<6 else print("6>5")