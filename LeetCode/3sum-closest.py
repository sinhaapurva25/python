from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mn = float("inf")
        i = 0
        res = sum(nums[:3])
        while i < len(nums):
            if i == 0 or (i != 0 and nums[i] != nums[i - 1]):
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    sm = nums[i] + nums[l] + nums[r]
                    if sm == target:
                        return sm
                    # if target > 0:
                    # USE THIS COND INSTEAD
                    if target > sm:
                        dst = target - sm
                    else:
                        dst = sm - target
                    # YOU CAN REPLACE LINES 19-22 with
                    # dst = abs(sm - target)
                    if dst < mn:
                        mn = dst
                        res = sm
                    if sm < target:
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    else:
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
            i += 1
        return res


f = Solution()
print(f.threeSumClosest(nums=[-1, 2, 1, -4], target=1))
print(f.threeSumClosest(nums=[0, 0, 0], target=1))
print(f.threeSumClosest(nums=[1, 1, 1, 0], target=-100))
print(f.threeSumClosest(nums=[4, 0, 5, -5, 3, 3, 0, -4, -5], target=-2))

