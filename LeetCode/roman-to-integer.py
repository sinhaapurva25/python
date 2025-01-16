class Solution:
    def romanToInt(self, s: str) -> int:
        # value - [intValue, index]
        lookupDict = {
            'I': (1, 0),'V': (5, 1),'X': (10, 2),'L':(50, 3),'C':(100, 4),'D':(500, 5),'M':(1000, 6)
        }
        # s - LVIII
        # s - III
        return_value = 0
        idx=0
        while(idx < (len(s)-1)):
            curr = s[idx] # L - 3
            next = s[idx+1] # V - 1
            if(lookupDict[next][1] > lookupDict[curr][1]):
                return_value += lookupDict[curr][0]
                idx += 1
            elif(lookupDict[next][1] < lookupDict[curr][1]):
                tmp = lookupDict[next][0] - lookupDict[curr][0]
                print("tmp:", tmp)
                return_value += tmp
                idx += 2
            else:
                tmp = lookupDict[next][0] + lookupDict[curr][0]
                return_value += tmp
                idx+=2
            print("return_value: ", return_value)
        return return_value
f = Solution()
# print(f.romanToInt('III'))
print(f.romanToInt('LVIII'))
# print(f.romanToInt('MCMXCIV'))

class Solution:
    def romanToInt(self, s: str) -> int:
        # value - [intValue, index]
        lookupDict = {
            'I': (1, 0), 'V': (5, 1), 'X': (10, 2), 'L': (50, 3), 'C': (100, 4), 'D': (500, 5), 'M': (1000, 6)
        }
        # s - LVIII
        # s - III
        return_value = 0
        idx = 0
        while (idx < (len(s) - 1)):
            curr = s[idx]  # L - 3
            next = s[idx + 1]  # V - 1
            if (lookupDict[next][1] > lookupDict[curr][1]):
                return_value += lookupDict[curr][0]
                idx += 1
            elif (lookupDict[next][1] < lookupDict[curr][1]):
                tmp = lookupDict[next][0] - lookupDict[curr][0]
                print("tmp:", tmp)
                return_value += tmp
                idx += 2
            else:
                tmp = lookupDict[next][0] + lookupDict[curr][0]
                return_value += tmp
                idx += 2
            print("return_value: ", return_value)
        return return_value
