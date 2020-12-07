# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
# The order of output does not matter.

# Example 1:
# Input:
# s: "cbaebabacd" p: "abc"
# Output:
# [0, 6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Example 2:
# Input:
# s: "abab" p: "ab"
# Output:
# [0, 1, 2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

# Solution, O(n)
# Sliding window method works for everything string related!!
# If you're hashing strings you can use dict, 
# BUT be sure to mention that an int array with ASCII codes would be faster
class Solution:
    def hash(self, s):
        S = len(s)
        occ = [0]  * 26
        for char in s:
            occ[ord(char) - ord('a')] += 1
        return occ
    def findAnagrams(self, s, p):
        S, P = len(s), len(p)
        indices = [] # could use LinkedList for O(1) insertion
        phash = self.hash(p)
        h = self.hash(s[:P])
        for i in range(S - P + 1):
            j = i + P
            if h == phash:
                indices.append(i)
            if i < S - P:
                h[ord(s[i]) - ord('a')] -= 1
                h[ord(s[j]) - ord('a')] += 1
        return indices
sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc"))