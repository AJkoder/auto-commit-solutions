# Problem  : Balanced Binary Tree
# Difficulty: Easy
# Tags     : Tree, Depth-First Search, Binary Tree
# URL      : https://leetcode.com/problems/balanced-binary-tree/
# Solved on: 2026-04-08 17:49
# ──────────────────────────────────────────────────

class Solution:
    def solve(self, root):
        if root is None:
            return 0
        
        lh = self.solve(root.left)
        if lh == -1:
            return -1
        
        rh = self.solve(root.right)
        if rh == -1:
            return -1
        
        if abs(lh - rh) > 1:
            return -1
        
        return 1 + max(lh, rh)

    def isBalanced(self, root):
        return self.solve(root) != -1
