# Problem  : Maximum Depth of Binary Tree
# Difficulty: Easy
# Tags     : Tree, Depth-First Search, Breadth-First Search, Binary Tree
# URL      : https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Solved on: 2026-04-08 18:10
# ──────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if root==None: 
                return 0
            lh=solve(root.left)
            rh=solve(root.right)
            return 1+max(lh,rh)
        return solve(root)
