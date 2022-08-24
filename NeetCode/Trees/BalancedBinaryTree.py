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
    root.right.val = 2
    root.left.val = 3
    # root.right.right = TreeNode()
    # root.right.right.val = 10
    result = []
    print(dfs(root))


def dfs(root):
    if root:
        left = dfs(root.left)
        right = dfs(root.right)
        balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
    else:
        return [True, 0]
    return [balanced, 1 + max(left[1], right[1])]


solve()
