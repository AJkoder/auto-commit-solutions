# Problem  : Same Tree
# Difficulty: Easy
# Tags     : Tree, Depth-First Search, Breadth-First Search, Binary Tree
# URL      : https://leetcode.com/problems/same-tree/
# Solved on: 2026-05-27 12:45
# ──────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node1, node2):

            # both are empty
            if not node1 and not node2:
                return True

            # one is empty, other isn't
            if not node1 or not node2:
                return False

            # values different
            if node1.val != node2.val:
                return False

            # check left and right subtrees
            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)

            return left and right

        return dfs(p, q)
        
