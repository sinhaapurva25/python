N = int(input())

length_A_arr = []
A_arr = []
length_B_arr = []
B_arr = []

for i in range(N):
    length_A = int(input())
    A = list(map(int, input().split()))[:length_A]
    length_B = int(input())
    B = list(map(int, input().split()))[:length_B]
    
    length_A_arr.append(length_A)
    A_arr.append(A)
    length_B_arr.append(length_B)
    B_arr.append(B)

output = []
for i in range(N):
    length_A = length_A_arr[i]
    A = A_arr[i]

    length_B = length_B_arr[i]
    B = B_arr[i]

    if length_B < length_A:
        output.append(False)
    else:
        count = 0
        for i in A:
            if i in B: count += 1
        # print(count)
        if count == length_A:
            output.append(True)
        else:
            output.append(False)

[print(i,sep="\n") for i in output]
