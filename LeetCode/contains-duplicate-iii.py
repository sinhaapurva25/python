from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        dct = dict()
        for i in range(len(nums)):
            
            if i != j and abs(i - j) <= indexDiff and abs(nums[i] - nums[j]) <= valueDiff:
                return [i, j]
        return False


s = Solution()
print(s.containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], indexDiff=3, valueDiff=0))
print(s.containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], indexDiff=2, valueDiff=3))
