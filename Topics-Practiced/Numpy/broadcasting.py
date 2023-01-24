import numpy as np
import warnings


def ex2():
    a = np.array([
                 [0.0,0.0,0.0],
                 [10.0,10.0,10.0],
                 [20.0,20.0,20.0],
                 [30.0,30.0,30.0]
                 ]) 
    b = np.array([1.0,2.0,0.0])# same as # np.array([[1.0,2.0,3.0],[1.0,2.0,3.0],[1.0,2.0,3.0],[1.0,2.0,3.0]])
    print(a/b)
try:
    ex2()
except:
    pass