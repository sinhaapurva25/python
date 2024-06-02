class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        freq = dict()
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        sorted_array = [key for key, val in sorted(freq.items(), key=lambda item: item[1], reverse=True)]
        if len(sorted_array) <= k:
            return sorted_array
        else:
            return sorted_array[:k]
        # ==================================
        # frq = dict()
        # for i in range(len(nums)):
        #     if nums[i] in frq:
        #         frq[nums[i]] += 1
        #     else:
        #         frq[nums[i]] = 1
        # sorted_frq = sorted(frq.items(), key=lambda item: item[1], reverse=True)
        # return [i[0] for i in sorted_frq][:k]


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], k=2))
print(s.topKFrequent(nums=[1], k=1))
