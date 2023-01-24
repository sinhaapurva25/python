with open(r'C:\myWork\GitHub\python\Topics-Practiced\bst_levels.txt', 'r') as f:
    fl = f.readlines()
for idx,i in enumerate(fl):
    if i.strip().split(':')[0] == '5':
        break
# print(idx)
for idx2,i in enumerate(fl[::-1]):
    if i.strip().split(':')[0] == '5':
        break
# print(idx2)
print(idx2-idx+1)