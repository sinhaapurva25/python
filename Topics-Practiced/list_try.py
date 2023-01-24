import numpy as np
import sys

pos = []
for i in range(5):
    pos.append("-")
# print(pos,np.array([pos]))
fruit_cluster_arr = []
for i in range(5):
    fruit_cluster_arr.append([2,2,2,2,2])

rows, cols = (5, 5)
fruit_cluster_arr = [[0]*cols]*rows
print("fruit_cluster_arr",fruit_cluster_arr)

empty_array = np.empty((5, 5), '')
print("empty_array",empty_array)
print("empty_array[0][1]",sys.getsizeof(empty_array[0][1]),"end")

fruit_cluster_arr = [[(str(j)+str(i)) for i in range(cols)] for j in range(rows)]
print("fruit_cluster_arr\n",np.array(fruit_cluster_arr))
fruit_cluster_arr = [[[] for i in range(cols)] for j in range(rows)]

list = [12, 13,14]
print(list.pop())