def merge_the_tools(string, k):
    # for i in range(0, len(string), k):
    #     s = ""
    #     for j in string[i : i + k]:
    #         if j not in s:
    #             s += j          
    #     print(s)
    for i in range(len(string)//k):
        res = ''
        for j in string[i*k:(i+1)*k]:
            if j not in res:
                res += j
        print(res)
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)