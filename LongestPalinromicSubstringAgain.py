class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Ex: babad
        # Output: bab or aba
        
        # Brute force: generate substrings of all length, and check if they are palindromes
        # Let N = len(s)
        # For a fixed ending point there are N substrings, and there are N endpoints total.
        # Therefore there are N^2 total substrings
        # To check if one is a palindrome would take O(N). 
        # Therefore our algorithm would run in O(N^3)
        
        # Can we do better?
        
        # Example: "cbbdadbzz"
        # Output: dbadb
        # "abcb"
        
        # Cases:
        # 1) first != last: 
            # return best of f(without first), f(without last)
        # 2) first = last:
        #     return best of f(without first), f(without last),
        #                    2 + 
        def f(A, i, j):
            if i == j:
                return A[i]
            if i > j:
                return ''
            if memo[i][j] != '':
                return memo[i][j]
            if A[i] == A[j]:
                withoutBoth = f(A, i + 1, j - 1)
                print(withoutBoth, i, j)
                if len(withoutBoth) + 1 == j - i:
                    memo[i][j] = A[i] + withoutBoth + A[j] 

                    return memo[i][j]
            withoutFirst = f(A, i + 1, j)
            withoutLast = f(A, i, j - 1)
            if len(withoutFirst) > len(withoutLast):
                memo[i][j] = withoutFirst
            else:
                memo[i][j] = withoutLast
            return memo[i][j]
        N = len(s)
        memo = [[''] * N for i in range(N)]
        ans = f(s, 0, N - 1)
        # print(memo)
        return ans
        
        
sol = Solution()
print(sol.longestPalindrome(""))
            
            
            
        