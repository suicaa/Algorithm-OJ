class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

q = False
def next_node(value, root):
    global q
    if root is None:
        return None
    elif root.value == value:
        q = True
    elif q == True:
        return root.value

    left = next_node(value, root.left_child)
    if left:
        return left
    right = next_node(value, root.right_child)
    if right:
        return right
