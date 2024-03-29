def leftTopDiagnol(r, c, n, obstacles):
    count = 0
    while 1:
        if r == n or c == 1 or ([r, c] in obstacles):
            break
        else:
            r += 1
            c -= 1
            count += 1
    return count

def rightTopDiagnol(r, c, n, obstacles):
    count = 0
    while 1:
        if r == n or c == n or ([r, c] in obstacles):
            break
        else:
            r += 1
            c += 1
            count += 1
    return count

def rightBottomDiagnol(r, c, n, obstacles):
    count = 0
    while 1:
        if r == 1 or c == 1 or ([r, c] in obstacles):
            break
        else:
            r -= 1
            c -= 1
            count += 1
    return count

def leftBottomDiagnol(r, c, n, obstacles):
    count = 0
    while 1:
        if r == 1 or c == n or ([r, c] in obstacles):
            break
        else:
            r -= 1
            c += 1
            count += 1
    return count

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
    
    count = 0
    
    # lst.extend([[i,c_q] for i in range(n,0,-1) if i!=r_q])
    # lst.extend([[r_q,i] for i in range(1,n+1) if i!=c_q])

    for i in range(r_q+1,n+1):
        if [i,c_q] in obstacles:
            break
        else:
            count += 1

    for i in range(r_q-1,0,-1):
        if [i,c_q] in obstacles:
            break
        else:
            count += 1

    for i in range(c_q+1,n+1):
        if [r_q,i] in obstacles:
            break
        else:
            count += 1

    for i in range(c_q-1,0,-1):
        if [r_q,i] in obstacles:
            break
        else:
            count += 1

    # print(lst)
    
    # print(leftTopDiagnol(list(), r_q, c_q, n, obstacles))
    # print(rightTopDiagnol(list(), r_q, c_q, n, obstacles))
    # print(rightBottomDiagnol(list(), r_q, c_q, n, obstacles))
    # print(leftBottomDiagnol(list(), r_q, c_q, n, obstacles))
    
    count += leftTopDiagnol(r_q, c_q, n, obstacles)
    count += rightTopDiagnol(r_q, c_q, n, obstacles)
    count += rightBottomDiagnol(r_q, c_q, n, obstacles)
    count += leftBottomDiagnol(r_q, c_q, n, obstacles)
    
    # printPattern(n, r_q, c_q, lst)

    return count