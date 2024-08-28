class hashtable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size
    def hash_fun(self,key):
        i = 0
        for char in key:
            i+=ord(char)
        index = i%self.size
        print(index)

    def insert(self,key,value):
        index = self.hash_fun(key)
        self.table[index]=value
    def delete(self,key):
        index = self.hash_fun(key)
        self.table[index]=None
    def disp(self,key):
        index = self.hash_fun(key)
        return self.table[index]

h=hashtable(10)
# h.insert("name","john")
# h.insert("age",30)
# print(h.disp("name"))
h.hash_fun("march 6")
h.hash_fun("march 17")