import itertools


class Solution:
    def min_in_arr(self, nums, search_from_idx):
        mn_idx = search_from_idx
        for i in range(mn_idx, len(nums)):
            if nums[i] < nums[search_from_idx]:
                search_from_idx = i
        return nums[search_from_idx], search_from_idx

    def mostCompetitive(self, nums: list(), k: int) -> list():
        s = 0
        res = list()
        while len(res) != k:
            mn, new_search_from_idx = self.min_in_arr(nums, s)
            s  = new_search_from_idx
            res.append(nums[mn])
        return res



s = Solution()
print(s.mostCompetitive(nums=[3, 5, 2, 6], k=2))
# print(s.mostCompetitive(nums=[2, 4, 3, 3, 5, 4, 9, 6, -1], k=4))
