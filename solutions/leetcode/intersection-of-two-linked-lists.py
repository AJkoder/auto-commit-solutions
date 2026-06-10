# Problem  : Intersection of Two Linked Lists
# Difficulty: Easy
# Tags     : Hash Table, Linked List, Two Pointers
# URL      : https://leetcode.com/problems/intersection-of-two-linked-lists/
# Solved on: 2026-06-10 20:49
# ──────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> Optional[ListNode]:
        p1=head1
        p2=head2

        while p1!=p2:
            p1=p1.next if p1 else head2
            p2=p2.next if p2 else head1
        return p1

        
