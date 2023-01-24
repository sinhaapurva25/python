# def print_formatted(number):
    
#     def decimal_to_octal(n):
#         oct = ''
#         while n:
#             res = str(n % 8)
#             n = n // 8
#             oct += res
#         return oct[::-1]

#     def decimal_to_hexadec(n):
#         hexadec = ''
#         while n:
#             res = str(n % 16)
#             n = n // 16
#             hexadec += res
#         hexadec = hexadec[::-1]
#         # if hexadec == str(10): hexadec = 'A'
#         # if hexadec == str(11): hexadec = 'B'
#         # if hexadec == str(12): hexadec = 'C'
#         # if hexadec == str(13): hexadec = 'D'
#         # if hexadec == str(14): hexadec = 'E'
#         # if hexadec == str(15): hexadec = 'F'

#         return hexadec

#     def decimal_to_bin(n):
#         bin = ''
#         while n:
#             res = str(n % 2)
#             n = n // 2
#             bin += res
#         return bin[::-1]

#     for i in range(0,number):
#         print(i+1,decimal_to_octal(i+1),decimal_to_hexadec(i+1),decimal_to_bin(i+1))

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)


# # def dec_to_oct(n):
# #     res = ''
# #     base = 8
# #     while n > base:
# #         res += str(n%base)
# #         n = n//base
# #     return (str(n) +res[::-1])

# # print(dec_to_oct(384))

def print_formatted(number):
    l = len(bin(number)) - 2
    for i in range(1, number + 1):
        f = ""
        for c in "doXb":
            if f:
                f += " "
            f += "{:>" + str(l) + c + "}"
        print(f.format(i, i, i, i))
        # print(f)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
print("{:>d} {:>o} {:>X} {:>b}".format(10,10,10,10))
# dec = "{:>X}".format(10)
# print(dec)