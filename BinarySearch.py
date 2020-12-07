# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.

# Solution:
# Easy peasy. Just remember to set lo = mid + 1. 
# You can remember this by the fact that mid always rounds down (bias towards lower)
# So to keep it even lo has to go up (bias towards higher). This avoids infinite loops
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target: lo = mid + 1
            elif nums[mid] > target: hi = mid
            else: return mid
        return lo if nums[lo] == target else -1
