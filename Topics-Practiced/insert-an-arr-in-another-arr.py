def insert_arr(ranked,players):
    ranked.sort()
    for j in range(len(players)):
        element = players[j]
        u = ranked.copy()
        for i in range(len(ranked)):
            if i == 0:
                if element <= ranked[i]:
                    u = [element] + ranked
                    break
                elif element in range(ranked[i-1],ranked[i]):
                    u = [ranked[i]] + [element] + ranked[i+1:]
                    break
            elif i == len(ranked) - 1:
                if element in range(ranked[i-1],ranked[i]):
                    u = ranked[:i] + [element] + [ranked[i]]
                    break
                elif element >= ranked[i]:
                    u = ranked + [element]
                    break
            else:
                if element in range(ranked[i-1]-1,ranked[i]+1):
                    u = ranked[:i] + [element] + ranked[i:]
                    break
        ranked = u
    return ranked

print(insert_arr([11,13,15,17,19],[10,12,12,14]))
print(insert_arr([9,12,13,14],[0,15,10,12]))
print(insert_arr([100,90,90,80],[70,80,105]))