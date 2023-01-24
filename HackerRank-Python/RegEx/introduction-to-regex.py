# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    S = input()
    if len(re.findall(r'^[+-]{0,1}[0-9]{0,}[.][0-9]+$',S)) == 1:
        print('True')
    else:
        print('False')

# 10
# .7
# 0.7
# +1.7
# -1.7
# somthing
# -.7
# 12.0
# 12.
# 5
# 8.
# +4.50
# -1.0
# .5
# -.7
# +.4
# -+4.5
# 12.
# 12.0
# 4
# 4.0O0
# -1.00
# +4.54
# SomeRandomStuff