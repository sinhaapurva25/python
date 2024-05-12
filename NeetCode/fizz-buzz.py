class Solution:
    def fizzBuzz(self, n: int) -> list:
        res = list()
        for i in range(1, n+1):
            if i%3==0 and i%5==0:
                res.append("FizzBuzz")
            elif i%3==0:
                res.append("Fizz")
            elif i%5==0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res


s = Solution()
print(s.fizzBuzz(n=3))

# Next challenges:
# Fizz Buzz Multithreaded
# Categorize Box According to Criteria
