class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def preorder_iterator(context, root):
    if context is None:
        context = [root]
    top = context.pop(-1)
    if top.right_child:
        context.append(top.right_child)
    if top.left_child:
        context.append(top.left_child)
    return context, top.value

