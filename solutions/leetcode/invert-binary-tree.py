# Problem  : Invert Binary Tree
# Difficulty: Easy
# Tags     : Tree, Depth-First Search, Breadth-First Search, Binary Tree
# URL      : https://leetcode.com/problems/invert-binary-tree/
# Solved on: 2026-05-26 13:36
# ──────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):

            if not node:
                return None

            left = dfs(node.left)
            right = dfs(node.right)

            node.left = right
            node.right = left

            return node

        return dfs(root)
