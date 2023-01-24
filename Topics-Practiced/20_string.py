check1 = ['learn','quiz','practice','contribute']
check2 = check1
check3 = check1[:]

check2[0] = 'code'
check3[1] = 'mcq'

count = 0

for c in (check1,check2,check3):
    # print("c[0]",c[0],"c[1]",c[1],"c[2]",c[2],"c[3]",c[3])
    ## print(c)
    # print(count)
    # count += 1
    if c[0] == 'code':
        count += 1
    if c[1] == 'mcq':
        count +=10
print("what will be the value of 'count?'")
# print(count)