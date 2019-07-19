class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def height(root):
    if root:
        return 1 + max(height(root.left_child), height(root.right_child))
    else:
        return -1
