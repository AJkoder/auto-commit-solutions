# Problem  : Reverse Linked List
# Difficulty: Easy
# Tags     : Linked List, Recursion
# URL      : https://leetcode.com/problems/reverse-linked-list/
# Solved on: 2026-06-10 20:49
# ──────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        nxt=None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev

