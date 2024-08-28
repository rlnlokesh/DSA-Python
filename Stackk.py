class Stackk:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def display(self):
         print(self.items)

def reverse(str):
    st = Stackk()
    r = ""
    for word in str:
        st.push(word)
    while st.size()!=0:
        r+=st.pop()
    return r

if __name__ == '__main__':
    s = Stackk()
    print(reverse("lokesh"))
    s.push(12)
    s.push(23)
    s.push(45)
    s.push(33)
    s.display()