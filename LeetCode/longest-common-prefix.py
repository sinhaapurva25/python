class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if len(strs) == 1:
            return strs[0]

        min_str_length = float('inf')

        for i in range(len(strs)):
            if len(strs[i]) < min_str_length:
                min_str_length = len(strs[i])

        res = ''
        for j in range(min_str_length):
            c = strs[0][j]
            arr = [1 if i[j] == c else 0 for i in strs[1:]]
            if sum(arr) == len(strs[1:]):
                res += c
            else:
                break
        return res


f = Solution()
print(f.longestCommonPrefix(strs=["flower", "flow", "flight"]))
print(f.longestCommonPrefix(strs=["dog", "racecar", "car"]))
