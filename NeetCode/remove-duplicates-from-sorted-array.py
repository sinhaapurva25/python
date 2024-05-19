class Solution:
    def removeDuplicates(self, nums) -> int:
        lst = list()
        for i in range(len(nums)):
            if nums[i] not in lst:
                lst.append(nums[i])
        for i in range(len(lst)):
            nums[i] = lst[i]
        return len(lst)
f = Solution()
f.removeDuplicates([0, 1, 1, 1, 2, 2, 3, 3, 4])

# Next challenges:
# Remove Duplicates from Sorted Array II
# Apply Operations to an Array
# Sum of Distances