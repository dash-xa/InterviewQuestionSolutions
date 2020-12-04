# Question:
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# Follow up: Could you implement the O(n) solution? 

# Solution, O(n):
# This shit took me so long
class Solution:
    def longestConsecutive(self, A):
        L = 0
        S = set(A)
        for x in S:
            if x - 1 in S: continue
            l = 0
            while x in S:
                l += 1
                x += 1
            L = max(L, l)
        return L
        