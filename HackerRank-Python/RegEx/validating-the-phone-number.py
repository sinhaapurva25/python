import re
import re
lst = list()
for _ in range(int(input())):
    number = input()
    lst.append('YES') if bool(re.search(r'^[789][0-9]{9,9}$',number)) else lst.append('NO')
[print(i) for i in lst]