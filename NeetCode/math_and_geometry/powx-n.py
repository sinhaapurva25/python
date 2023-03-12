class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        elif n == 1:
            return x

        elif n == -1:
            return 1 / x

        if x == 1:
            return 1

        elif x == 0:
            return 0

        else:
            if str(x).find('e') > -1:
                index_of_e = str(x).find('e')
                if str(x).find('.') == -1:
                    number_of_dig_after_decimal = index_of_e - 1 + int(str(x)[index_of_e + 1:]) * -1
                    x = int(str(x)[:index_of_e])
                else:
                    number_of_dig_after_decimal = index_of_e - str(x).find('.') - 1 + int(str(x)[index_of_e + 1:]) * -1
                    x = int(str(x)[:index_of_e].replace('.', ''))
            else:
                if str(x).find('.') == -1:
                    number_of_dig_after_decimal = 0
                else:
                    digits_after_decimal = str(x)[str(x).find('.') + 1:]
                    if digits_after_decimal != '0':
                        number_of_dig_after_decimal = len(str(x)) - str(x).find('.') - 1
                        x = int(str(x).replace('.', ''))
                    else:
                        number_of_dig_after_decimal = 0
                        x = int(x)

            d = '1'
            for i in range(number_of_dig_after_decimal):
                d += '0'
            d = int(d)


            if x == 0:
                p = 0
            else:
                if x > 0:
                    if x == 1:

                        # runtime error
                        # if n < 0:
                        #     r = range(n * -1)
                        # else:
                        #     r = range(n)
                        # if d!= 1:
                        #     for i in r:
                        #         div *= d

                        # memory error
                        # if d != 1:
                        #     div = int('1' + ''.join(['0'] * len(str(d)[1:]) * abs(n)))

                        p = 1
                        x /= d
                        if d!= 1:
                            for i in range(abs(n)):
                                p *= x
                                if p == 0:
                                    break
                    else:
                        p = 1
                        x /= d
                        for i in range(abs(n)):
                            p *= x
                            if p == 0:
                                break

                        if n < 0:
                            p = 1 / p
                else:
                    if x == -1:
                        if n % 2 == 0:
                            p = 1
                        else:
                            p = -1

                        # p = 1
                        x /= d
                        if d != 1:
                            for i in range(abs(n)):
                                p *= x
                                if p == 0:
                                    break
                    else:
                        if n == 1:
                            p = 1
                            x /= d
                            if d != 1:
                                for i in range(abs(n)):
                                    p *= x
                                    if p == 0:
                                        break
                        elif n == -1:
                            p = 1
                            x /= d
                            if d != 1:
                                for i in range(abs(n)):
                                    p *= x
                                    if p == 0:
                                        break
                            p = 1 / p
                        else:
                            p = 1
                            x /= d
                            for i in range(abs(n)):
                                p *= abs(x)
                                if p == 0:
                                    break
                            if n < 0:
                                if n % 2 == 0:
                                    p = 1 / p
                                else:
                                    p = (1 / p) * -1
                            else:
                                if n % 2 == 1:
                                    p = (-1) * p
            return p

f = Solution()
print(f.myPow(x=0.00001, n=2147483647)==0.0)
print(f.myPow(x=2.00000, n=10)==1024.0)
print(f.myPow(x=2.00000, n=10)==1024.0)
print(f.myPow(x=2.10000, n=3)==9.261000000000001)
print(f.myPow(x=2.00000, n=-2)==0.25)
print(f.myPow(x=2.10200, n=3)==9.287485208)
print(f.myPow(x=0.000000123, n=2)==1.5129e-14)  #9
print(f.myPow(x=-0.000000123, n=2)==1.5129e-14)  #9
print(f.myPow(x=0.12300, n=2)==0.015129)  #3
print(f.myPow(x=0.123, n=2)==0.015129)  #3
print(f.myPow(x=-0.12300, n=2)==0.015129)  #3
print(f.myPow(x=-0.123, n=2)==0.015129)  #3
print(f.myPow(x=0.0001, n=2)==1e-08)  #4
print(f.myPow(x=-0.0001, n=2)==1e-08)  #4
print(f.myPow(x=0.00001, n=2)==1.0000000000000002e-10)  #5
print(f.myPow(x=0.00001000, n=2)==1.0000000000000002e-10)  #5
print(f.myPow(x=3, n=2)==9.0)  #0
print(f.myPow(x=8.88023, n=3)==700.2814829452681)#700.2814829452682
print(f.myPow(x=17.37328, n =3)==5243.7920079515125)#5243.79201
print(f.myPow(x=2.00000, n =-2147483648), f.myPow(x=2.00000, n =-2147483648)==0.0)#5243.79201
                           #-2147483648
