import random
import numpy as np
def missingNumber():
    def missnum(lst):
        # print(l)
        # print(lst)
        return set(range(lst[len(lst)-1])[1:])-set(l)
    l = list(range(1,101))
    l.remove(100)
    print(missnum(l))
k = missingNumber()

def duplicateInList():
    lst = [random.randint(0,5) for i in range(50)]
    res = {}
    for i in lst:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    print(res)
    print([(j,res[j]) for j in sorted(res)])
# duplicateInList()

def listIntersection():
    lst1 = np.unique([random.randint(0,25) for i in range(50)])
    lst2 = np.unique([random.randint(0,25) for i in range(20)])
    res = []
    for i in lst1:
        if i in lst2:
            res.append(i)
    print(lst1)
    print(lst2)
    print(res)
# listIntersection()

def anagram():
    str1 = 'tokyo'
    str2 = 'kyotooo'
    print(set(str1)==set(str2))
# anagram()

def min_max():
    arr = random.sample(range(0, 50), 10)
    print(arr)
    minInArr = float('inf')
    maxInArr = float('-inf')
    for i in arr:
        if i < minInArr:
            minInArr = i
        if i > maxInArr:
            maxInArr = i
    print(minInArr,maxInArr)
    print(min(arr),max(arr))
# min_max()

def removeDuplicates():
    arr = [random.randint(0,10) for i in range(10)]
    print(arr)
    print(id(arr))
    print(list(set(arr)))
    print(id(list(set(arr))))
# removeDuplicates()

def fibonacci(n):
    a = -1
    b = 1
    for i in range(n):
        c = a+b
        print(c)
        a = b
        b = c
# fibonacci(10)

def palindrome(string=''):
    print(string[::-1].casefold(), string.casefold(), string[::-1].casefold()==string.casefold())
# palindrome('Hannah')
# palindrome('AnNa')

# def stringPermutations(string=''):
#     for i in string:

def npFuncs():
    # print(np.matmul(2,2))
    # print(2@2)
    print(np.arange(12,20,1))
    print(np.arange(0,5))
    print(np.cumsum(np.arange(0,5)))
    lst = [10,5,13,-1,0,-1]
    print([lst[i] for i in np.argsort(lst)])
    # print(lst.pop(0))
    del lst[0]
    print(lst)
# npFuncs()

def strJoin():
    list1 = [7,8,9,10]
    list2 = 's'
    result = list2.join(str(list1))
    print(result)
    result = list2.join([str(i) for i in list1])
    print(result)
# strJoin()

# first_name = "Nora"
# favorite_language = "Python"
# print(f"Hi, I'm {first_name}. I'm learning {favorite_language}.")

# value = 5
# print(f"{value} multiplied by 2 is: {value * 2}")