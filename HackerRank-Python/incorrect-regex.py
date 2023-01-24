# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())
lst = list()
for i in range(N):
    S = input()
    try:
        re.compile(S)
        valid = True
    except Exception:
        valid = False
    lst.append(valid)
[print(i) for i in lst]