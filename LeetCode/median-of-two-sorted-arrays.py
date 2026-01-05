class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        i = j = k = 0
        m = len(nums1)
        n = len(nums2)
        l = ((m + n) // 2) + 1

        while i < m and j < n and k < l:
            if nums1[i] < nums2[j]:
                i += 1
                k += 1
            elif nums2[j] < nums1[i]:
                j += 1
                k += 1
            else:
                i += 1
                j += 1
                k += 2
        while i < m and k < l:
            i += 1
            k += 1
        while j < n and k < l:
            j += 1
            k += 1

        m1 = nums1[i - 1]
        m2 = nums2[j - 1]
        k -= 1

        if k % 2 == 0:
            return float(m1)
        else:
            return (float(m1) + float(m2)) / 2.0


# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         i = j = k = 0
#         m = len(nums1)
#         n = len(nums2)
#         l = (m + n) // 2
#
#         while i < m and j < n and k <= l:
#             if nums1[i] < nums2[j]:
#                 i += 1
#                 k += 1
#             elif nums2[j] < nums1[i]:
#                 j += 1
#                 k += 1
#             else:
#                 i += 1
#                 j += 1
#                 k += 2
#         while i < m and k <= l:
#             i += 1
#             k += 1
#         while j < n and k <= l:
#             j += 1
#             k += 1
#
#         # return "i:{}, j:{}, k: {}".format(i-1, j-1, k-1)
#         i -= 1
#         j -= 1
#         k -= 1
#
#         if k % 2 == 0:
#             return float(nums1[i])
#         else:
#             return float((nums1[i] + nums2[j]) / 2)


s = Solution()
print(s.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
# print(s.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
# print(s.findMedianSortedArrays([-33, 0, 1, 3, 5], [-1, 2, 6]))
# print(s.findMedianSortedArrays([0, 2, 4], [1, 3, 5]))
# print(s.findMedianSortedArrays(nums1=[1, 2, 4], nums2=[1, 3, 4]))
# print(s.findMedianSortedArrays(nums1=[1, 2, 4], nums2=[1, 3, 4, 8, 90]))
# print(s.findMedianSortedArrays(nums1=[], nums2=[]))
# print(s.findMedianSortedArrays(nums1=[], nums2=[0]))
