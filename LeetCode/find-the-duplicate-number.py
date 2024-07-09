from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # BRUTE FORCE -> Time Exceeded Exception
        # for i in range(len(nums)):
        #     j = nums[:i] + nums[i+1:]
        #     if nums[i] in j:
        #         return nums[i]

        # BRUTE FORCE -> Passed
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         return nums[i]
        slow = fast = 0
        while True:
            # print("slow: {}, fast: {}".format(slow, fast))
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                # slow and fast becomes equal because it's cyclic
                break
        slow = 0
        while slow != fast:
            # print("slow: {}, fast: {}".format(slow, fast))
            slow = nums[slow]
            fast = nums[fast]
        return slow


s = Solution()
tc = [[[1, 3, 4, 2, 2], 2],
      [[3, 1, 3, 4, 2], 3],
      [[3, 3, 3, 3, 3], 3],
      [[2, 6, 4, 1, 3, 1, 5], 1],
      [[2, 5, 9, 6, 9, 3, 8, 9, 7, 1], 9]]
for nums in tc:
    input = nums[0]
    expected = nums[1]
    print("Test Case", end=" ")
    if s.findDuplicate(input) == expected:
        print("Passed")
    else:
        print("Failed")
