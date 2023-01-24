## https://pydash.readthedocs.io/en/latest/
import pydash
print("flatten",pydash.flatten([1,
                      2,
                      [3, [4, 5, [6, 7]]]]))
print("flatten_deep",pydash.flatten_deep([1,
                     2,
                     [3, [4, 5, [6, 7]]]]))

print(pydash.map_([{'name': 'moe', 'age': 40}, {'name': 'larry', 'age': 50}], 'ui')) #if key is not present, you'll get None

curried = pydash.curry(lambda a, b, c: a + b + c)
print(curried(1, 2)(3))