from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        mx_l = height[0]
        mx_r = height[len(height)-1]
        mx_l_arr = [0] * len(height)
        mx_r_arr = [0] * len(height)
        res = 0
        for i in range(1, len(height)):
            l = i
            r = len(height)-i-1
            if height[l-1] > mx_l:
                mx_l = height[l-1]
            if height[r+1] > mx_r:
                mx_r = height[r+1]
            mx_l_arr[l] = mx_l
            mx_r_arr[r] = mx_r
        # print(height, mx_l_arr, mx_r_arr, sep="\n")

        for i in range(len(height)):
            t = min(mx_l_arr[i], mx_r_arr[i]) - height[i]
            if t > 0:
                res += t

        return res


s = Solution()
print(s.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap(height = [4,2,0,3,2,5]))
