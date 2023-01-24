def merge_the_tools(string, k):
    res = ['' for i in range(k)]
    l = len(string)//k
    for i in range(k):
        w=string[i*l:((i*l)+l)]
        unique = (list(set(w)))
        for j in w:
            if j in unique:
                if j not in res[i]:
                    res[i] = res[i] + j
    [print(i,sep='\n') for i in res]
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)