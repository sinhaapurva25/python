# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap


def heapify(arr, N, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < N and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < N and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, N, largest)


# The main function to sort an array of given size

def heapSort(arr):
    N = len(arr)

    # Build a maxheap.
    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)
        # nlogn

    # One by one extract elements
    for i in range(N - 1, 0, -1): # 6, 5, 4, 3, 2, 1, 0
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
        # nlogn


# Driver's code
if __name__ == '__main__':
    arr = [5, 16, 8, 14, 20, 1, 26]
    arr = [5, 3, 8, 7, 0, 6, 3, 7]

    # Function call
    heapSort(arr)
    N = len(arr)

    print("Sorted array is")
    for i in range(N):
        print("%d" % arr[i], end=" ")
# This code is contributed by Mohit Kumra
