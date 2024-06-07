class Solution:
    def removeDuplicates(self, nums) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j


f = Solution()
num = [0, 1, 1, 1, 2, 2, 3, 3, 4]
f.removeDuplicates(num)
print(num)

num = [1, 2, 2, 3, 4, 4, 4, 5, 100]
f.removeDuplicates(num)
print(num)
# Next challenges:
# Remove Duplicates from Sorted Array II
# Apply Operations to an Array
# Sum of Distances
