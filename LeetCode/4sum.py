from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = list()
        nums.sort()
        i = 0
        while i < len(nums):
            if i == 0 or (i != 0 and nums[i] != nums[i - 1]):
                j = i + 1
                while j < len(nums):
                    if j == i+1 or (j !=i+1 and nums[j] != nums[j - 1]):
                        l = j + 1
                        r = len(nums) - 1
                        while l < r:
                            if nums[i] + nums[j] + nums[l] + nums[r] == target:
                                res.append([nums[i], nums[j], nums[l], nums[r]])
                                l += 1
                                while l < r and nums[l] == nums[l - 1]:
                                    l += 1
                            elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                                l += 1
                            else:
                                r -= 1
                    j += 1
            i += 1
        return res


f = Solution()
print(f.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
print(f.fourSum(nums=[2, 2, 2, 2, 2, 2], target=8))

