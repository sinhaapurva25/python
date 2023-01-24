X = int(input())
# shoeSizes = [int(i) for i in input().split()]
shoeSizes = list(map(int,input().split()))
N = int(input())

amountEarned = 0
for i in range(N):
    shoeSizeWanted,amount = [int(i) for i in input().split()]
    if shoeSizeWanted in shoeSizes:
        amountEarned += amount
        removeIndex = shoeSizes.index(shoeSizeWanted)
        shoeSizes.pop(removeIndex)
print(amountEarned)