class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        nums2_copy = nums2

        i = j = k = 0
        while i < m and j < n:
            if nums1_copy[i] < nums2_copy[j]:
                nums1[k] = nums1_copy[i]
                k += 1
                i += 1
            elif nums2_copy[j] < nums1_copy[i]:
                nums1[k] = nums2_copy[j]
                k += 1
                j += 1
            else:
                nums1[k] = nums1_copy[i]
                k += 1
                i += 1
                nums1[k] = nums2_copy[j]
                k += 1
                j += 1

        while i < m:
            nums1[k] = nums1_copy[i]
            k += 1
            i += 1

        while j < n:
            nums1[k] = nums2_copy[j]
            k += 1
            j += 1


f = Solution()

print("***** start *****")
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
f.merge(nums1, m, nums2, n)
print(nums1, nums2)
print("***** end *****")

# print("***** start *****")
# nums1 = [1]
# m = 1
# nums2 = []
# n = 0
# f.merge(nums1, m, nums2, n)
# print(nums1, nums2)
# print("***** end *****")
#
# print("***** start *****")
# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1
# f.merge(nums1, m, nums2, n)
# print(nums1, nums2)
# print("***** end *****")
