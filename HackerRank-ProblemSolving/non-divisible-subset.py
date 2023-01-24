import itertools
def nonDivisibleSubset(k, s):
    # Write your code here
    # m = list()
    # for i in range(len(s)):
    #     for j in itertools.combinations(s,i):
    #         if sum(j)%k!=0:
    #             m.append(list(j))
    # max_len = max([len(i) for i in m])
    # print([i for i in m if len(i) == max_len])
    # return sum([1 for i in m if len(i) == max_len])
    res = list()
    for i in itertools.combinations(s,2):
        if sum(i)%k!=0:
            res.append(i)
    print(list(set(res)))
    return len(list(set(res)))
print(nonDivisibleSubset(3,[1,7,2,4]))
print(nonDivisibleSubset(4,[19,20,12,10,24,25,22]))