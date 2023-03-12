class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        dct = {}
        res = False
        for i in nums:
            if i in dct:
                dct[i] += 1
                res = True
                break
            else:
                dct[i] = 1
        return res

f = Solution()
print(f.containsDuplicate([1,2,3,1]))
print(f.containsDuplicate([1,2,3,4]))
print(f.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))