class Solution:
    def findLeastNumOfUniqueInts(self, arr, k: int) -> int:
        dct = dict()
        for i in arr:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        sorted_freq = sorted(dct.values(), key=lambda v: v)
        elements_removed = 0
        res = sorted_freq.copy()
        for key in sorted_freq:
            key_copy = key
            elements_removed += key
            res.remove(key_copy)
            if elements_removed > k:
                elements_removed -= key
                res.append(key_copy)
                break
        return len(res)


s = Solution()
print(s.findLeastNumOfUniqueInts(arr=[5, 5, 4], k=1))
print(s.findLeastNumOfUniqueInts(arr=[4, 3, 1, 1, 3, 3, 2], k=3))
print(s.findLeastNumOfUniqueInts(arr=[2, 1, 1, 3, 3, 3], k=3))

# Next challenges:
# Count Unhappy Friends
# Minimum Number of Operations to Convert Time
# Maximum Number of Alloys
