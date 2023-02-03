# https://www.youtube.com/watch?v=hhkLdjIimlw

def swap(arr, a, b):
    if a != b:
        arr[a] ^= arr[b]
        arr[b] ^= arr[a]
        arr[a] ^= arr[b]


def selection_sort(arr):
    for i in range(len(arr)-1):
    # len(arr)-1 because the last element is already sorted, you don't need to go throught it
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        swap(arr, i, min_index)


if __name__ == '__main__':
    arr = [38, 9, 29, 7, 2, 15, 28]
    selection_sort(arr)
    print(arr)