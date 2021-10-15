# Given an integer array A, return the number of subarrays that sum to at most k
# Ex: [1, 2, 5, 3], k = 5
# [1], [1, 2], [2], [5], [3]
# Output: 5

# Questions
# Can numbers be negative? Assume yes. Can address no in a follow up

# Brute force: check every subarray using two pointers. This would be O(n^2)
# Can we optimize? I've done a problem where you can get subarray sum k. 
# If k is small we could make an O(k) algorithm which check every k value. But for large k this is bad

# But we can still use prefix sums. The idea is we keep track of running sums array. 
# Say we count using j. Then we want all i < j such that S[j] - S[i] <= k, so S[i] >= S[j] - k.

# One approach would be to keep (prefix sum, index) values in sorted array. Then at every j we binary search for (S[j]-k).
 # We add it and all values greater than it to our count variable. This would be O(nlogn) time.

# Working through an example:
# [4, -4, 3], k = 3
# Ans: [4, -4], [-4], [-4, 3], [3], [4, -4, 3]
# 		==> 5
# 	j			count	S		sums						
#	0			0		4	(0, -1), 
# 	1			0 		0	(0, -1), (4, 0)
# 	2					
							# (0, -1), (4, 0), (0, 1)
# Iteration 0: S = 4, we binary search for 4-3 = 1. We get z=1. len(sums)==(j+1). Right now j+1=1. We add (j+1)-z==0 to count
# j=1: S=0, we binary search for 0-3==-3 and get z=0. len(sums)=2 right now, so there are 2 items we can use. So, count += (j+1)-1=2
# j=2: S=3, we binary search for 3-3==0 and get z=0 (we want to use bisect_left), so there are 3 items we can use. So count += (j+1)-1=3

from bisect import insort, bisect_left
def atMost(A, k):
	N = len(A)
	sums = [0] # null case
	S = count = 0
	for j in range(N):
		S += A[j]
		z = bisect_left(sums, S - k) # TODO: make sure this returns the index OF the first occurrence, NOT the one before
		count += (j+1) - z
		insort(sums, S)
	return count

# Implementing binary search
def binarySearch(A, x):
	lo, hi = 0, len(A) - 1
	while lo <= hi:
		mid = (lo + hi) // 2
		if x > A[mid]:
			lo = mid + 1
		elif x < A[mid]:
			hi = mid - 1
		else:
			return mid
	return -1

import bisect