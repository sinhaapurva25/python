s = "geeks"
res = list()
for i in range(len(s)):
    tmp = list()
    for j in range(i, len(s)):
        tmp.append(s[j])
        res.append("".join(tmp))
print(res)