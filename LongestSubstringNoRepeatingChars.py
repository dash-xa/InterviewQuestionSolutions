
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        if N == 0:
            return 0
        start = 0
        size = 1
        maxSize = 0
        chars = set()
        while start + size - 1 < N:
            lastIndex = start + size - 1
            while size > 0 and s[lastIndex] in chars:
                chars.remove(s[start])
                start += 1
                size -= 1
                lastIndex = start + size - 1
            maxSize = max(maxSize, size)
            chars.add(s[lastIndex])
            size += 1
        return maxSize

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
