N = int(input())
columns = [i for i in input().split()]
for idx,i in enumerate(columns):
    if i == 'MARKS':
        markColIdx = idx
sum = 0
for i in range(N):
    studentInfo = [j for j in input().split()]
    sum += int(studentInfo[markColIdx])
print(sum/N)