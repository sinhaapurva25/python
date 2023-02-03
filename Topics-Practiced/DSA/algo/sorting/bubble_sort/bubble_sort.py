# https://github.com/sinhaapurva25/c/blob/main/data_structures/bubblesort.c
# https://www.geeksforgeeks.org/bubble-sort/

def swap(arr, a, b):
    if a != b:
        arr[a] ^= arr[b]
        arr[b] ^= arr[a]
        arr[a] ^= arr[b]


def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            # ascending order
            if arr[j + 1] < arr[j]:
            # # descending order
            # if arr[j+1] > arr[j]:
                swap(arr, j, j + 1)
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    arr = [38, 9, 29, 7, 2, 15, 28]
    bubble_sort(arr)
    print(arr)

    arr = [5, 9, 2, 1, 67, 34, 88, 34]
    bubble_sort(arr)
    print(arr)

    arr = [1, 2, 4]
    bubble_sort(arr)
    print(arr)