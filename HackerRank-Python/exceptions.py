# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
lst = []
for i in range(T):
    a,b = input().split()
    lst.append([a,b])
for i in lst:
    try:
        print(int(i[0])//int(i[1]))
    except Exception as e:
        print("Error Code:",e)