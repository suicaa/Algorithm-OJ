class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

dia = 0
def diameter(root):
    def lr(root):
        global dia
        if root is None:
            return 0
        left_layer = lr(root.left_child)
        right_layer = lr(root.right_child)
        dia = max(dia, left_layer + right_layer)
        return max(left_layer, right_layer) + 1
    lr(root)
    return dia
