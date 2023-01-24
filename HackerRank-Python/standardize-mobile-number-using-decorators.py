def wrapper(f):
    def fun(l):
        l_unsorted = list()
        for i in l:
            l_unsorted.append(int(str(i)[::-1][:10][::-1]))
        l_sorted = sorted(l_unsorted)
        l_op = list()
        for i in l_sorted:
            ph = '+91',str(i)[:5],str(i)[5:]
            l_op.append(ph)
        return l_op
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


