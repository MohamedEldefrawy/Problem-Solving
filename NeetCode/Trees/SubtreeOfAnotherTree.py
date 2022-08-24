class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    root = TreeNode()
    root.val = 3
    root.right = TreeNode()
    root.left = TreeNode()
    root.right.val = 5
    root.left.val = 4
    root.left.left = TreeNode()
    root.left.right = TreeNode()
    root.left.left.val = 1
    root.left.right.val = 10

    sub_root = TreeNode()
    sub_root.val = 4
    sub_root.right = TreeNode()
    sub_root.left = TreeNode()
    sub_root.right.val = 10
    sub_root.left.val = 1

    def isSubtree(self, root, subRoot) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.dfs(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def dfs(self, s, q):
        if not s and not q:
            return True
        if s and q and s.val == q.val:
            return self.dfs(s.left, q.left) and self.dfs(s.right, q.right)
        return False

    def solve(self):
        return self.isSubtree(self.root, self.sub_root)


print(Solution().solve())
