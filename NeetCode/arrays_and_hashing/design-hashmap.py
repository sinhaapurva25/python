class MyHashMap:

    def __init__(self):
        self.MAX = 1000
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key) -> int:
        return key % self.MAX

    def put(self, key: int, value: int) -> None:
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
        if not found:
            self.arr[h].append((key, value))

    def get(self, key: int) -> int:
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]
        return -1

    def remove(self, key: int) -> None:
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                del self.arr[arr_index][index]