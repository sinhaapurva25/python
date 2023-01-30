def swap(arr, i, j):
    if i != j:
        arr[i] ^= arr[j]
        arr[j] ^= arr[i]
        arr[i] ^= arr[j]

def heapify(arr, i, N):
    left_child_index = 2 * i + 1
    right_child_index = 2 * i + 2

    largest = i

    if left_child_index < N and arr[largest] < arr[left_child_index]:
    # for arranging in descending order:
    # if left_child_index < N and arr[largest] > arr[left_child_index]:
        largest = left_child_index


    if right_child_index < N and arr[largest] < arr[right_child_index]:
    # for arranging in descending order:
    # if right_child_index < N and arr[largest] > arr[right_child_index]:
        largest = right_child_index

    if largest != i:
        swap(arr, i, largest)

        heapify(arr, largest, N)



def heap_sort(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, i, len(arr))

    for i in range(len(arr) - 1, 0, -1):
        swap(arr, 0, i)
        heapify(arr, 0, i)


if __name__ == '__main__':
    arr = [30, -1, 5, 9, 1, 29, 0]
    k = 3

    print(f"input arr: {arr}")
    heap_sort(arr)
    print(f"sorted arr: {arr}")
    print(f"for k={k}, k smallest numbers are {arr[:k]}")

