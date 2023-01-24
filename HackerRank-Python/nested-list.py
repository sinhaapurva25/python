import numpy as np
if __name__ == '__main__':
    info = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        info.append([name,score])
    info = sorted(info, key=lambda x: x[1])
    info = sorted(info, key=lambda x: x[0])

    second_lowest = np.unique([i[1] for i in info])[1]
    [print(i[0]) for i in info if i[1]==second_lowest]