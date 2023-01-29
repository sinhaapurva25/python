def binary_search(arr, element, start, end):
    if start <= end:
        mid = (start+end)//2

        if mid < 0 or mid > len(arr)-1:
            return -1

        if element == arr[mid]:
            return mid
        elif element < arr[mid]:
            end = mid - 1
            return binary_search(arr, element, start, end)
        else:
            start = mid + 1
            return binary_search(arr, element, start, end)

    return -1



arr = [2, 5, 8, 9, 10, 12, 15, 16]

print(binary_search(arr,10,0,len(arr)))
print(binary_search(arr,15,0,len(arr)))
print(binary_search(arr,16,0,len(arr)))
print(binary_search(arr,32,0,len(arr)))