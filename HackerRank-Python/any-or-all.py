N = int(input())
arr = list(map(int,input().split()))

res1 = all(map(lambda x: True if x > 0 else False, arr))
res2 = False
if res1 == True:
    res2 = any(map(lambda x: True if str(x)==str(x)[::-1] else None,arr))
print(all([res1,res2]))