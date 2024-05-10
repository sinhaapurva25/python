class Solution:

    def kthSmallestPrimeFraction(self, arr: list(), k: int) -> list():

        new_arr = dict()
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                new_arr[arr[i]/arr[j]] = str(arr[i]) + ':' + str(arr[j])
        return [int(i) for i in new_arr[sorted(new_arr).__getitem__(k - 1)].split(":")]

    # def kthSmallestPrimeFractionTimeLimitExceeded(self, arr: list(), k: int) -> list():
    #     l = 1
    #     r = 1
    #     left_arr = [0] * len(arr)
    #     right_arr = [0] * len(arr)
    #     prod_except_self = dict()
    #
    #     for i in range(len(arr)):
    #         if i > 0:
    #             l *= arr[i - 1]
    #             r *= arr[len(arr) - i]
    #         left_arr[i] = l
    #         right_arr[len(arr) - i - 1] = r
    #
    #     new_arr = dict()
    #     for i in range(len(arr)):
    #         for j in range(i + 1, len(arr)):
    #             f = left_arr[j] * right_arr[j]
    #             new_arr[int(arr[i] * f)] = str(arr[i]) + ':' + str(arr[j])
    #
    #     return [int(i) for i in new_arr[sorted(new_arr).__getitem__(k - 1)].split(":")]


s = Solution()
print(s.kthSmallestPrimeFraction(arr=[1, 2, 3, 5], k=3))
