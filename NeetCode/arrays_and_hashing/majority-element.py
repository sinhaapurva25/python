class Solution:
    def majorityElement(self, nums: list) -> int:
        dct = {}
        for i in nums:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        mx_k = -1
        mx_v = 0
        for k, v in dct.items():
            if v > mx_v:
                mx_k = k
                mx_v = v
        return mx_k


f = Solution()
print(f.majorityElement(nums=[3, 2, 3]))
print(f.majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]))
