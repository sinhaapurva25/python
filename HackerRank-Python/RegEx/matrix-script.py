matrix=[r'Tsi', r'h%x', r'i #', r'sM ', r'$a ', r'#t%', r'ir!']
m,n=7,3

import re
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
s = ''
for i in range(m):
    for j in range(n):
        print(matrix[j][i])
print(re.sub(r'(?<=[a-zA-Z0-9_])([^A-Za-z_]+)(?=[a-zA-Z0-9_])', ' ', s))

# print(re.sub(r'(?<=[a-zA-Z0-9_])(^[A-Za-z]+)(?=[a-zA-Z0-9_])',' ',s))
# print(re.sub(r"(?<=\w)(^\W)(?=\w)", ' ', s))
print(re.sub(r'(?<=[a-zA-Z0-9_])([\W]+)(?=[a-zA-Z0-9_])', ' ', s))