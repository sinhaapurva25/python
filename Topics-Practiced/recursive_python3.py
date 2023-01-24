import datetime
print(datetime.datetime.now().strftime("%H:%M:%S"))
def count_recursive(n=1):
    if n > 3:
        return
    print(2)

count_recursive()

print(9/3)
num_list =[21,13,19,3,11,5,18]
num_list.sort()
print(num_list[len(num_list)//2])

# Q97. What is the correct syntax for calling an instance method on a class named Game?
#  my_game = Game(self) self.my_game.roll_dice()
#  my_game = Game() self.my_game.roll_dice()
#  my_game = Game() my_game.roll_dice()
#  my_game = Game(self) my_game.roll_dice(self)

import numpy as np
a = np.array([1,2,3,4])
print(a[False, True, False, False])

print("stuff;thing;junk;".split(';'), len("stuff;thing;junk;".split(';')))