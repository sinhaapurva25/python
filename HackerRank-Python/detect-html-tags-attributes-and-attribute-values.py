# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    C = input()
    print(re.match(r'([4-6][0-9^_^\s]+){16}$',C))