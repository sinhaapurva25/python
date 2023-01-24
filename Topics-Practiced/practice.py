import numpy
## 1
char_arr = [i for i in input().split()]# char_arr = list(map(chr,input().split()))
# string = input().split()
# for substring in string:
#     equal = 0
#     for c in char_arr:
#         for _char_ in substring:
#             if c == _char_:
#                 equal += 1
#             if equal == len(char_arr):
#                 print(substring)


## 2
# char_arr = [i for i in input().split()]
# string = input().split()
# for substring in string:
#     if len(substring) >= len(char_arr):
#         print(list(numpy.sort(numpy.array([ord(s) for s in substring]))[:len(char_arr)]),",",list(numpy.sort(numpy.array([ord(c) for c in char_arr]))))
#         # if list(numpy.sort(numpy.array([ord(s) for s in substring]))[:len(char_arr)]) == list(numpy.sort(numpy.array([ord(c) for c in char_arr]))):
#             # print(substring)

## 3
char_arr = [i for i in input().split()]
string = input().split()
for substring in string:
    equal = 0
    for c in char_arr:
        if c in substring:
            equal += 1
    if equal == len(char_arr):
        print(substring)