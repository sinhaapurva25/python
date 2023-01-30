class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for i in key:
            hash += ord(i)
        return hash % self.MAX

    def __setitem__(self, date, temp):
        h = self.get_hash(date)
        if len(self.arr[h]) > 0:
            self.arr[h].append((date, temp))
        else:
            self.arr[h] = [(date, temp)]

    def read_file(self, file_name):
        with open(file_name,'r') as f:
            lines = f.readlines()
        for l in lines[1:]:
            date, temp = l.rstrip().split(',')
            # self.add(date, temp)
            self[date] = temp

    def __getitem__(self, item):
        hash = self.get_hash(item)
        res = None
        if len(self.arr[hash]) > 1:
            for i in self.arr[hash]:
                if i[0] == item:
                    res = i[1]
                    break
            return res
        else:
            res = self.arr[hash][0][1]
        return res

    def get_avg(self, first_n_days=7):
        s = 0
        for i in range(1, first_n_days+1):
            k = 'Jan '+str(i)
            s += 0 if None else int(self[k])
        return s/first_n_days

    def get_max(self, first_n_days=10):
        res = 0
        for i in range(1, first_n_days+1):
            # print('Jan '+str(i), self['Jan '+str(i)])
            val = int(self['Jan '+str(i)])
            if val > res:
                res = val
        return res


ht = HashTable()
ht.read_file(r'nyc_weather.csv')
[print(i) for i in ht.arr]
print(ht['Jan 1'])

# 1
print('\n')
print('# 1')
print(ht.get_avg())
print(ht.get_max())

# 2
print('\n')
print('# 2')
print(ht['Jan 9'])
print(ht['Jan 4'])
