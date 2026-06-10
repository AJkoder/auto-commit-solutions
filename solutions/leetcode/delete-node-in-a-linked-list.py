# Problem  : Delete Node in a Linked List
# Difficulty: Medium
# Tags     : Linked List
# URL      : https://leetcode.com/problems/delete-node-in-a-linked-list/
# Solved on: 2026-06-10 20:49
# ──────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next



        
