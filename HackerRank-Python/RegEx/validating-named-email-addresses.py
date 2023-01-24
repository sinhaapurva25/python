# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
res = list()
for i in range(int(input())):
    S = input()
    # match = re.match(r'^[A-Za-z][A-Za-z0-9\-\.\_]+@[A-Za-z]+\.[A-Za-z]{1,3}$',S.split()[1][1:-1])
    # OR
    match = re.match(r'^[A-Za-z][A-Za-z0-9-._]+@[A-Za-z]+\.[A-Za-z]{1,3}$',S.split()[1][1:-1])
    if match:
        res.append(S)
[print(i) for i in res]