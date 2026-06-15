# Problem  : Delete the Middle Node of a Linked List
# Difficulty: Medium
# Tags     : Linked List, Two Pointers
# URL      : https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# Solved on: 2026-06-15 21:47
# ──────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        slow=head
        fast=head
        if not head.next:
            return None

        while fast.next.next and fast.next.next.next:
            slow=slow.next
            fast=fast.next.next
        slow.next=slow.next.next

        return head

