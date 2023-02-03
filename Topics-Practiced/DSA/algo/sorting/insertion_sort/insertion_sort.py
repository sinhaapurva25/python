def swap(arr, a, b):
    if a != b:
        arr[a] ^= arr[b]
        arr[b] ^= arr[a]
        arr[a] ^= arr[b]


def insertion_sort(arr):
    if len(arr) <= 1:
        return
    for i in range(1, len(arr)):
        anchor = arr[i]
        j = i - 1
        while anchor < arr[j] and 0 <= j:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = anchor
        # print(arr)


if __name__ == '__main__':
    # arr = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    # insertion_sort(arr)
    # print(arr)

    arr = [11, 9, 29, 7, 2, 15, 28]
    insertion_sort(arr)
    print(arr)

    # arr = [21]
    # insertion_sort(arr)
    # print(arr)
