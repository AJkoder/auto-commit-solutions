# Problem  : Binary Tree Postorder Traversal
# Difficulty: Easy
# Tags     : Stack, Tree, Depth-First Search, Binary Tree
# URL      : https://leetcode.com/problems/binary-tree-postorder-traversal/
# Solved on: 2026-04-08 18:10
# ──────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def helper(root):
            if not root:
                return 
            helper(root.left)
            helper(root.right)
            res.append(root.val)
        helper(root)
        return res
