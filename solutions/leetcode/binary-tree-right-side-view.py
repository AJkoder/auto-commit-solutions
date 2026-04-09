# Problem  : Binary Tree Right Side View
# Difficulty: Medium
# Tags     : Tree, Depth-First Search, Breadth-First Search, Binary Tree
# URL      : https://leetcode.com/problems/binary-tree-right-side-view/
# Solved on: 2026-04-09 15:57
# ──────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def rpo(node,lvl,ans):
            if node is None:
                return
            if len(ans)==lvl:  #means it is the first element from right
                ans.append(node.val)
            if node.right:
                rpo(node.right,lvl+1,ans)
            if node.left:
                rpo(node.left,lvl+1,ans)
        ans=[]
        rpo(root,0,ans)
        return ans
            

