# https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
class Solution:
    # Back-end complete function Template for Python 3

    # Function to find the leaders in the array.
    def leaders(self, A, N):
        ans = [A[N - 1]]
        max = A[N - 1]
        for i in range(N - 2, -1, -1):
            if A[i] >= max:
                max = A[i]
                ans.append(A[i])
        return ans[::-1]

s = Solution()
A=[16,17, 17, 17, 17, 4,3,5,2]
print(s.leaders(A, len(A)))