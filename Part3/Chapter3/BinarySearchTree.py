from Part3.Chapter1.RootedTree import TreeNode, RootedTree


def inorder_tree_walk(x: TreeNode) -> None:
    if x is not None:
        inorder_tree_walk(x.left)
        print(x.key)
        inorder_tree_walk(x.right)


class BinarySearchTree(RootedTree):
    @staticmethod
    def __walk(x, forward, satisfy):
        while x is not None and satisfy(x, y := forward(x)):
            x = y
        return x

    def insert(self, z: TreeNode) -> None:
        y = self.__walk(self.root, lambda x: x.left if z.key < x.key else x.right, lambda x, y: y is not None)
        z.parent = y
        if y is None:
            self.root = z
        else:
            setattr(y, "left" if z.key < y.key else "right", z)

    def delete(self, z: TreeNode) -> None:
        y = z.parent
        if z.left is None or z.right is None:
            x = z.left or z.right
        else:
            x = self.successor(z)
            BinarySearchTree.delete(self, x)
            x.left = z.left
            x.right = z.right
            x.left.parent = x
            x.right.parent = x
        if x is not None:
            x.parent = y
        if y is None:
            self.root = x
        else:
            setattr(y, "left" if z == y.left else "right", x)

    def search(self, k) -> TreeNode:
        return self.__walk(self.root, lambda x: x.left if k < x.key else x.right, lambda x, y: x.key != k)

    def minimum(self, x: TreeNode = None, is_root: bool = True) -> TreeNode:
        return self.__walk(self.root if x is None and is_root else x, lambda x: x.left, lambda x, y: y is not None)

    def maximum(self, x: TreeNode = None, is_root: bool = True) -> TreeNode:
        return self.__walk(self.root if x is None and is_root else x, lambda x: x.right, lambda x, y: y is not None)

    def predecessor(self, x: TreeNode) -> TreeNode:
        return self.maximum(x.left, False) \
            or self.__walk(x, lambda x: x.parent, lambda x, y: y is not None and x == y.left).parent

    def successor(self, x: TreeNode) -> TreeNode:
        return self.minimum(x.right, False) \
            or self.__walk(x, lambda x: x.parent, lambda x, y: y is not None and x == y.right).parent


__all__ = ["TreeNode", "BinarySearchTree", "inorder_tree_walk"]
