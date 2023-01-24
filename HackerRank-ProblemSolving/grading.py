# k = [73,67,38,33]
# print([[i, (5 - i),(5 - i) % 5,(i + (5 - i) % 5)] for i in k])

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    res = grades
    for i in range(len(grades)):
        grade = grades[i]
        if grade < 38:
            pass
        else:
            if grade % 5 == 0:
                pass
            else:
                if (5 - grade) % 5 < 3:
                    res[i] = grade + (5 - grade) % 5
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()