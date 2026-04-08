# Problem  : Diameter of Binary Tree
# Difficulty: Easy
# Tags     : Tree, Depth-First Search, Binary Tree
# URL      : https://leetcode.com/problems/diameter-of-binary-tree/
# Solved on: 2026-04-08 18:10
# ──────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia=0
        def solve(root):
            nonlocal dia
            if root==None: 
                return 0
            lh=solve(root.left)
            rh=solve(root.right)
            dia=max(dia,lh+rh)
            return 1+max(lh,rh)
        solve(root)
        return dia
