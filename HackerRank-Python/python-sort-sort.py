nm = input().split()

n = int(nm[0])

m = int(nm[1])

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

k = int(input())

kSorted = sorted(arr, key=lambda x: x[k:k+1])

# [print(j,sep=' ') for i in kSorted for j in i]
for i in kSorted:
        row = ''
        for j in i:
            row += str(j) + ' '
        print(row.rstrip())