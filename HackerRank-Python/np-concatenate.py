import numpy
N_M_P = [int(i) for i in input().split()]
if len(N_M_P)<3:
    pass
else:
    N = N_M_P[0]
    M = N_M_P[1]
    P = N_M_P[2]
    N_cross_P = []
    for i in range(N):
        row=[int(p) for p in input().split()]
        N_cross_P.append(row)
    M_cross_P = []
    for i in range(M):
        row=[int(p) for p in input().split()]
        M_cross_P.append(row)
    # print(numpy.array(N_cross_P), "\n",numpy.array(M_cross_P))
    print(numpy.concatenate((numpy.array(N_cross_P), numpy.array(M_cross_P))))