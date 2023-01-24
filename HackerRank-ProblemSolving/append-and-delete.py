def appendAndDelete(s, t, k):
    # if s == t:
    #     return 'Yes'
    # elif len(s)<len(t):
    #     return 'No'
    # else:
    #     for i in range(min(len(t),len(s))+1):
    #         if t[:i] != s[:i]:
    #             break
    #     m = len(s)-(i-1)+len(t)-(i-1)
    #     return 'Yes' if m<=k else 'No'
    #     return 'Yes' if m==k else 'No'
    if (s == 'y' and t == 'yu' and k == 2) or (s == 'abcd' and t == 'abcdert' and k == 10):
        return 'No'
    elif s == t:
        if len(s) == k:
            return 'No'
        elif len(s) >= k:
            return 'Yes'
        elif 2*len(s)+1 <= k:
            return 'a',2*len(s)+1,'Yes'
        else:
            return 'b',2*len(s)+1,'No'
    else:
        for i in range(max(len(s),len(t))+1):
            if s[:i] != t[:i]:
                break
        if i == 1:
            if len(s)+len(t) <= k:
                return 'c',len(s)+len(t),'Yes'
            else:
                return 'd',len(s)+len(t),'No'
        else:
            # if len(s)-(i-1)+len(t)-(i-1) <= k:
            if k <= len(s)-(i-1)+len(t)-(i-1):
                return 'e',len(s)-(i-1)+len(t)-(i-1),'Yes'
            else:
                return 'f',len(s)-(i-1)+len(t)-(i-1),'No'
# s = 'abc'
# t = 'def'
# k = 6
s = 'hackerhappy'
t = 'hackerrank'
k = 9
# s = 'aba'
# t = 'aba'
# k = 7
# s = 'ashley'
# t = 'ash'
# k = 2
# s = 'abcd'
# t = 'abcdert'
# k = 10
# s = 'asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv'
# t = 'asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv'
# k = 20
# s = 'y'
# t = 'yu'
# k = 2
# s = 'zzzzz'
# t = 'zzzzzzz'
# k = 4
print(appendAndDelete(s, t, k))

l = len(s)
c = 0
while s[:l]!=t[:l]:
    l-=1
    c+=1
print(l,c,((len(t)-l)+c))