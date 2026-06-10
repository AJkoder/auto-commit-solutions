# Problem  : Add Two Numbers
# Difficulty: Medium
# Tags     : Linked List, Math, Recursion
# URL      : https://leetcode.com/problems/add-two-numbers/
# Solved on: 2026-06-10 20:49
# ──────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while l1 or l2 or carry:

            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            total = a+b+carry

            carry = total//10
            digit = total%10

            tail.next = ListNode(digit)

            tail = tail.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next



