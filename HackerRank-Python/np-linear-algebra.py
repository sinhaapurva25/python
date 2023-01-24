import numpy
if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(0,N):
        user_input = [float(i) for i in input().split()]
        row = []
        for j in range(0,N):
            row.append(user_input[j])
        arr.append(row)
    print(numpy.round(numpy.linalg.det(arr),2))