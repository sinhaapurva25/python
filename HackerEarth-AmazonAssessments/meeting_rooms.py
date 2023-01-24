schedule = list()
count = 0
N = int(input())
for i in range(N):
    t = list(map(int,input().split(" ")))#input()
    schedule.append([t[0]*60+t[1],t[2]*60+t[3]])
schedule.sort(key=lambda x:x[0])
# print(schedule)
for i in range(N):
    for j in schedule[:i]:
        if schedule[i][0] in range(j[0],j[1]):
            count += 1
            break
print(count)
# 6
# 09 00 09 45
# 09 30 10 30
# 10 40 12 00
# 11 00 13 00
# 11 45 14 00
# 16 00 17 00