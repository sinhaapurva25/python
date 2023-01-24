# Enter your code here. Read input from STDIN. Print output to STDOUT
number_of_students, number_of_subjects = map(int,input().split())
arr = [list(map(float,input().split())) for i in range(number_of_subjects)]
print(zip(*arr))
trns = list(map(list, zip(*arr)))
[print(sum(i)/number_of_subjects) for i in trns]