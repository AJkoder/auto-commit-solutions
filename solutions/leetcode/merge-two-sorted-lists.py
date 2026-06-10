# Problem  : Merge Two Sorted Lists
# Difficulty: Easy
# Tags     : Linked List, Recursion
# URL      : https://leetcode.com/problems/merge-two-sorted-lists/
# Solved on: 2026-06-10 20:49
# ──────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        if not list1:
            return list2
        if not list2:
            return list1

        while list1 and list2:

            if list1.val<list2.val:
                tail.next = list1
                list1=list1.next

            else:
                tail.next = list2
                list2=list2.next

            tail = tail.next
        if list1:
            tail.next=list1
        if list2:
            tail.next=list2
        return dummy.next

