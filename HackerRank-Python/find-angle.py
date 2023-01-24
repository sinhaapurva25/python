import math
AB = int(input())
BC = int(input())
print(str(round(90-(math.atan2(BC,AB)*180)/math.pi))+ u"\N{DEGREE SIGN}")