def permutationEquation(p):
    # Write your code here
    x = list(range(1,len(p)+1))
    # fInverseP = []
    # for i in x:
    #     for j in range(len(p)):
    #         if i == p[j]:
    #             fInverseP.append(j+1)
    #             break
    # print(fInverseP)
    fInverseInverseP = []
    for i in x:
        for j in range(len(p)):
            if i == p[j]:
                for k in range(len(p)):
                    if j+1 == p[k]:
                        fInverseInverseP.append(x[k])
                break
    return fInverseInverseP

# permutationEquation(list(map(int, '2 3 1'.rstrip().split())))
permutationEquation(list(map(int, '4 3 5 1 2'.rstrip().split())))