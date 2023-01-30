import re

def timeConversion(s):
    # Write your code here
    pat = r'(\d+)(:\d+:\d+)([A,P]M)'
    match = re.search(pat,s)
    # print(match.group(1),match.group(2),match.group(3))
    if match:
        if match.group(3)=='PM':
            if int(match.group(1)) >= 12:
                res = match.group(1)+match.group(2)
            else:
                res = str(int(match.group(1))+12)+match.group(2)
        else:
            if match.group(1) == '12':
                res = '00'+match.group(2)
            else:
                res = match.group(1)+match.group(2)
    return res

print(timeConversion('12:01:00PM'))
print(timeConversion('12:01:00AM'))
print(timeConversion('06:40:03AM'))