import re

S = '..12345678910111213141516171820212223' # input()
# S = '123456789'
# S = 'butter butterfly buttermilk'
match = re.findall(r'([0-9A-Za-z])\1+',S)
print(match[0]) if match else print(-1)