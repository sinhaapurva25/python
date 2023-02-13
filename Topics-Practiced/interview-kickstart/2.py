# Python Program to find 2 Missing
# Numbers using O(1)
# extra space and no overflow.

# Function to find two missing
# numbers in range
# [1, n]. This function assumes
# that size of array
# is n-2 and all array elements
# are distinct
def findTwoMissingNumbers(arr, n):
    # Get the XOR of all
    # elements in arr[] and
    # {1, 2 .. n}
    XOR = arr[0]
    for i in range(1, n - 2):
        XOR ^= arr[i]
    for i in range(1, n + 1):
        XOR ^= i

    # Now XOR has XOR of two
    # missing elements. Any set
    # bit in it must be set in
    # one missing and unset in
    # other missing number

    # Get a set bit of XOR
    # (We get the rightmost set bit)
    set_bit_no = XOR & ~(XOR - 1)

    # Now divide elements in two sets
    # by comparing rightmost
    # set bit of XOR with bit at same
    # position in each element.
    x = 0

    # Initialize missing numbers
    y = 0
    for i in range(0, n - 2):
        if arr[i] & set_bit_no:

            # XOR of first set in arr[]
            x = x ^ arr[i]
        else:

            # XOR of second set in arr[]
            y = y ^ arr[i]
    for i in range(1, n + 1):
        if i & set_bit_no:

            # XOR of first set in arr[] and
            # {1, 2, ...n }
            x = x ^ i

        else:

            # XOR of second set in arr[] and
            # {1, 2, ...n }
            y = y ^ i

    print("Two Missing Numbers are\n%d %d" % (x, y))


# Driver program to test
# above function
arr = [1, 2, 3]+[i for i in range(5,95)]+[97, 98, ]

# Range of numbers is 2
# plus size of array
n = 2 + len(arr)
findTwoMissingNumbers(arr, n)

# This code is contributed
# by Shreyanshi Arun.
