def func(arr1, arr2):
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr2[j] > arr1[i]:
            arr1[i] ^= arr2[j]
            arr2[j] ^= arr1[i]
            arr1[i] ^= arr2[j]
            j += 1
        else:
            i += 1
    print(arr1, arr2)

func([1,5,9,10,15,20],[2,3,8,13])
func([2,3,8,13], [1,5,9,10,15,20])
