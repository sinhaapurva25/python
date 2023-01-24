# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def checkConditions(S):
    a = len(re.findall(r'\s',S))==0
    # b = len(re.findall(r'^[456][0-9]{3,3}[-]*[0-9]{4,4}[-]*[0-9]{4,4}[-]*[0-9]{4,4}$',S))==1
    b = len(re.findall(r'^[456][0-9]{3,3}[-]{0,1}[0-9]{4,4}[-]{0,1}[0-9]{4,4}[-]{0,1}[0-9]{4,4}$',S))==1
    c = len(re.findall(r'(\d)\1{3}',re.sub(r'-','',S)))==0

    return a and b and c

for _ in range(int(input())):
    S = input()
    if checkConditions(S):
        print('Valid')
    else:
        print('Invalid')