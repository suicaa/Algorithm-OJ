class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

list = []
def postorder_traverse(root):
    if root:
        postorder_traverse(root.left_child)
        postorder_traverse(root.right_child)
        list.append(root.value)
    return list
