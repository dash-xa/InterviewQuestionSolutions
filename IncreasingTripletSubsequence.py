# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

# Solution: 1 pass, O(N) time, O(1) space. Essentially dynamic programming
class Solution:
    def increasingTriplet(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        a = A[0]
        b = p = float('inf')
        for n in A[1:]:
            if n > b:
                return True
            elif a < n < b:
                b = n
            elif n < p:
                p = n
            elif p < n <= a:
                a = p
                b = n
                p = float('inf')
        return False