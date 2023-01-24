def jumpingOnClouds(c):

    i = 0
    j = 0

    while 1:
        i += 2
        if i > len(c):
            i -= 1
        if i < len(c):
            if c[i]==1:
                i -= 1
        j += 1
        if i >= len(c)-1:
            break

    return j
print(jumpingOnClouds(list(map(int, '0 1 0 0 0 1 0'.rstrip().split()))))
print(jumpingOnClouds(list(map(int, '0 0 0 1 0 0'.rstrip().split()))))