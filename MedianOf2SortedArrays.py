

# O(n):
class Solution:
    def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:
        merged = []
        n1 = len(arr1)
        n2 = len(arr2)
        N = n1 + n2
        p1 = 0
        p2 = 0
        while p1 + p2 < N:
            if p1 == n1:
                merged.append(arr2[p2])
                p2 += 1
            elif p2 == n2:
                merged.append(arr1[p1])
                p1 += 1
            elif arr1[p1] < arr2[p2]:
                merged.append(arr1[p1])
                p1 += 1
            else:
                merged.append(arr2[p2])
                p2 += 1
        if N % 2 == 0:
            return (merged[(N - 1) // 2] + merged[N // 2]) / 2
        return merged[(N - 1) // 2]