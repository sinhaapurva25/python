lst = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
lst_copy = []
padding = 'p'
for i in range(len(lst)+2):
    row = []
    for j in range(len(lst[0])+2):
            if i==0 or j==0 or i==len(lst)+1 or j==len(lst[0])+1:
                row.append(padding)
            else:
                row.append(lst[i-1][j-1])
    lst_copy.append(row)

print("Input",lst,"--","Output",sep='\n')

for i in range(len(lst_copy)):
    for j in range(len(lst_copy[0])):
        neighbours = []
        if i==0 or j==0 or i==len(lst)+1 or j==len(lst[0])+1:
            pass
        else:
            if lst_copy[i-1][j-1] != padding: neighbours.append(lst_copy[i-1][j-1])
            if lst_copy[i][j-1] != padding: neighbours.append(lst_copy[i][j-1])
            if lst_copy[i+1][j-1] != padding: neighbours.append(lst_copy[i+1][j-1])
            if lst_copy[i-1][j] != padding: neighbours.append(lst_copy[i-1][j])
            if lst_copy[i+1][j] != padding: neighbours.append(lst_copy[i+1][j])
            if lst_copy[i-1][j+1] != padding: neighbours.append(lst_copy[i-1][j+1])
            if lst_copy[i][j+1] != padding: neighbours.append(lst_copy[i][j+1])
            if lst_copy[i+1][j+1] != padding: neighbours.append(lst_copy[i+1][j+1])
        if len(neighbours)>0:
            print('[',i-1,',',j-1,']:',neighbours)
    print("--")