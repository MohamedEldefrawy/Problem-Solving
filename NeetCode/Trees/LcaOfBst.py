class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    root = TreeNode()
    root.val = 6
    root.right = TreeNode()
    root.left = TreeNode()
    root.right.val = 8
    root.left.val = 2
    root.left.left = TreeNode()
    root.left.right = TreeNode()
    root.right.left = TreeNode()
    root.right.right = TreeNode()
    root.left.left.val = 0
    root.left.right.val = 4
    root.right.left.val = 7
    root.right.right.val = 9
    result = 0

    def LCA(self, root, p: TreeNode, q: TreeNode) -> bool:
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root

    def solve(self):
        return self.LCA(self.root, self.root.right, self.root.left)


print(Solution().solve().val)
