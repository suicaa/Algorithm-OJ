class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def tree_copy(root):
    if root is None:
        return None
    if root:
        b = TreeNode(root.value)
        b.left_child = tree_copy(root.left_child)
        b.right_child = tree_copy(root.right_child)
    return b
