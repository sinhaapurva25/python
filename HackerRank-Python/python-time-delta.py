#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
from datetime import datetime
def time_delta(t1, t2):
    t1_s = datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    t2_s = datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    return str(int(abs((t1_s-t2_s)).total_seconds()))

t = int(input())
for t_itr in range(t):
    t1 = input()
    t2 = input()
    delta = time_delta(t1, t2)
    print(delta)