# This problem sucks dick
# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# Example 4:
# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"

# Constraints:
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].

# Solution passed Leetcode
class Solution:
    def index(self, haystack, needle):
        for i in range(len(haystack)):
            if haystack[i] == needle:
                return i
        return float('inf')
    def firstDigit(self, s):
        minIndex = float('inf')
        minDigit = -1
        for d in range(9):
            i = self.index(s, str(d))
            if i < minIndex:
                minIndex = i
                minDigit = d
        return (minDigit, minIndex)
    def getCloseBracketIndex(self, s):
        depth = 0
        for i in range(len(s)):
            if s[i] == "[":
                depth += 1
            elif s[i] == "]":
                depth -= 1
            if depth == 0:
                return i
    def decodeString(self, s):
        digit, digitIndex = self.firstDigit(s)
        while digitIndex != float('inf'):
            openBracketIndex = s[digitIndex:].index("[") + digitIndex

            # find number at that point
            numRepeat = int(s[digitIndex : openBracketIndex])
            offset = digitIndex + len(str(numRepeat)) 
            before = s[:digitIndex]
            closeBracketIndex = self.getCloseBracketIndex(s[offset:]) + offset
            partToRepeat = s[openBracketIndex + 1 : closeBracketIndex] # assuming s valid
            after = s[closeBracketIndex + 1:]

            s = before + numRepeat * partToRepeat + after
            digit, digitIndex = self.firstDigit(s)
        return s
sol = Solution()
print(sol.decodeString("10[leetcode]"))