class TreeNode:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class RootedTree:
    def __init__(self):
        self.root = None


__all__ = ["TreeNode", "RootedTree"]
