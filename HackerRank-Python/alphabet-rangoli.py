def print_rangoli(size):
    arr = []
    for i in range(size,0,-1):# for i in range(0,size):
        row = ''
        for j in range(size,i-1,-1):
            row += chr(j+64).lower()
        arr.append(row+row[::-1][1:])
    lowerRows = arr[::-1][1:]
    for j in lowerRows:
        arr.append(j)
    # print(*arr,sep='\n')
    Arr = []
    width = 0
    for i in arr:
        row = ('-').join(i)
        Arr.append(row)
        if len(row)>width:
            width = len(row)
    arr.clear()
    arr = str()
    for i in Arr:
        row = i.center(width,'-')
        arr = arr + row + '\n'
    print(arr)
# n = int(input())
# print_rangoli(n)
for i in range(5,0,-1):
    print(i)