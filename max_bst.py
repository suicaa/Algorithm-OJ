class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def is_bst(root):
    if root.left_child is not None:
        if root.left_child.value >= root.value:
            return False
        if root.right_child.value <= root.value:
            return False
        else:
            if root.left_child:
                return is_bst(root.left_child)
            if root.right_child:
                return is_bst(root.right_child)
    return True

def max_bst(root):
    if is_bst(root) is True:
        while root.right_child:
            a = root.right_child.value
        return a
    else:
        root = max(root.value, root.left_child.value, root.right_child.value)

        if root.left_child:
            return is_bst(root.left_child)
        if root.right_child:
            return is_bst(root.right_child)
