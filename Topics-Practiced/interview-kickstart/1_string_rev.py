def reverse_word(wrd):  # hannah -> hannah, moon -> noom
    wrd_len = 0
    for i in wrd:
        wrd_len += 1
    res = ''
    for i in range(wrd_len):
        res += wrd[wrd_len - i - 1]
    return res


def reverse_string(string):
    string = reverse_word(string)
    l = 0
    for i in string:
        l += 1
    res = ''
    start = 0
    for i in range(l):
        if string[i] == ' ':
            if i >= 1:
                if string[i - 1] != ' ':
                    res += reverse_word(string[start:i]) + ' '
                else:
                    res += string[i]
            else:
                res += string[i]

        if i >= 1:
            if string[i] != ' ' and string[i - 1] == ' ':
                start = i
    # print([ord(i) for i in res])
    return f'"{res}"'


input = ' I will do it. '
print(f'reverse_string("{input}")={reverse_string(input)}="{" ".join(input.split(" ")[::-1])}"')
input = '   word1  word2 '
print(f'reverse_string("{input}")={reverse_string(input)}="{" ".join(input.split(" ")[::-1])}"')

