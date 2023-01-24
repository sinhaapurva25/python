import numpy as np
print("Numpy","\n")
output = np.ones((7, 7))
# print(output)

z = np.zeros((5, 5))
z[2, 2] = 5
print(z)
output[1:-1, 1:-1] = z
print(output)

a = np.array(([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
b = np.max(a, axis=0).sum() #axis 0 is rows, axis 1 is column
print(b)


grid = np.array([
[0,2],[1,0],
[0,1],[0,-1]])
coord = np.where(grid == 2)
print(coord)
# Grab x axis coordinates with coord[0][0]
# Add 1 t y axis to resemble coordinates more
coord_to_set = (coord[0][0], coord[1][0] + 1)
# prints (0,2)
print(str(coord_to_set))


# 1:
# filedata = np.genfromtxt('data.txt', delimiter=',')
# output = np.all(filedata < 50, axis=1)
# print(output)

# 2:
# filedata = np.genfromtxt('data.txt', delimiter=',')
# output = np.any(filedata < 50)
# print(output)

# 3:
# filedata = np.genfromtxt('data.txt', delimiter=',')
# output = filedata[filedata < 50]
# print(output)

