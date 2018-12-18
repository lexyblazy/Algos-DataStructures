

class HashTable:
    def __init__(self, size=53):
        self.keyMap = [None] * size

    def __repr__(self):
        return "{}".format(self.keyMap)

    def _hash(self, key):
        total = 0
        prime = 227
        for i in range(min(100, len(key))):
            value = ord(key[i]) - 97
            total = (total*prime+value) % (len(self.keyMap))
        return total

    def set(self, key, value):
        hashedKey = self._hash(key)
        if self.keyMap[hashedKey] is None:
            self.keyMap[hashedKey] = [[key, value]]
        else:
            self.keyMap[hashedKey].append([key, value])

    def get(self, key):
        hashedKey = self._hash(key)
        result = self.keyMap[hashedKey]
        if not result:
            return "does not exist"
        if(len(result) == 1):
            return result[0][1]
        for res in result:
            if(res[0] == key):
                return res[1]

    def values(self):
        values = []
        for el in self.keyMap:
            if el is not None:
                for value in el:
                    values.append(value[1])
        print(values)
        return values


hash = HashTable(10)
hash.set("_id", "jdskhdsew78jsd")
hash.set("color", "red")
hash.set("name", "brian")
hash.set("email", "brian@gmail.com")
hash.set("phone", "09083289273")
# print(hash)
# print(hash.get("name"))
# print(hash.get("email"))
# print(hash.get("_id"))
hash.values()
