file = open(r'Python\file_read_write.txt')
# print(file.readable())
# print(file.readline(3))
file.close()
for each_line in file:
    print(each_line)

with open(r'Python\file_read_write.txt') as file:
    for idx,each_line in enumerate(file):
        print(idx, each_line)