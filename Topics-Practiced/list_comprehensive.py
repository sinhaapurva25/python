# import math
# for i in range(1,5):
#     for j in range(1,4):
#         print(math.pow(i,j))
# print([int(math.pow(i,j)) for i in range(1,5) for j in range(1,4)])

list1 = [10, 11, 12, 13, 14] 
list2 = [20, 30, 42]
print([j for i in [list1,list2] for j in i])

generator = (i*i for i in range(0, 5))
print(list(generator))
for i in list(generator):
    print(i)