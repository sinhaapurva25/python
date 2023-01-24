import sys
# print(sys.getsizeof([i for i in range(10,14)]))
# print(sys.getsizeof((i for i in range(10,14))))
print(sys.getsizeof([]),sys.getsizeof([10]),sys.getsizeof([10,11]),sys.getsizeof([10,11,12]),sys.getsizeof([10,11,12,13]))
print(sys.getsizeof(()),sys.getsizeof((10)),sys.getsizeof((10,11)),sys.getsizeof((10,11,12)),sys.getsizeof((10,11,12,13)))

print((i for i in range(10,14)))
print(list(i for i in range(10,14)))

print(map(int, "10 11 12 13".split()))
print(list(map(int, "10 11 12 13".split())))
print(list(map(str, "10 11 12 13".split())))
print(list(map(str, "10 11 12 13")))

print(list(zip('10','11','12','13')))


# Python code to demonstrate the working of
# unzip

# initializing lists
name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]
print(*list(list(zip(name, roll_no, marks))))
namz, roll_noz, marksz = zip(*list(list(zip(name, roll_no, marks))))
print(namz,roll_noz,marksz)