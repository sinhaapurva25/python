class Base(object):
    def __init__(self):
        print("Base created")

# class ChildA(Base):
#     def __init__(self):
#         Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__()
        super().__init__()
        Base.__init__(self)

# ChildB()
import random
k = ['Enthusiastic', 'responsible', 'goal-oriented', 'ambitious', 'driven', 'passionate', 'polite', 'inquisitive', 'motivated', 'responsible', 'assertive', 'fun-loving', 'committed', 'articulate']
random.shuffle(k)
print(k)
print(random.shuffle(['0',89,90]))