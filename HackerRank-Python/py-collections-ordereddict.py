N = int(input())
collection = {}
for i in range(N):
    net_price, *item_name = [i for i in input().split()][::-1]
    net_price = int(net_price)
    item_name = ' '.join(item_name[::-1])
    if item_name in collection:
        collection[item_name] += int(net_price)
    else:
        collection[item_name] = int(net_price)
[print(key,val) for key,val in collection.items()]
# print(*collection.items(),sep='\n')
# a,*b = [1,2,3,4]
# print(a,b)