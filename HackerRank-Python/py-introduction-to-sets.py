def average(array):
    arr = []
    for i in array:
        if i not in arr:
            arr.append(i)
    sum = 0
    for i in arr:
        sum += i
    return sum/len(arr)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)