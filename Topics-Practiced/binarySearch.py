def bS(x, num):
    beg = 0
    end = len(x)-1
    flag = 0
    while(beg<=end):
        mid = int((beg+end)/2)
        if x[mid] == num:
            print(num, 'found at index', mid)
            flag = 1
            # break
        elif num < x[mid]:
            end = mid - 1
        else:
            beg = mid + 1
    if flag == 0:
        print(num, 'not found in', x)


x = [-7, 0, 2, 4, 9]

bS(x, -7)
bS(x, 11)