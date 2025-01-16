from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return nums
        c = 0
        res = dict()
        res[c] = "{}->{}".format(nums[0], nums[0])
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                res[c] = res[c].split("->")[0] + "->" + str(nums[i + 1])
            else:
                c += 1
                res[c] = "{}->{}".format(nums[i + 1], nums[i + 1])
        return [i if i.split("->")[0]!=i.split("->")[1] else i.split("->")[0] for i in res.values()]
s = Solution()
print(s.summaryRanges([0,1,2,4,5,7]))