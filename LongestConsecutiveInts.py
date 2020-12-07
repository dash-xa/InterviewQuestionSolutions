# Question:
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# Follow up: Could you implement the O(n) solution? 

# Solution, O(n):
# question: Can I modify the array?
class Solution:
    def longestConsecutive(self, A):
        S = set(A)
        maxLength = 0
        for n in S:
            if n - 1 not in S:
                length = 0
                while n in S:
                    length += 1
                    n += 1
                maxLength = max(maxLength, length)
        return maxLength
        