import re
import warnings
warnings.filterwarnings('ignore')

N = int(input())
S = []
for _ in range(N):
    line = input()
    '''
    this will fail if there are overalapping || or &&
    line = re.sub("\s\|\|\s", "or",line)
    line = re.sub("\s\&\&\s", "and",line)
    '''
    # # both options below are correct
    # using container r''
    line = re.sub(r'(?<= )(\|\|)(?= )', "or",line)
    line = re.sub(r'(?<= )(&&)(?= )', "and",line)
    # using placeholder \
    line = re.sub("(?<=\s)(\|\|)(?=\s)", "or",line)
    line = re.sub("(?<=\s)(&&)(?=\s)", "and",line)
    S.append(line)
[print(i) for i in S]