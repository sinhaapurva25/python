class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(combination, sum, index):
            if sum == target:
                res.append(combination.copy())
                return
            if sum > target:
                return
            for c in range(index, len(candidates)):
                helper(combination.append(candidates[c]), sum+candidates[c], index)
            helper += 1
        res = list()
        helper(res, 0, 0)
        return res
s = Solution()
print(s.combinationSum([2,3,5],8))