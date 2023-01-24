s="apurva sinha Yui pOI 4 5 6 7 8  K"
res = ""
for idx,i in enumerate(s):
    # print(idx,i)
    if idx==0 or s[idx-1]==" ":  
        res += i.upper()
    else:
        res += i
print(s)
print(res)