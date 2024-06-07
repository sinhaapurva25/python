class Solution:
    def getAllTriplets(self, nums: list, diff: int):
        t = list()
        print("[nums[i], nums[j], nums[k]], (i, j, k), nums[k]-nums[i], k-i)")
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    # t.append("[{}, {}, {}], {}, {}".format(nums[i], nums[j], nums[k], nums[k]-nums[i], k-i))
                    print("[{}, {}, {}], ({}, {}, {}), {}, {}".format(nums[i], nums[j], nums[k], i, j, k, nums[k]-nums[i], k-i))
        return t

    def arithmeticTriplets(self, nums: list, diff: int) -> int:
        i = 0
        k = len(nums) - 1
        idx = 0
        res = 0
        while idx < len(nums):
            if nums[k] - nums[i] == 2 * diff:
               res += 1
            elif nums[k] - nums[i] < 2 * diff:
                k -= 1
            else:
                i += 1
            idx += 1
        return res

f = Solution()

nums = [4,5,6,7,8,9]
diff = 2
print(f.arithmeticTriplets(nums, diff))
print(f.getAllTriplets(nums, diff)) # 6, 3

nums = [0,1,4,6,7,10]
diff = 3
print(f.arithmeticTriplets(nums, diff))
print(f.getAllTriplets(nums, diff))

# Next challenges:
# Number of Unequal Triplets in Array
# Maximum Value of an Ordered Triplet I
# Minimum Sum of Mountain Triplets I

