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

def queenToTop(r_q, c_q, n, obstacles):
    print('queenToTop')
    count = 0
    for i in range(r_q+1,n+1):
        print([i,c_q])
        if [i,c_q] in obstacles:
            break
        else:
            count += 1
    print(count)
    return count

def queenToBottom(r_q, c_q, n, obstacles):
    print('queenToBottom')
    count = 0
    for i in range(r_q-1,0,-1):
        print([i,c_q])
        if [i,c_q] in obstacles:
            break
        else:
            count += 1
    print(count)
    return count

def queenToRight(r_q, c_q, n, obstacles):
    print('queenToRight')
    count = 0
    for i in range(c_q+1,n+1):
        print([r_q,i])
        if [r_q,i] in obstacles:
            break
        else:
            count += 1
    print(count)
    return count

def queenToLeft(r_q, c_q, n, obstacles):
    print('queenToLeft')
    count = 0
    for i in range(c_q-1,0,-1):
        print([r_q,i])
        if [r_q,i] in obstacles:
            break
        else:
            count += 1
    print(count)
    return count

def leftTopDiagnol(r, c, n, obstacles):
    print('leftTopDiagnol')
    count = 0
    while 1:
        print([r, c])
        if r == n or c == 1 or ([r, c] in obstacles):
            break
        else:
            r += 1
            c -= 1
            count += 1
    print(count)
    return count

def rightTopDiagnol(r, c, n, obstacles):
    print('rightTopDiagnol')
    count = 0
    while 1:
        print([r, c])
        if r == n or c == n or ([r, c] in obstacles):
            break
        else:
            r += 1
            c += 1
            count += 1
    print(count)
    return count

def rightBottomDiagnol(r, c, n, obstacles):
    print('rightBottomDiagnol')
    count = 0
    while 1:
        print([r, c])
        if r == 1 or c == 1 or ([r, c] in obstacles):
            break
        else:
            r -= 1
            c -= 1
            count += 1
    print(count)
    return count

def leftBottomDiagnol(r, c, n, obstacles):
    print('leftBottomDiagnol')
    count = 0
    while 1:
        print([r, c])
        if r == 1 or c == n or ([r, c] in obstacles):
            break
        else:
            r -= 1
            c += 1
            count += 1
    print(count)
    return count

def queensAttack(n, k, r_q, c_q, obstacles):
    
    count = 0
    
    count += queenToTop(r_q, c_q, n, obstacles)
    count += queenToBottom(r_q, c_q, n, obstacles)
    count += queenToRight(r_q, c_q, n, obstacles)
    count += queenToLeft(r_q, c_q, n, obstacles)

    count += leftTopDiagnol(r_q, c_q, n, obstacles)
    count += rightTopDiagnol(r_q, c_q, n, obstacles)
    count += rightBottomDiagnol(r_q, c_q, n, obstacles)
    count += leftBottomDiagnol(r_q, c_q, n, obstacles)

    return count

print('queen:',[4, 4])
result = queensAttack(8, 1, 4, 4,[[3,5]])
print(result)
# result = queensAttack(4, 0, 4, 4,[])
# print(result)
# result = queensAttack(5, 3, 4, 3,[[5, 5],[4, 2],[2, 3]])
# print(result)
# result = queensAttack(1, 0, 1, 1,[])
# print(result)

# import os
# with open(r'queens-attack-testcases\outputs.txt') as f:
#     outputs = [i.rstrip() for i in f.readlines()]

# for file in os.listdir(r'queens-attack-testcases\inputs'):
    
#     fileName = os.path.join(r'queens-attack-testcases\inputs',file)
#     with open(fileName) as f:
#         data = [j.rstrip() for j in f.readlines()]
#     n, k = list(map(int,data[0].split(' ')))
#     r_q, c_q = list(map(int,data[1].split(' ')))
#     if k == 0:
#         obstacles = list()
#     else:
#         obstacles = [list(map(int,j.split(' '))) for j in data[2:]]

#     result = queensAttack(n, k, r_q, c_q, obstacles)

#     cse = int(file.split('.')[0].split('-')[1])
#     if result==outputs[cse]:
#         print("test case",cse, "passed")
#     else:
#         print('expected res',outputs[cse], 'your res',result, "test case",cse, "failed")