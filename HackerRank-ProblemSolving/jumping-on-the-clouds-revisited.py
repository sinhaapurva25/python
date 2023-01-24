def jumpingOnClouds(c, k):
    
    # flag = 1
    e = 0
    i = 0

    # while flag!=2:
    #     e =  e + 1 + c[i] * 2
    #     i = (i+k)%len(c)
    #     if i == 0:
    #         flag = 2

    while 1:
        e =  e + 1 + c[i] * 2
        i = (i+k)%len(c)
        if i == 0:
            break

    return 100-e