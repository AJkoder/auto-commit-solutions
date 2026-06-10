# Problem  : Remove Nth Node From End of List
# Difficulty: Medium
# Tags     : Linked List, Two Pointers
# URL      : https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Solved on: 2026-06-10 20:49
# ──────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=head
        fast=head

        if not head.next:
            return None

        for i in range (n):
            fast=fast.next
        
        if fast==None:
            return head.next
        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next

        return head

        
