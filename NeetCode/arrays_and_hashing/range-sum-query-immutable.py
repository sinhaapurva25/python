class NumArray:

    def __init__(self, nums: list):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])

# Your NumArray object will be instantiated and called as such:
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
obj = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(0, 2)
print(param_1)
param_2 = obj.sumRange(2, 5)
print(param_2)
param_3 = obj.sumRange(0, 5)
print(param_3)