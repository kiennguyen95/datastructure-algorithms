import sys
from enum import Enum


class Color(Enum):
    RED = 0
    BLACK = 1


class Node():
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = Color.RED


class RedBlackTree():
    def __init__(self):
        self.NIL = Node(0)
        self.NIL.color = Color.BLACK
        self.NIL.left = None
        self.NIL.right = None
        self.root = self.NIL


    def display(self):
        self._displayHelper(self.root, "", True)


    def _displayHelper(self, node, indent, last):
        if node != self.NIL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "R" if node.color == Color.RED else "B"
            print(str(node.data) + "(" + s_color + ")")
            self._displayHelper(node.left, indent, False)
            self._displayHelper(node.right, indent, True)


    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.NIL
        node.right = self.NIL
        node.color = Color.RED

        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = Color.BLACK
            return

        if node.parent.parent == None:
            return

        self._fixInsert(node)


    def _fixInsert(self, node):
        while node.parent.color == Color.RED:
            if node.parent == node.parent.parent.right:
                u = node.parent.parent.left
                if u.color == Color.RED:
                    u.color = Color.BLACK
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rightRotate(node)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._leftRotate(node.parent.parent)
            else:
                u = node.parent.parent.right

                if u.color == Color.RED:
                    u.color = Color.BLACK
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._leftRotate(node)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._rightRotate(node.parent.parent)
            if node == self.root:
                break
        self.root.color = Color.BLACK


    def delete(self, data):
        z = self.NIL
        node = self.root
        while node != self.NIL:
            if node.data == data:
                z = node

            if node.data <= data:
                node = node.right
            else:
                node = node.left

        if z == self.NIL:
            print("Couldn't find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self._transplant(z, z.right)
        elif (z.right == self.NIL):
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == Color.BLACK:
            self._fixDelete(x)


    def _fixDelete(self, node):
        while node != self.root and node.color == Color.BLACK:
            if node == node.parent.left:
                s = node.parent.right
                if s.color == Color.RED:
                    s.color = Color.BLACK
                    node.parent.color = Color.RED
                    self._leftRotate(node.parent)
                    s = node.parent.right

                if s.left.color == Color.BLACK and s.right.color == Color.BLACK:
                    s.color = Color.RED
                    node = node.parent
                else:
                    if s.right.color == Color.BLACK:
                        s.left.color = Color.BLACK
                        s.color = Color.RED
                        self._rightRotate(s)
                        s = node.parent.right

                    s.color = node.parent.color
                    node.parent.color = Color.BLACK
                    s.right.color = Color.BLACK
                    self._leftRotate(node.parent)
                    node = self.root
            else:
                s = node.parent.left
                if s.color == Color.RED:
                    s.color = Color.BLACK
                    node.parent.color = Color.RED
                    self._rightRotate(node.parent)
                    s = node.parent.left

                if s.left.color == Color.BLACK and s.right.color == Color.BLACK:
                    s.color = Color.RED
                    node = node.parent
                else:
                    if s.left.color == Color.BLACK:
                        s.right.color = Color.BLACK
                        s.color = Color.RED
                        self._leftRotate(s)
                        s = node.parent.left

                    s.color = node.parent.color
                    node.parent.color = Color.BLACK
                    s.left.color = Color.BLACK
                    self._rightRotate(node.parent)
                    node = self.root
        node.color = Color.BLACK


    def _transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent


    def _minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node


    def _maximum(self, node):
        while node.right != self.NIL:
            node = node.right
        return node


    def _leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y


    def _rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y


if __name__ == "__main__":
    bst = RedBlackTree()
    bst.insert(4)
    bst.insert(6)
    bst.insert(2)
    bst.insert(5)
    bst.insert(1)
    bst.insert(10)
    bst.insert(7)
    bst.insert(11)
    bst.insert(3)
    bst.insert(9)
    bst.insert(8)
    bst.delete(11)
    bst.display()