# def split_and_join(line):
#     line_output = ''
#     for i in line.split():
#         line_output += i + '-'
#     return line_output.rstrip('-')

# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)

def split_and_join(line):
    return "-".join(line.split(" ")).rstrip("-")

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)