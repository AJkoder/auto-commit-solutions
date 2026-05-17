# Problem  : Search in a Binary Search Tree
# Difficulty: Easy
# Tags     : Tree, Binary Search Tree, Binary Tree
# URL      : https://leetcode.com/problems/search-in-a-binary-search-tree/
# Solved on: 2026-05-17 13:42
# ──────────────────────────────────────────────────

class Solution:
    def searchBST(self, node: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if node is None:
            return None

        if node.val == val:
            return node

        if val < node.val:
            return self.searchBST(node.left, val)

        return self.searchBST(node.right, val)
