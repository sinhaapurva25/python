class Solution:
    def leftRightDifference(self, nums):
        left_arr = [0 for i in range(len(nums))]
        right_arr = [0 for i in range(len(nums))]

        for i in range(len(nums)):
            if i == 0:
                left_arr[i] = 0
            if i == len(nums) - 1:
                right_arr[len(nums) - i - 1] = 0

            left_arr[i] = sum(nums[:i])
            right_arr[len(nums) - i - 1] = sum(nums[(len(nums) - i):])

        print(left_arr, right_arr)

        res = list()
        for i in range(len(nums)):
            d = left_arr[i]-right_arr[i]
            res.append(d if d > 0 else d*-1)

        return res
s = Solution()
print(s.leftRightDifference(nums = [10,4,8,3]))