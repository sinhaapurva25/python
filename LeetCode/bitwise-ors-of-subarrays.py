class Solution:
    def subarrayBitwiseORs(self, A: list) -> int:
        # sub_arr = set()
        # for i in range(len(arr)):
        #     bitwise_or = 0
        #     for j in range(i, len(arr)-1):
        #         bitwise_or |= arr[j+1]
        #         print(arr[i:j+1], bitwise_or)
        # # print(sub_arr)
        # return len(sub_arr)
        ans = set()
        cur = {0}
        for x in A:
            cur = {x | y for y in cur} | {x}
            print({x | y for y in cur}, {x})
            ans |= cur
        return len(ans)
s = Solution()
print(s.subarrayBitwiseORs([1,1,2]))
