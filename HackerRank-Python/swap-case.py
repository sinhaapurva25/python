def swap_case(s):
    s_output = ''
    for i in s:
        # print(i)
        if i.isupper():
            s_output += i.lower()
        else:
            s_output += i.upper()
    return s_output

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)