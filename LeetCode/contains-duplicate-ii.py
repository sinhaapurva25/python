from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # BRUTE FORCE - HASHMAP
        dct = dict()
        for i in range(len(nums)):
            if nums[i] in dct:
                id_of_occurences = dct[nums[i]]
                for j in id_of_occurences:
                    if abs(i-j) <= k:
                        return True
                dct[nums[i]].append(i)
            else:
                dct[nums[i]] = [i]
        # print(dct)
        return False


s = Solution()
print(s.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))
print(s.containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))
print(s.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))
