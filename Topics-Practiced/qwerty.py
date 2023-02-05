print('{:>d}'.format(11))
print('{:>X}'.format(11))
print('{:>o}'.format(11))
print('{:>b}'.format(11))
x = 4
squared_if_odd = 'A' if x == 1 else ('B' if x == 2 else ('C' if x == 3 else ('D' if x == 4 else 'E')))


def my_function(*kids):
    kid1, kid2, kid3 = kids
    print(kid1, kid2, kid3, kids)

my_function("Emil", "Tobias", "Linus")
arr = ['t', 'y', 'i', 'j']
print(arr[:-2])

print(''.join(list(map(str,map(int, [i in self._odd_months, i in self._even_months, self._leap_year(yy)])))))


