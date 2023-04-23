from Part3.Chapter3.BinarySearchTree import TreeNode, BinarySearchTree


class RBTree(BinarySearchTree):
    def __init__(self):
        super().__init__()
        self.null = TreeNode(None)
        self.null.color = "black"

    @staticmethod
    def __get_color(x):
        return "black" if x is None else x.color

    @staticmethod
    def __turn_around(forward):
        return "right" if forward == "left" else "left"

    def __rotate(self, x, forward):
        backward = self.__turn_around(forward)
        p = x.parent
        y = getattr(x, backward)
        z = getattr(y, forward)
        y.parent = p
        if p is None:
            self.root = y
        else:
            setattr(p, "left" if x == p.left else "right", y)
        x.parent = y
        setattr(y, forward, x)
        if z is not None:
            z.parent = x
        setattr(x, backward, z)

    def __insert_fixup(self, z):
        while self.__get_color(y := z.parent) == "red":
            p = y.parent
            forward = "right" if y == p.left else "left"
            if self.__get_color(x := getattr(p, forward)) == "red":
                x.color = "black"
                z = p
            else:
                if z == getattr(y, forward):
                    self.__rotate(y, self.__turn_around(forward))
                    z, y = y, z
                self.__rotate(p, forward)
            y.color = "black"
            p.color = "red"
        self.root.color = "black"

    def insert(self, z: TreeNode) -> None:
        super().insert(z)
        z.color = "red"
        self.__insert_fixup(z)

    def __delete_fixup(self, x):
        while x != self.root and x.color == "black":
            p = x.parent
            forward = "left" if x == p.left else "right"
            backward = self.__turn_around(forward)
            y = getattr(p, backward)
            if y.color == "red":
                y.color = "black"
                p.color = "red"
                self.__rotate(p, forward)
                y = getattr(p, backward)
            f = getattr(y, forward)
            b = getattr(y, backward)
            if self.__get_color(f) == "black" and self.__get_color(b) == "black":
                y.color = "red"
                x = p
            else:
                if self.__get_color(b) == "black":
                    f.color = "black"
                    y.color = "red"
                    self.__rotate(y, backward)
                    b = y
                    y = f
                y.color = p.color
                p.color = "black"
                b.color = "black"
                self.__rotate(p, forward)
                x = self.root
        x.color = "black"

    def delete(self, z: TreeNode) -> TreeNode:
        y = z if z.left is None or z.right is None else self.successor(z)
        y.color, z.color = z.color, y.color
        x = y.left or y.right
        if x is None:
            x = self.null
            x.parent = y
            y.right = x
        super().delete(z)
        if z.color == "black":
            self.__delete_fixup(x)
        if x == self.null:
            super().delete(x)


__all__ = ["TreeNode", "RBTree"]
