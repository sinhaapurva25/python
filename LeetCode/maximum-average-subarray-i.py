from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        mx = float("-inf")
        avg = 0
        for i in range(len(nums) - k + 1):
            if i > 0:
                avg = (avg * k + nums[i + k - 1] - nums[i - 1]) / k
            else:
                avg = sum(nums[i:i + k]) / k
            if avg > mx:
                mx = avg
            # print("i: {}, avg: {}".format(i, avg))
        return mx


s = Solution()
print(s.findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))
print(s.findMaxAverage(nums=[5], k=1))
