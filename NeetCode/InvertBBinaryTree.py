class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve():
    root = TreeNode()
    root.val = 1
    root.right = TreeNode()
    root.left = TreeNode()
    root.right = 2
    root.left = 3


def flip(root):
    if root:
        temp = root.left
        root.left = root.right
        root.right = temp
        flip(root.right)
        flip(root.left)
