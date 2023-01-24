import re
for _ in range(int(input())):
    match = re.findall(r'(#[A-Fa-f0-9]{3,6}){1,2}[^\s]',input())
    for x in match:
        print(x)