CSS = list()
N = int(input())
for j in range(N):
    line = input().split()
    # print(line)
    for i in line:
        firstHalf = ''
        secondHalf = ''
        firstHalfisTrue = False
        secondHalfisTrue = False
        if i[0]=='#' and len(i) > 4:
            # print(i)
            l = i[1:].strip(',')
            l.strip(';')
            l.strip(')')
            l.strip(';')
            print(l)
            for h in l:
                if h.isdigit() or h=='a' or h=='b'or h=='c' or h=='d' or h=='e' or h=='f' or h=='A' or h=='B' or h=='C' or h=='D' or h=='E' or h=='F':
                    pass
print(CSS)