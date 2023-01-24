import re
lst = list()
N = int(input())
for i in range(N):
    lst.append('YES') if bool(re.match(r'[789]\d{9}$',input()))==True else lst.append('NO')
[print(i) for i in lst]