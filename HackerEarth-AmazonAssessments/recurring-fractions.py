def isRecurring(s):
    reccurring = False
    reccurring_num = ''
    reverse_s = s.split('.')[1][::-1]
    if len(reverse_s) > 1:
        for i in range(len(reverse_s)):
            z = reverse_s[1] if i==0 else reverse_s[i:2*i]
            if reverse_s[:i] == z:
                reccurring = True
                reccurring_num = str(z[::-1])
                break
    return reccurring,reccurring_num

def returnRecurringPart(N, D):
    M = N//D
    if N%D == 0:
        return M
    else:
        M = str(M) + '.'
        N = N%D
        k = False
        while not k:
            N = N * (10 ** len(str(D)))
            M += '0'*(len(str(D))-1) + str(N//D)
            k,reccurring_num = isRecurring(M)
            N = N%D
    return M.split(reccurring_num+reccurring_num)[0]+'('+reccurring_num+')'
print(returnRecurringPart(100,99))
print(returnRecurringPart(10,3))
# print(isRecurring('1.42857142857142857'))