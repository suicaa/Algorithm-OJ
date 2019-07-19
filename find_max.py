class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def find_max(root):
    value = []
    if root.left_child:
        left_max = find_max(root.left_child)
        value.append(left_max)
    if root.right_child:
        right_max = find_max(root.right_child)
        value.append(right_max)
    value.append(root.value)

    return max(value)
