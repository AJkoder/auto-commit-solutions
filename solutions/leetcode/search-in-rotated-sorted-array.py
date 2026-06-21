# Problem  : Search in Rotated Sorted Array
# Difficulty: Medium
# Tags     : Array, Binary Search
# URL      : https://leetcode.com/problems/search-in-rotated-sorted-array/
# Solved on: 2026-06-21 20:09
# ──────────────────────────────────────────────────

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)

        # Find pivot (smallest element index)
        low = 0
        high = n - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        pivot = low

        # Decide which side to search
        if nums[pivot] <= target <= nums[n - 1]:
            low = pivot
            high = n - 1
        else:
            low = 0
            high = pivot - 1

        # Normal Binary Search
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return -1
