a = -1
b = 1
fibonacci = []
for i in range(0, 10):
    c = a+b
    fibonacci.append(c)
    a = b
    b = c
print(fibonacci)


def prints(a, n, ind):
    # Create an auxiliary array of twice size.
    b = [None] * 2 * n
    i = 0

    # Copy a[] to b[] two times
    while i < n:
        b[i] = b[n + i] = a[i]
        i = i + 1

    i = ind

    # print from ind-th index to (n+i)th index.
    while i < n + ind:
        print(b[i], end=" ");
        i = i + 1
a = ['A', 'B', 'C', 'D', 'E', 'F']
n = len(a);
prints(a, n, 3);