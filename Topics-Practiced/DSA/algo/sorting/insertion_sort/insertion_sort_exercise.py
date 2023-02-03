def median(arr):
    N = len(arr)
    mid = N // 2
    if N%2 == 0:
        return (arr[mid-1]+arr[mid])/2
    else:
        return arr[mid]


def insertion_sort(arr):
    if len(arr) <= 1:
        print(f"median of {arr}: {median(arr)}", '\n')
        return
    for i in range(1, len(arr)):
        anchor = arr[i]
        j = i - 1

        while j >= 0 and anchor <= arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = anchor
        print(f"median of {arr[:i+1]}: {median(arr[:i])}",'\n')



if __name__ == "__main__":
    arr = [2, 1, 5, 7, 2, 0, 5]
    print(f"original arr: {arr}",'\n')

    insertion_sort(arr)