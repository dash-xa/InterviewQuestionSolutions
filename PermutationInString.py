# Tips: work through examples, ESPECIALLY if there are fancy index operations
class Solution:
    def checkInclusion(self, s: str, b: str) -> bool:
        def count(w):
            occ = [0] * 26
            for char in w:
                occ[ord(char) - ord('a')] += 1
            return occ
        
        if len(s) > len(b) or s == '':
            return False
        S, B = len(s), len(b)
        occ = count(b[:S])
        s_occ = count(s)
        for i in range(B - S + 1):
            print(i, B - S)
            print(i + S)
            if i > 0:
                occ[ord(b[i - 1]) - ord('a')] -= 1
                occ[ord(b[i + (S - 1)]) - ord('a')] += 1
            if occ == s_occ:
                return True
        return False
s = "adc"
b = "dcda"
sol = Solution()
print(sol.checkInclusion(s, b))