class BSTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BSTreeNode(data)

    def leaf_nodes(self):
        if not self.left and self.right:
            print(self.data,end=" ")
        if self.left:
            self.left.leaf_nodes()
        if self.right:
            self.right.leaf_nodes()


    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            min = self.right.find_min()
            self.data = min
            self.right = self.right.delete(min)

        return self


    def searchh(self,val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.searchh(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.searchh(val)
            else:
                return False

    def inorder(self):
        if self.data:
            self.left.inorder() if self.left else None
            print(str(self.data) + "-->", end="")
            self.right.inorder() if self.right else None

    def postorder(self):
        if self.data:
            self.left.postorder() if self.left else None
            self.right.postorder() if self.right else None
            print(str(self.data) + "-->", end="")

    def preorder(self):
        if self.data:
            print(str(self.data)+"-->",end="")
            self.left.preorder() if self.left else None
            self.right.preorder() if self.right else None

def build_bst(elements):
    root = BSTreeNode(elements[0])
    for i in range(1 , len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numberss = [1,4,9,17,18,20,23,34,3,21,313,21,36,465,346]
    numbers_tree = build_bst(numberss)
    numbers_tree.delete(9)
    numbers_tree.postorder()
    print("")
    numbers_tree.leaf_nodes()
    # print("max is ",numbers_tree.find_max())
    # print("min is ",numbers_tree.find_min())
    # numbers_tree.inorder()
    # print("inorder")
    # numbers_tree.postorder()
    # print("postorder")
    # numbers_tree.preorder()
    # print("preorder")
    # print(numbers_tree.searchh(1200))