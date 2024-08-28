class Hashtable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_fun(self, key):
        i = 0
        for char in key:
            i += ord(char)
        index = i % self.size
        return index

    def insert(self, key, value):
        index = self.hash_fun(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            found = False
            for ind, element in enumerate(self.table[index]):
                if len(element) == 2 and element[0] == key:
                    self.table[index][ind] = (key, value)
                    found = True
            if not found:
                self.table[index].append((key, value))

    def delete(self, key):
        index = self.hash_fun(key)
        if self.table[index] is not None:
            for ind, element in enumerate(self.table[index]):
                if len(element) == 2 and element[0] == key:
                    self.table[index][ind] = None

    def disp(self, key):
        index = self.hash_fun(key)
        if self.table[index] is not None:
            for element in self.table[index]:
                if element[0] == key:
                    return element[1]
        return None

# Example usage:
h = Hashtable(10)
h.insert("name", "john")
h.insert("age", 30)
print(h.disp("name"))  # Output: john

h.insert("march 6", 67)
h.insert("march 17", 66)
print(h.table)
h.delete("march 6")
print(h.table)
