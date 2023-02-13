def swap(arr, a, b):
    if a != b:
        arr[a] ^= arr[b]
        arr[b] ^= arr[a]
        arr[a] ^= arr[b]


def heapify(arr, i, N):
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    largest = i

    if left_child < N:
        if arr[left_child] < arr[largest]:
            largest = left_child
    if right_child < N:
        if arr[right_child] < arr[largest]:
            largest = right_child
    if largest != i:
        swap(arr, largest, i)
        heapify(arr, largest, N)


def heap_sort(arr):
    for i in range((len(arr) // 2) - 1, -1, -1):
        heapify(arr, i, len(arr))
    for i in range(len(arr) - 1, 0, -1):
        swap(arr, 0, i)
        heapify(arr, 0, i)


def calculate_xor(arr):
    res = 0
    for i in arr:
        res ^= i
    return res

def func(arr):
    heap_sort(arr)
    return arr

# https://www.geeksforgeeks.org/find-two-missing-numbers-set-2-xor-based-solution/
arr = [1, 2, 4, 6]
sorted_arr = func(arr)
N = sorted_arr[0]
req_s = N * (N + 1) // 2
obtained_s = sum(arr)
x_plus_y = req_s-obtained_s
x_xor_y = calculate_xor(arr)^calculate_xor([i for i in range(1,N+1)])
print(x_plus_y, x_xor_y)
