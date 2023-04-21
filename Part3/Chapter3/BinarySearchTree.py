from Part3.Chapter1.RootedTree import TreeNode, RootedTree


def inorder_tree_walk(x: TreeNode) -> None:
    if x is not None:
        inorder_tree_walk(x.left)
        print(x.key)
        inorder_tree_walk(x.right)


class BinarySearchTree(RootedTree):
    def insert(self, z: TreeNode) -> None:
        x = self.root
        y = None
        while x is not None:
            y = x
            x = getattr(x, "left" if z.key < x.key else "right")
        z.parent = y
        if y is None:
            self.root = z
        else:
            setattr(y, "left" if z.key < y.key else "right", z)

    def delete(self, z: TreeNode) -> TreeNode:
        y = z.parent
        if z.left is None or z.right is None:
            x = z.left or z.right
        else:
            x = self.delete(self.successor(z))
            x.left = z.left
            x.right = z.right
        if x is not None:
            x.parent = y
        if y is None:
            self.root = x
        else:
            setattr(y, "left" if z == y.left else "right", x)
        return x

    def search(self, k) -> TreeNode:
        x = self.root
        while x is not None and x.key != k:
            x = getattr(x, "left" if k < x.key else "right")
        return x

    def minimum(self, x: TreeNode = None, is_root: bool = True) -> TreeNode:
        x = self.root if x is None and is_root else x
        if x is not None:
            while x.left is not None:
                x = x.left
        return x

    def maximum(self, x: TreeNode = None, is_root: bool = True) -> TreeNode:
        x = self.root if x is None and is_root else x
        if x is not None:
            while x.right is not None:
                x = x.right
        return x

    def predecessor(self, x: TreeNode) -> TreeNode:
        if x.left is not None:
            return self.maximum(x.left)
        y = x.parent
        while y is not None and x == y.left:
            x = y
            y = x.parent
        return y

    def successor(self, x: TreeNode) -> TreeNode:
        if x.right is not None:
            return self.minimum(x.right)
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = x.parent
        return y


__all__ = ["TreeNode", "BinarySearchTree"]
