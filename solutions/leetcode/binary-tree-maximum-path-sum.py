# Problem  : Binary Tree Maximum Path Sum
# Difficulty: Hard
# Tags     : Dynamic Programming, Tree, Depth-First Search, Binary Tree
# URL      : https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Solved on: 2026-04-09 00:15
# ──────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.mx = float("-inf")
        
        def solve(node):
            if node is None:
                return 0
            
            ls = max(0, solve(node.left))
            rs = max(0, solve(node.right))
            
            self.mx = max(self.mx, ls + rs + node.val)
            
            return node.val + max(ls, rs)
        
        solve(root)
        return self.mx
