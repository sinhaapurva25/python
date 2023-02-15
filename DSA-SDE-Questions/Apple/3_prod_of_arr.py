# Python3 program for A Product Array Puzzle
def product_array(arr, n):
    # Base case
    if n == 1:
        print(0)
        return

    i, temp = 1, 1

    # Allocate memory for the product array
    prod = [1 for i in range(n)]

    # Initialize the product array as 1


    temp = 1
    for i in range(1, n):
        prod[i] = temp*arr[i-1]
        temp = temp*arr[i-1]

    # Initialize temp to 1 for product on right side
    temp = 1
    # In this loop, temp variable contains product of
    # elements on right side excluding arr[i]
    for i in range(n - 2, -1, -1):
        prod[i] *= temp*arr[i+1]
        temp = temp*arr[i+1]

    # Print the constructed prod array
    for i in range(n):
        print(prod[i], end=" ")

    return


# Driver Code
arr = [10, 3, 5, 6, 2]
n = len(arr)
print("The product array is: n")
product_array(arr, n)

# This code is contributed by mohit kumar
