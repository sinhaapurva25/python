def compare(el1, el2):
    if el1 == el2:
        return 1
    else:
        return -1

def rec(arr1, arr2, iteration, pen):
    if iteration == len(arr1):
        return pen
    else:
        pen += compare(arr1[iteration], arr2[iteration])
        iteration += 1
        return rec(arr1, arr2, iteration, pen)

arr1 = ['A', 'B', 'C']
arr2 = ['A', 'B', 'D']
pen = 0
print(rec(arr1, arr2, 0, 0))


# def rec(stringArr, substring, n):
#     if n == 1:
#         return string.find(substring)
#     else:
#         return string.find(substring, rec(stringArr, substring, n-1)+1)

# string = "apurva_sinha_kolkata_india.1997"
# print(string[rec(string,'_',3)+1:rec(string,'.',3)])

def solution(A):
    # write your code in Python 3.8.10
    n = max(set(A))+1
    print(n)
    m = [i for i in range(1,n)]
    return [i for i in m if i not in A]

# print(solution([1, 3, 6, 4, 1, 2]))
# print(solution([1, 2, 3]))
print(solution([-1, -3]))