m,n = 4,8
# m,n = 4,7
# m,n = 8,4
# m,n = 7,4
matrix = []
count = 25
for i in range(m):
    row = []
    for j in range(n):
        row.append(count)
        count += 1
    matrix.append(row)
[print(i) for i in matrix]
# print(matrix)

r = m//2 if m%2==0 else m//2+1
c = n//2 if n%2==0 else n//2+1
# print(r,c)
layers = [[] for i in range(min(r,c))]
res_arr = matrix.copy()

rows = 0
cols = 1
l = 0
while l!=min(r,c):
# while rows!=r and cols!=c:
    # print(rows,m-rows,cols,n-cols)# print(rows,m-rows-1,cols,n-cols-1)
    left = [matrix[j][rows]for j in range(rows,m-rows)]
    bottom = [matrix[m-rows-1][i]for i in range(cols,n-cols)]
    right = [matrix[j][n-cols]for j in range(m-rows-1,rows-1,-1)]
    top = [matrix[rows][i] for i in range(n-cols-1,cols-1,-1)]
    indices = [[j,rows] for j in range(rows,m-rows)] + [[m-rows-1,i] for i in range(cols,n-cols)] + [[j,n-cols] for j in range(m-rows-1,rows-1,-1)] + [[rows,i] for i in range(n-cols-1,cols-1,-1)]
    layers[l].extend(left)
    layers[l].extend(bottom)
    layers[l].extend(right)
    layers[l].extend(top)
    # print(layers)
    # print(len(layers[l]),len(indices))
    rot = 2
    rotated_arr = [layers[l][(i-rot)%len(layers[l])] for i in range(len(layers[l]))]
    
    for i in range(len(layers[l])):
        res_arr[indices[i][0]][indices[i][1]] = rotated_arr[i]
    rows += 1
    cols += 1
    l += 1
[print(i,sep=' ') for i in res_arr]
res = ''
for i in res_arr:
    for j in i:
        res += str(j)+' '
    res+='\n'
print(res)
