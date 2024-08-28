class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def create_sample_tree(self):
        # Creating a sample binary tree
        self.root = TreeNode(1)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(3)
        self.root.left.left = TreeNode(4)
        self.root.left.right = TreeNode(5)
        self.root.right.left = TreeNode(6)
        self.root.right.right = TreeNode(7)

    def print_tree(self, root, level=0, prefix="Root: "):
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.value))
            self.print_tree(root.left, level + 1, "L--- ")
            self.print_tree(root.right, level + 1, "R--- ")

    def printt(self):
        # Call the print_tree method with the root of the tree
        return self.print_tree(self.root)

# Example usage
if __name__ == '__main__':
    t = Tree()
    t.create_sample_tree()
    t.printt()
