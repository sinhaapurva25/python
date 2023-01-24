from collections import defaultdict
# default_d = defaultdict(list)
# regular_d = dict()
# sample_list = [1,2,3]
# sample_tuple = (1,2,3)
# # print(regular_d[sample_list].append("value"))
# print(regular_d[sample_tuple].append("value"))

def def_value():
	return "Not Present"

d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2
 
print(d["a"])
print(d["b"])
print(d["c"])

print(d.__missing__("a"))
print(d.__missing__("b"))
print(d.__missing__("c"))
print(d.__missing__("d"))