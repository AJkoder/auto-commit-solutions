# Problem  : Median of Two Sorted Arrays
# Difficulty: Hard
# Tags     : Array, Binary Search, Divide and Conquer
# URL      : https://leetcode.com/problems/median-of-two-sorted-arrays/
# Solved on: 2026-06-22 14:24
# ──────────────────────────────────────────────────

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        arr = []
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1

        arr.extend(nums1[i:])
        arr.extend(nums2[j:])

        n = len(arr)

        if n % 2:
            return arr[n // 2]

        return (arr[n // 2 - 1] + arr[n // 2]) / 2
