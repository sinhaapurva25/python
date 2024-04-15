def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap

# year = int(input())
# print(is_leap(1600))
# print(is_leap(1652))
# print(is_leap(2020))
# print(is_leap(2000))

print(is_leap(2000))
print(is_leap(2400))
print(is_leap(1800))
print(is_leap(1900))
print(is_leap(2100))
print(is_leap(2200))
print(is_leap(2300))
print(is_leap(2500))