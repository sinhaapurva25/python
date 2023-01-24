def leftTopDiagnol(subLst, r, c, n, obstacles):
    while 1:
        if r == n or c == 1 or ([r, c] in obstacles):
            break
        else:
            r += 1
            c -= 1
            subLst.append([r, c])
    return subLst

def rightTopDiagnol(subLst, r, c, n, obstacles):
    while 1:
        if r == n or c == n or ([r, c] in obstacles):
            break
        else:
            r += 1
            c += 1
            subLst.append([r, c])
    return subLst

def rightBottomDiagnol(subLst, r, c, n, obstacles):
    while 1:
        if r == 1 or c == 1 or ([r, c] in obstacles):
            break
        else:
            r -= 1
            c -= 1
            subLst.append([r, c])
    return subLst

def leftBottomDiagnol(subLst, r, c, n, obstacles):
    while 1:
        if r == 1 or c == n or ([r, c] in obstacles):
            break
        else:
            r -= 1
            c += 1
            subLst.append([r, c])
    return subLst

def printPattern(n, r_q, c_q, lst):
    res = ""
    for i in range(n, 0, -1):
        for j in range(1, n+1):
            if [i,j] == [r_q, c_q]:
                res += "Q"
            else:
                if [i,j] in lst:
                    res += "#"
                else:
                    res += "_"
        res += "\n"
    print(res)

def queensAttack(n, k, r_q, c_q, obstacles):
    
    lst = list()
    
    # lst.extend([[i,c_q] for i in range(n,0,-1) if i!=r_q])
    # lst.extend([[r_q,i] for i in range(1,n+1) if i!=c_q])

    for i in range(r_q+1,n+1):
        if [i,c_q] in obstacles:
            break
        else:
            lst.append([i,c_q])

    for i in range(r_q-1,0,-1):
        if [i,c_q] in obstacles:
            break
        else:
            lst.append([i,c_q])

    for i in range(c_q+1,n+1):
        if [r_q,i] in obstacles:
            break
        else:
            lst.append([r_q,i])

    for i in range(c_q-1,0,-1):
        if [r_q,i] in obstacles:
            break
        else:
            lst.append([r_q,i])

    # print(lst)
    
    # print(leftTopDiagnol(list(), r_q, c_q, n, obstacles))
    # print(rightTopDiagnol(list(), r_q, c_q, n, obstacles))
    # print(rightBottomDiagnol(list(), r_q, c_q, n, obstacles))
    # print(leftBottomDiagnol(list(), r_q, c_q, n, obstacles))
    
    lst.extend(leftTopDiagnol(list(), r_q, c_q, n, obstacles))
    lst.extend(rightTopDiagnol(list(), r_q, c_q, n, obstacles))
    lst.extend(rightBottomDiagnol(list(), r_q, c_q, n, obstacles))
    lst.extend(leftBottomDiagnol(list(), r_q, c_q, n, obstacles))
    
    # printPattern(n, r_q, c_q, lst)

    return len(lst)

import os
with open(r'queens-attack-test-cases\outputs.txt') as f:
    outputs = [i.rstrip() for i in f.readlines()]
print(outputs)
for file in os.listdir(r'queens-attack-test-cases\inputs'):
    fileName = os.path.join(r'queens-attack-test-cases\inputs',file)
    with open(fileName) as f:
        data = [j.rstrip() for j in f.readlines()]
    n, k = list(map(int,data[0].split(' ')))
    r_q, c_q = list(map(int,data[1].split(' ')))
    if k == 0:
        obstacles = list()
    else:
        obstacles = [list(map(int,j.split(' '))) for j in data[2:]]

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(result, outputs[int(file.split('.')[0].split('-')[1])-1])