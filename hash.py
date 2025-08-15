class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]
    
    def _hash_function(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])
    
    def get(self, key):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None
    
    def remove(self, key):
        index = self._hash_function(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                self.table[index].pop(i)
                return
    
    def print_table(self):
        for i, bucket in enumerate(self.table):
            print(f"Ячейка {i}: {bucket}")


ht = HashTable()
ht.put("apple", 5)
ht.put("banana", 10)
ht.put("ape", 15)  # Возможна коллизия с "apple" из-за хэша
ht.put("appl", 14)

print("Значение для 'appl':", ht.get("appl"))  # Вывод: 14
print("Значение для 'ape':", ht.get("ape"))  # Вывод: 15