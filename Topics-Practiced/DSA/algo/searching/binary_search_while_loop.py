def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index+right_index)//2

        if number_to_find == numbers_list[mid_index]:
            return mid_index

        if number_to_find < numbers_list[mid_index]:
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1

    return -1


if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 67667

    index = binary_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using binary search")