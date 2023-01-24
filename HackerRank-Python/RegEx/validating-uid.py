# Enter your code here. Read input from STDIN. Print output to STDOUT

def noOfDigitsAndAlphabets(UID):
    count_alpha = 0
    count_numeric = 0
    for i in UID:
        if i.isalpha():
            count_alpha += 1
        else:
            count_numeric += 1
        if count_alpha==2 and count_numeric==3:
            break
    return count_alpha>=2 and count_numeric>=3

def check(UIDS):
    res = list()

    for UID in UIDS:
        len_UID = len(UID)
        if len_UID == 10:
            if len(set(UID)) == len_UID:
                if UID.isalnum():
                    if noOfDigitsAndAlphabets(UID):
                        res.append('Valid')
                    else:
                        res.append('Invalid')
                else:
                    res.append('Invalid')
            else:
                res.append('Invalid')
        else:
            res.append('Invalid')
    
    return res

UIDS = list()
for _ in range(int(input())):
    UIDS.append(input())
[print(i) for i in check(UIDS)]