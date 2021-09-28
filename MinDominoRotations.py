# Idea: loop through each possible value and see if we can count enough of it in the array
# By "enough", we mean that #top + #bottom + #both == N
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        topCount = [0 for digit in range(7)]
        bottomCount = [0 for digit in range(7)]
        sameCount = [0 for digit in range(7)]
        N = len(tops)
        for i in range(N):
            if tops[i] == bottoms[i]:
                sameCount[tops[i]] += 1
            else:
                topCount[tops[i]] += 1
                bottomCount[bottoms[i]] += 1
        minRotationsNeeded = float('inf')
        for digit in range(1, 7):
            if topCount[digit] + bottomCount[digit] + sameCount[digit] == N:
                minRotationsNeeded = min(minRotationsNeeded, topCount[digit], bottomCount[digit])
        return -1 if minRotationsNeeded == float('inf') else minRotationsNeeded     