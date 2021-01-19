class TreeNode():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preOrderTraversalRecursive(root: TreeNode):
    res = []
    if root:
        res.append(root.data)
        res += preOrderTraversalRecursive(root.left)
        res += preOrderTraversalRecursive(root.right)
    return res


def preOrderTraversalIterative(root: TreeNode):
    if not root:
        return []

    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


def inOrderTraversalRecursive(root: TreeNode):
    res = []
    if root:
        res += inOrderTraversalRecursive(root.left)
        res.append(root.data)
        res += inOrderTraversalRecursive(root.right)
    return res


def inOrderTraversalIterative(root: TreeNode):
    if not root:
        return []

    res = []
    stack = []
    current = root
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            node = stack.pop()
            res.append(node.data)
            if node.right:
                current = node.right
    return res


def postOrderTraversalRecursive(root: TreeNode):
    res = []
    if root:
        res += postOrderTraversalRecursive(root.left)
        res += postOrderTraversalRecursive(root.right)
        res.append(root.data)
    return res


def postOrderTraversalIterative(root: TreeNode):
    if not root:
        return []

    res = []
    stack = [root, root]
    while stack:
        current = stack.pop()
        if stack and stack[-1] is current:
            if current.right:
                stack.append(current.right)
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
                stack.append(current.left)
        else:
            res.append(current.data)

    return res


import unittest


class TestTreeTraversals(unittest.TestCase):

    tree: TreeNode

    def setUp(self):
        root = TreeNode(8)
        root.left = TreeNode(3)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(6)
        root.left.right.left = TreeNode(4)
        root.left.right.right = TreeNode(7)
        root.right = TreeNode(10)
        root.right.right = TreeNode(14)
        root.right.right.left = TreeNode(13)
        self.tree = root


    def testPreOrderTraversal(self):
        self.assertEqual(preOrderTraversalRecursive(self.tree), [8, 3, 1, 6, 4, 7, 10, 14, 13])
        self.assertEqual(preOrderTraversalIterative(self.tree), [8, 3, 1, 6, 4, 7, 10, 14, 13])


    def testInOrderTraversal(self):
        self.assertEqual(inOrderTraversalRecursive(self.tree), [1, 3, 4, 6, 7, 8, 10, 13, 14])
        self.assertEqual(inOrderTraversalIterative(self.tree), [1, 3, 4, 6, 7, 8, 10, 13, 14])


    def testPostOrderTraversal(self):
        self.assertEqual(postOrderTraversalRecursive(self.tree), [1, 4, 7, 6, 3, 13, 14, 10, 8])
        self.assertEqual(postOrderTraversalIterative(self.tree), [1, 4, 7, 6, 3, 13, 14, 10, 8])


if __name__ == '__main__':
    unittest.main(verbosity=2)