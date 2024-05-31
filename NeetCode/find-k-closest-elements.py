class Solution:
    def findClosestElements(self, arr: list, k: int, x: int) -> list:
        first_closest_element_index = self.get_first_closest_element_index(arr, k, x)
        i = first_closest_element_index

        res = arr[i]
        if arr[i] == x:
            a = i-1
            b = i+1
        else:
            a = i-1
            b = i
        count = 1
        while count < k:
            if arr[i] == x:
                i -= 1

    def get_first_closest_element_index(self, arr, k, x):
        if x <= arr[0]:
            return arr[:k]
        elif x >= arr[len(arr) - 1]:
            return arr[len(arr) - 1 - k:]
        else:
            i = 1
            while i < len(arr):
                if x == arr[i]:
                    return i
                elif arr[i - 1] <= x < arr[i]:
                    # return i
                    if x - arr[i - 1] <= arr[i] - x:
                        return i - 1
                    else:
                        return i
                i += 1
        return -1


f = Solution()
arr, k, x = [1, 2, 3, 4, 5], 4, 3
print("arr, k, x: {}, {}, {}".format(arr, k, x))
print(f.findClosestElements(arr, k, x))
arr, k, x = [1,2,3,4,5], 4, -1
print("arr, k, x: {}, {}, {}".format(arr, k, x))
print(f.findClosestElements(arr, k, x))
arr, k, x = [1,2,3,6,100], 4, 5
print("arr, k, x: {}, {}, {}".format(arr, k, x))
print(f.findClosestElements(arr, k, x))
arr, k, x = [1,2,4,7,100], 4, 5
print("arr, k, x: {}, {}, {}".format(arr, k, x))
print(f.findClosestElements(arr, k, x))