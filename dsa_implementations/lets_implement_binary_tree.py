from typing import List

# use this class to initiate left and right nodes with value
class TreeNode:
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    # insertion
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            # we call this to place our node at the right position
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            # first check if left child exists
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            # first check if right child exists
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    # helper function of in-order traversal
    def _inorder_recursive(self, node, result) -> List[int]:
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
        return result

    def inorder_traversal(self):
        return self._inorder_recursive(self.root, [])
    
def main():
    tree = BinaryTree()
    
    # insert values
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    tree.insert(12)
    tree.insert(17)

    # print the values sorted
    print(tree.inorder_traversal())

if __name__ == "__main__":
    main()