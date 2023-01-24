z = {'a':12,'b':13}
print(*z)
print(*z.values())
[print(k) for k in z.keys()]
print(list(k for k in z.keys()))
[print(k,sep='\t') for k in z.keys()]