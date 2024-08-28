class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def print_leaf_nodes(node):
    if node:
        if not node.left and not node.right:
            print(node.key, end=" ")
        print_leaf_nodes(node.left)
        print_leaf_nodes(node.right)

# Example usage:
if __name__ == '__main__':
    bst_root = None

    keys = [10, 5, 15, 3, 7, 12, 18, 2, 4, 6, 8, 11, 13, 17, 19, 1, 9, 14, 16, 20]

    for key in keys:
        bst_root = insert(bst_root, key)

    print("Leaf nodes of the BST:")
    print_leaf_nodes(bst_root)
