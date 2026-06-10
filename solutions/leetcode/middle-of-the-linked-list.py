# Problem  : Middle of the Linked List
# Difficulty: Easy
# Tags     : Linked List, Two Pointers
# URL      : https://leetcode.com/problems/middle-of-the-linked-list/
# Solved on: 2026-06-10 20:49
# ──────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
