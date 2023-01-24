S= input()
length = 1
res = ''
for idx,i in enumerate(S):
    if idx < len(S)-1:
        if i==S[idx+1]:
            length += 1
        else:
            # print(length,i)
            res = res + '(' + str(length) + ', ' + str(i)+ ')' + ' '
            length = 1
    else:
        # print(length,i)
        res = res + '(' + str(length) + ', ' + str(i)+ ')' + ' '
print(res)