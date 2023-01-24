def func():
    yield 1
    yield 2
    yield 'k'
    yield '9'
    return 0

print([i for i in func()])
k = {"a":"a","b":"b","c":34,"d":[1,2,3]}
for i in k: print(i)