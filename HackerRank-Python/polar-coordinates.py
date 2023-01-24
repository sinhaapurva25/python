# complexNumArr = ['1+2j','1-2j','-1+2j','-1-2j']
# for complexNum in complexNumArr:
#     w = complexNum
#     realSign = '+'
#     realVal = 0
#     complexSign = '+'
#     complexVal = 0
#     if complexNum[0]=='-':
#         w = complexNum[1:]
#         realSign = '-'
#     if w.find('+')>-1:
#         realVal =  w.partition('+')[0]
#         complexSign =  w.partition('+')[1]
#         complexVal =  w.partition('+')[2]
#     elif w.find('-')>-1:
#         realVal =  w.partition('-')[0]
#         complexSign =  w.partition('-')[1]
#         complexVal =  w.partition('-')[2]
#     print(realSign,realVal,complexSign,complexVal)
import cmath
print(*cmath.polar(complex(input())), sep='\n')