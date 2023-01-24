import numpy as np 
x = np.arange(10,20,2) 
print(x)

import numpy as np 
print(np.linspace(10,20, 5, endpoint = False,retstep = True) )
print(np.linspace(10,20, 5, retstep = True))

print(np.logspace(start=1,stop=5,num=5,endpoint=True,base=2,dtype=int))