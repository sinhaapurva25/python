t = int(input())
boolean_arr = []
for i in range(t):
    wrds = int(input())
    dict_wrds = input().split(" ")
    gibberish_wrd = input()
    boolean_arr.append(1)
    
    gibberish_wrds = list()
    len_last_wrd = len(gibberish_wrd)%len(dict_wrds[0])

    for j in range(0,len(gibberish_wrd)-len_last_wrd,len(dict_wrds[0])):
        gibberish_wrds.append(gibberish_wrd[j:j+len(dict_wrds[0])])
    if len_last_wrd != 0:
        gibberish_wrds.append(gibberish_wrd[::-1][:len_last_wrd][::-1])
    for j in gibberish_wrds:
        if j in dict_wrds: pass
        else:
            boolean_arr[i] = 0
            break
[print(i) for i in boolean_arr]

# 2
# 4
# ab ba ac ff
# bafab
# 4
# ab ba ac ff
# baffab