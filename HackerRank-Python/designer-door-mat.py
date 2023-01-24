# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = [int(i) for i in input().split()]
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))