# # O(m*n)
# class Solution:
#     def nextGreaterElement(self, nums1: list, nums2: list) -> list:
#         arr = [0] * len(nums1)
#         for i in range(len(nums1)):
#             idx = None
#             for j in range(len(nums2)):
#                 if nums1[i] == nums2[j]:
#                     idx = j
#                     break
#             res = -1
#             for j in nums2[idx + 1:]:
#                 if j > nums2[idx]:
#                     res = j
#                     break
#
#             arr[i] = res
#
#         return arr

# O(m+n)
class Solution:
    def nextGreaterElement(self, nums1: list, nums2: list) -> list:
        dct = {}
        for i in range(len(nums2)):
            mx = -1
            dct[nums2[i]] = mx
            if i < len(nums2) - 1 or i == 0:
                j = i + 1
                while i < j < len(nums2):
                    if nums2[j] > nums2[i]:
                        mx = nums2[j]
                        break
                    j += 1
            if mx > nums2[i] and mx != -1:
                dct[nums2[i]] = mx
        res = [0]*len(nums1)
        for i in range(len(nums1)):
            res[i] = dct[nums1[i]]
        return res


f = Solution()
print(f.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
print(f.nextGreaterElement([2, 4], nums2=[1, 2, 3, 4]))
print(f.nextGreaterElement([4, 1, 2], [1, 2, 3, 4]))
