my_list_1 = [5, 6, 7, 8]
my_list_2 = [1, 2, 3, 4]
for idx,(el1,el2) in enumerate(zip(my_list_1,my_list_2),ord('z')):
    print("idx",idx,el1,el2)
print("apurva "*7)

for el, (a,b) in enumerate(zip([1,2],[2,3]),-99):
    print(el,a,b)

# k = [1,2,3]
# l = ['q','w','e']
# m = [True,False,True]
# print(list(zip(k,l,m)))