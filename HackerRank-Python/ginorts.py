S = input()
low = list()
upp = list()
odd = list()
eve = list()
for i in S:
    if i.islower():
        low.append(ord(i))
    if i.isupper():
        upp.append(ord(i))
    if i.isdigit():
        if int(i)%2 == 0:
            eve.append(int(i))
        else:
            odd.append(int(i))
lowSorted = ''.join(x for x in list(map(chr,sorted(low))))
uppSorted = ''.join(x for x in list(map(chr,sorted(upp))))
oddSorted = ''.join(str(x) for x in sorted(odd))
eveSorted = ''.join(str(x) for x in sorted(eve))
print(lowSorted+uppSorted+oddSorted+eveSorted)