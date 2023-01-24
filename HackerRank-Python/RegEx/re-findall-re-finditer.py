# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
# S = input()
S = 'apurva'
match = re.findall(r'([aeiouAEIOU+-]+)[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]',S)
match = re.findall(r'^a\w+',S)
# You can use either Line 4 or 5
flag = 0
for vowel in match:
    if len(vowel) > 1:
        flag = 1
        print(vowel)
if flag == 0:
    print('-1')

print(re.search(r'ma*n','man'))