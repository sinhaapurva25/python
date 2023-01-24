def gen():
    x = 5
    yield 1
    yield 2
    yield x
    yield "apurva"
    return (9,0)
print(gen())
print(list(gen()))
for val in gen():
    print(val)