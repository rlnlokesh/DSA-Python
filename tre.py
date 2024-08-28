class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+=1
            p = p.parent
        return level

    def print_tree(self,level):
        if self.get_level() > level:
            return

        spaces = "    " * self.get_level()
        print(spaces + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

def build_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Windows"))
    laptop.add_child(TreeNode("Linux"))

    phone = TreeNode("Mobiles")
    phone.add_child(TreeNode("Samsung"))
    phone.add_child(TreeNode("Real Me"))
    phone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TVS")
    tv.add_child(TreeNode("SmartTV"))
    tv.add_child(TreeNode("OldTV"))

    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(tv)

    # print(phone.get_level())
    return root

if __name__ == '__main__':
    a = build_tree()
    a.print_tree(2)
