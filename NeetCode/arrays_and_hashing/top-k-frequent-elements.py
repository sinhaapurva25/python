class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        dct = dict()
        res = []
        mx = 0
        for i in nums:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
            if dct[i] > mx:
                mx = dct[i]
                res = [i]
        if len(res) == 1:
            mx2 = mx+1
            for k, v in dct.items():
                if k!=res[0]:
                    if mx-v <= mx2:
                        mx2 = v
            if mx2!=mx+1:
                res.append(mx2)
        return res

f = Solution()
print(f.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(f.topKFrequent(nums = [1], k = 1))