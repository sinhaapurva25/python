class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    # def get_hash(self, key):
    #     hash = 0
    #     for char in key:
    #         hash += ord(char)
    #     return hash % self.MAX

    def get_hash(self, key):
        return int(key.split(' ')[1])%10

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)

        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, kv in enumerate(self.arr[h]):
            if kv[0] == key:
                print("del",index)
                del self.arr[h][index]

hashtable = HashTable()

hashtable["march 6"]= 120
hashtable["march 16"]= 78
hashtable["march 1"]= 22
hashtable["march 2"]= 89
hashtable["march 15"]= 89
hashtable["march 5"]= 1
hashtable["march 25"]= 104
hashtable["march 7"]= 67
hashtable["march 17"]= 4
hashtable["march 27"]= 459

[print(i,'\n') for i in hashtable.arr if len(i) > 0]

print(hashtable["march 27"])

del hashtable["march 27"]

print(hashtable["march 27"])