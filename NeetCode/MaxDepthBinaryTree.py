from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(self, root, depth, depth_set):
    if root:
        depth += 1
        if root.left or root.right:
            self.dfs(root.right, depth, depth_set)
            self.dfs(root.left, depth, depth_set)
        else:
            depth_set.add(depth)
            depth -= 1
    else:
        return 0
    return max(depth_set)


def dfs_2(root):
    if root:
        return 1 + max(dfs_2(root.right), dfs_2(root.left))
    else:
        return 0


def solve():
    depth = 0
    depth_set = set()
    root = TreeNode()
    root.val = 1
    root.right = TreeNode()
    root.left = TreeNode()
    root.right = 2
    root.left = 3

    # BFS Solution
    # level = 0
    # q = deque([root])
    # if root:
    #     while q:
    #         for i in range(len(q)):
    #             node = q.popleft()
    #             if node.left:
    #                 q.append(node.left)
    #             if node.right:
    #                 q.append(node.right)
    #         level += 1
    # else :
    #   return 0
    # return level

    # DFS Iterative
    # stack = [[root, 1]]
    # res = 0
    #
    # while stack:
    #     node, depth = stack.pop()
    #
    #     if node:
    #         res = max(res, depth)
    #         stack.append([node.left, depth + 1])
    #         stack.append([node.right, depth + 1])
    # return res
    return dfs(root, depth, depth_set)
