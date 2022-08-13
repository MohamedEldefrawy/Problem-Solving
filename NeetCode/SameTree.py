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

    root2 = TreeNode()
    root2.val = 1
    root2.right = TreeNode()
    root2.left = TreeNode()
    root2.right.val = 2
    root2.left.val = 5

    same = False

    def dfs(first_root, second_root):
        if first_root and second_root:
            if first_root.val != second_root.val:
                return False
            else:
                same = dfs(first_root.right, second_root.right)
                if same:
                    same = dfs(first_root.left, second_root.left)
                else:
                    return False
        elif first_root == second_root:
            return True
        else:
            return False
        return same

    return dfs(root, root2)


result = solve()
print(result)
