number_of_numbers = int(input())
integer_list = [int(i) for i in input().split()]
print(hash(tuple(integer_list)))