def func(s):
    if s == 0 or len(s) % 2 == 1:
        return 0
    else:
        res = 1
        for i in range(1, len(s), 2):
            if s[i-1]+s[i] not in ['()', '{}', '[]']:
                res *= 0
                break
        return res


s = ['apurva', '{}[]()', '}[]()', '[}[]()']
[print(f'func("{i}")={func(i)}') for i in s]
