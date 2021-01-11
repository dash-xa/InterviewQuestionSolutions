# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.

# Solution:
# Easy peasy. Just remember to set lo = mid + 1. 
class Solution:
    def searchIterative(self, nums: List[int], target: int) -> int:
        N = len(nums)
        lo, hi = 0, N - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                return mid
        return -1
    def searchRecursiveWay(self, nums, target):
        def searchRecursive(lo, hi):
            if lo > hi:
                return -1
            mid = (lo + hi) // 2
            m = nums[mid]
            if m < target:
                return searchRecursive(mid + 1, hi)
            elif m > target:
                return searchRecursive(lo, mid - 1)
            return mid
        N = len(nums)
        return searchRecursive(0, N - 1)