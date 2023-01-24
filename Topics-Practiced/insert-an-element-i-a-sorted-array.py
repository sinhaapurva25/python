def insert_element(arr,element):
    arr.sort()
    u = arr.copy()
    for i in range(len(arr)):
        if i == 0:
            if element <= arr[i]:
                u = [element] + arr
                break
            elif element in range(arr[i-1],arr[i]):
                u = [arr[i]] + [element] + arr[i+1:]
                break
        elif i == len(arr) - 1:
            if element in range(arr[i-1],arr[i]):
                u = arr[:i] + [element] + [arr[i]]
                break
            elif element >= arr[i]:
                u = arr + [element]
                break
        else:
            if element in range(arr[i-1]-1,arr[i]+1):
                u = arr[:i] + [element] + arr[i:]
                break
    return u
print(insert_element([9,12,13,14],0))
print(insert_element([9,12,13,14],15))
print(insert_element([9,12,13,14],10))
print(insert_element([9,12,13,14],12))
print(insert_element([14,13,12,11],12))