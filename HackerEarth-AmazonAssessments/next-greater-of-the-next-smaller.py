# 7
# 5 1 9 2 5 1 7
# 9 -1 5 7 7 -1 -1
# N = int(input())
# arr = list(map(int,input().split()))
N = 7
arr = [5, 1, 9, 2, 5, 1, 7]
maxx_arr = list()
print(arr)
for i in range(N):
    el = arr[i]
    subset = arr[i+1:]

    minn = -1
    idx_subset = -1
    if len(subset) > 0:
        minn = min(subset)
        if not(minn < el):
            minn = -1
            idx_subset = -1
        else:
            idx_subset = subset.index(minn)
    
    if minn > -1:
        subset2 = subset[idx_subset+1:]
        subset2 = subset
        if len(subset2) == 0:
            maxx = -1
        else:
            maxx = max(subset2)
            # if i == 2: print(maxx)
            if not(maxx > minn):
                maxx = -1
        maxx_arr.append(maxx)
    else:
        maxx = -1
        maxx_arr.append(maxx)
    print(el,subset,minn,idx_subset,maxx)
# print(maxx_arr)