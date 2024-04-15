if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n])

    x = 1
    y = 1
    z = 2
    n = 3
    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)])
    print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n])


from functools import reduce

my_list = [1, 3, 5, 6, 2]

# Using a lambda function to add elements
sum_result = reduce(lambda x: x*2, my_list)
print(f"The sum of the list elements is: {sum_result}")
