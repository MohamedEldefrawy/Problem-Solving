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
    max_distance = [0]

    def dfs(temp_root):
        if not temp_root:
            return -1
        left_height = dfs(temp_root.left)
        right_height = dfs(temp_root.right)
        max_distance[0] = max(max_distance[0], (2 + left_height + right_height))

        return 1 + max(left_height, right_height)

    dfs(root)
    return max_distance[0]


print(solve())
