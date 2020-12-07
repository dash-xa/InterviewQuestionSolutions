class Solution:
    # "abcadfsw"
#     i   j   maxSize
#     0   1   0
#     0   2   0
#     0   3   3
#     1   3   3
#     1   4   3
#     1   5   3
#     1   6   3
#     1   7   3
#     1   8   3
    
    # "abcabcbb"
    # i   j   s[j] chars
    # 0   1   b
    # 0   2   c    a
    # 0   3   a    ab
    # 1   4   a   
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        if N == 0:
            return 0
        i, j = 0, 0
        maxSize = 0
        chars = set()
        while j < N:
            print(i, j)
            if s[j] in chars:
                if s[i] in chars:
                    chars.remove(s[i])
                i += 1
            else: # advance
                maxSize = max(maxSize, j - i + 1)
                chars.add(s[j])
                j += 1
        return max(maxSize, N - i)
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))