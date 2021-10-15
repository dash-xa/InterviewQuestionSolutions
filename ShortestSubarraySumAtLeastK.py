class Solution:
    def shortestSubarray(self, A: List[int], k: int) -> int:
        N = len(A)
        l = float('inf')
        S = 0
        p = [(0, -1)]
        for j in range(N):
            S += A[j]
            while p and p[-1][0] >= S:
                p.pop()
            while p and S - p[0][0] >= k:
                S_i, i = p.pop(0)
                l = min(l, j - i)
            p.append((S, j))
        return -1 if l == float('inf') else l

# Example: [5, -2, 7], k = 9
# 	j			S 		l 		p
# 	0			5		inf		[(0, -1), (5, 0)]
# 	1			3		inf		[(0, -1), (3, 1)]			S - k = -6, ie if S[i] <= -6
#	2			10				[(0, -1), (3, 1), (10, 4)]	S - k = 1, ie if S[i] <= 1. But we have i=-1 and S_i = 0, so add (2+1)=3 to q 
# This runs in O(n^2) worst case because worst case we will have the second for loop iterate all th way to the back of the array
# However, this can be improved by using binary search instead of a for loop on line 10. Namely, i = bisect_left(arr, i)
# TODO: find exactly how to implement this
# This would then be an O(nlogn) time solution

# Follow up: what if numbers couldn't be negative?