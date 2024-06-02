class Solution:
    def canPlaceFlowers(self, flowerbed: list, n: int) -> bool:
        if len(flowerbed) == 1:
            return False if flowerbed[0]*n == 1 else True
        # if len(flowerbed) == 2:
        #     if n >= 2: return False
        #     elif n == 1: return ~bool(flowerbed[0] & flowerbed[1])
        #     else: return ~bool(flowerbed[0] | flowerbed[1])
        if len(flowerbed) == 2:
            if flowerbed == [0, 0] and n == 1:
                return True
        # find out the results for the above conditions
        if len(flowerbed) == 3:
            if flowerbed == [0, 0, 0]:
                return n <= 2
            if flowerbed == [0, 0, 1] or flowerbed == [1, 0, 0]:
                return n <= 1
            else:
                return n <= 0
        c = 0
        if flowerbed[0:4] == [0, 0, 0, 0]:
            flowerbed[1],  flowerbed[2]= 1, 1
            c += 2
        if flowerbed[-1:-5:-1] == [0, 0, 0, 0]:
            flowerbed[-1], flowerbed[-3] = 1, 1
            c += 2
        if flowerbed[0:4] == [1, 0, 0, 0]:
            flowerbed[2] = 1
            c += 1
        if flowerbed[-1:-5:-1] == [1, 0, 0, 0]:
            flowerbed[-3] = 1
            c += 1
        if flowerbed[0:3] == [0, 0, 1]:
            flowerbed[0] = 1
            c += 1
        if flowerbed[-1:-4:-1] == [0, 0, 1]:
            flowerbed[-1] = 1
            c += 1
        if flowerbed[0:3] == [0, 0, 0]:
            flowerbed[1] = 1
            c += 1
        if flowerbed[-1:-4:-1] == [0, 0, 0]:
            flowerbed[-2] = 1
            c += 1
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1:i + 2] == [0, 0, 0]:
                flowerbed[i] = 1
                c += 1
        return n <= c
f = Solution()
print(f.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1))
print(f.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2))
print(f.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 0, 1], n=2))
print(f.canPlaceFlowers(flowerbed=[0, 0, 1, 0, 1], n=1))
print(f.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1, 0, 0], n=2))

print(f.canPlaceFlowers(flowerbed=[0], n=0))
print(f.canPlaceFlowers(flowerbed=[0], n=1))
print(f.canPlaceFlowers(flowerbed=[1], n=0))
print(f.canPlaceFlowers(flowerbed=[1], n=1))

print(f.canPlaceFlowers(flowerbed=[0, 0], n=0))
print(f.canPlaceFlowers(flowerbed=[0, 1], n=0))
print(f.canPlaceFlowers(flowerbed=[1, 0], n=0))
print(f.canPlaceFlowers(flowerbed=[1, 1], n=0))
print(f.canPlaceFlowers(flowerbed=[0, 0], n=1))
print(f.canPlaceFlowers(flowerbed=[0, 1], n=1))
print(f.canPlaceFlowers(flowerbed=[1, 0], n=1))
print(f.canPlaceFlowers(flowerbed=[1, 1], n=1))

print(f.canPlaceFlowers(flowerbed=[0, 0, 0], n=0))
print(f.canPlaceFlowers(flowerbed=[0, 0, 1], n=0))
print(f.canPlaceFlowers(flowerbed=[0, 1, 0], n=0))
print(f.canPlaceFlowers(flowerbed=[0, 1, 1], n=0))
print(f.canPlaceFlowers(flowerbed=[0, 0, 0], n=1))
print(f.canPlaceFlowers(flowerbed=[0, 0, 1], n=1))
print(f.canPlaceFlowers(flowerbed=[0, 1, 0], n=1))
print(f.canPlaceFlowers(flowerbed=[0, 1, 1], n=1))

print(f.canPlaceFlowers(flowerbed=[1, 0, 0], n=0))
print(f.canPlaceFlowers(flowerbed=[1, 0, 1], n=0))
print(f.canPlaceFlowers(flowerbed=[1, 1, 0], n=0))
print(f.canPlaceFlowers(flowerbed=[1, 1, 1], n=0))
print(f.canPlaceFlowers(flowerbed=[1, 0, 0], n=1))
print(f.canPlaceFlowers(flowerbed=[1, 0, 1], n=1))
print(f.canPlaceFlowers(flowerbed=[1, 1, 0], n=1))
print(f.canPlaceFlowers(flowerbed=[1, 1, 1], n=1))

