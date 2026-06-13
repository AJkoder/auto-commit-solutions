# Problem  : Linked List Cycle II
# Difficulty: Medium
# Tags     : Hash Table, Linked List, Two Pointers
# URL      : https://leetcode.com/problems/linked-list-cycle-ii/
# Solved on: 2026-06-13 21:47
# ──────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr=head
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        if not fast or not fast.next:
            return None
        while ptr!=slow:
            ptr=ptr.next
            slow=slow.next
        return slow
