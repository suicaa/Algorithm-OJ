class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def equal(a, b):
    if a is None or b is None:
        return a is b

    if a.value != b.value:
        return False
    else:
        return equal(a.left_child, b.left_child) and equal(a.right_child, b.right_child)
