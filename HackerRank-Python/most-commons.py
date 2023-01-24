import math
import os
import random
import re
import sys
import operator


if __name__ == '__main__':
    s = input()
    from collections import Counter
    for i in Counter(sorted(s)).most_common(3):
        print(*i)