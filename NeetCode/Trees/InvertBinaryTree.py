class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve():
    depth = 0
    depth_set = set()
    root = TreeNode()
    root.val = 3
    root.right = TreeNode()
    root.left = TreeNode()
    root.right.val = 20
    root.left.val = 9
    root.right.right = TreeNode()
    root.right.left = TreeNode()
    root.right.right.val = 15
    root.right.left.val = 7
    root.left.right = None
    root.left.left = None

    return traverse(root, depth, depth_set)


def traverse(root, depth, depth_set):
    if root:
        depth += 1
        if root.left or root.right:
            traverse(root.right, depth, depth_set)
            traverse(root.left, depth, depth_set)
        else:
            depth_set.add(depth)
            depth -= 1

    else:
        return 0
    return max(depth_set)


print(solve())
