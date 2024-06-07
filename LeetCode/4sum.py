class Solution:
    def fourSum(self, nums: list, target: int):
        nums.sort()
        i1 = 0
        res = list()
        while i1 < len(nums) - 3:
            i2 = i1 + 1
            while i2 < len(nums) - 2:
                i = i2 + 1
                j = len(nums) - 1
                while i < j:
                    if nums[i1] + nums[i2] + nums[i] + nums[j] == target:
                        if [nums[i1], nums[i2], nums[i], nums[j]] not in res:
                            res.append([nums[i1], nums[i2], nums[i], nums[j]])
                        # res.append([i1, i2, i, j])
                        i += 1
                        while nums[i - 1] == nums[i] and i < j:
                            i += 1
                    elif nums[i1] + nums[i2] + nums[i] + nums[j] < target:
                        i += 1
                    else:
                        j -= 1
                i2 += 1
            i1 += 1
        return res


f = Solution()
# print(f.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
print(f.fourSum(nums=[2, 2, 2, 2, 2, 2], target=8))
