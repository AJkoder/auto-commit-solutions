# Problem  : Linked List Cycle
# Difficulty: Easy
# Tags     : Hash Table, Linked List, Two Pointers
# URL      : https://leetcode.com/problems/linked-list-cycle/
# Solved on: 2026-06-10 20:49
# ──────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
