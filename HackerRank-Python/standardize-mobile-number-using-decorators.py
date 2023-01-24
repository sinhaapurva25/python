def wrapper(f):
    def fun(l):
        
        f(map(lambda p: '+91 '+str(p[::-1][:10][::-1][:5])+' '+str(p[::-1][:10][::-1][5:]),l))
        
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)