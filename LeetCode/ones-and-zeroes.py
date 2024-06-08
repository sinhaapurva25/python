# https://www.geeksforgeeks.org/problems/segregate-0s-and-1s5106/1
class Solution:
    def segregate0and1(self, arr, n):
        j = 0
        for i in range(n):
            if arr[i] == 0:
                arr[j] = 0
                j += 1
        arr[j:] = [1] * (n - j)


s = Solution()
arr=[0, 0, 1, 1, 0]
s.segregate0and1(arr, len(arr))
print(arr)

