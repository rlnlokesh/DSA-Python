class HashtableDoubleHashing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_fun(self, key):
        i = 0
        for char in key:
            i += ord(char)
        return i % self.size

    def hash_fun2(self, key):
        # Use a different hash function for double hashing
        return 7 - (ord(key[0]) % 7)

    def insert(self, key, value):
        index = self.hash_fun(key)
        step = self.hash_fun2(key)

        while self.table[index] is not None:
            if len(self.table[index]) == 2 and self.table[index][0] == key:
                self.table[index] = (key, value)  # Update value if key already exists
                return
            index = (index + step) % self.size

        self.table[index] = (key, value)

    def delete(self, key):
        index = self.hash_fun(key)
        step = self.hash_fun2(key)

        while self.table[index] is not None:
            if len(self.table[index]) == 2 and self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + step) % self.size

    def disp(self, key):
        index = self.hash_fun(key)
        step = self.hash_fun2(key)

        while self.table[index] is not None:
            if len(self.table[index]) == 2 and self.table[index][0] == key:
                return self.table[index][1]
            index = (index + step) % self.size

        return None

# Example usage:
h = HashtableDoubleHashing(10)
# h.insert("name", "john")
# h.insert("age", 30)
# print(h.disp("name"))  # Output: john
#
# h.insert("march 6", 67)
# h.insert("march 17", 66)
# print(h.table)
#
# h.delete("march 6")
# print(h.table)

h.insert("apple",5)
h.insert("banana",7)
h.insert("orange",9)

print(h.disp("banana"))
print(h.disp("apple"))
print(h.disp("orange"))

h.delete("banana")
print(h.disp("banana"))