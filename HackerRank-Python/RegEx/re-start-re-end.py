# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
S = 'aaadaa'#input()
# S = 'kkkk'#input()
k = 'aa'#input()
flag = 0
for _ in re.finditer('(?=('+k+'))', S):
    flag = 1
    print((_.start(),_.start()+len(k)-1))
if flag == 0:
    print((-1,-1))