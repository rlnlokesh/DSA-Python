class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.data)+"-->",end="")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.data) + "-->", end="")

def preorder(root):
    if root:
        print(str(root.data)+"-->",end="")
        preorder(root.left)
        preorder(root.right)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.left=Node(7)

print("Inorder Transversal")
inorder(root)

print("\nPreorder Transversal")
preorder(root)

print("\nPostorder Transversal")
postorder(root)