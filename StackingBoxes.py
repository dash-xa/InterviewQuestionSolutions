# input: List[[w, h, d]]
# output: int

# Question: are they in sorted order? Are w, h, w all strictly positive? Is each triplet unique? Does the box have to be strictly larger?
# Answer: Assume no. Assume yes. Assume no. Assume yes

# Ex
# input: [[1, 1, 1], [3, 3, 3], [1, 2, 3]]
# output: 4. Take 2nd box, then 1st box.

# Brute force recursive solution would have
# - time complexity O(n!)
# - space complexity O(1)

# Best conceivable runtime: O(n)
# Our algorithm runs in O(n^2) time, and O(n) space
# First, we sort the boxes. Let A denote this array
# Let S(n) denote max height of the stack such that A[n] is the topmost box
# Suppose we know S(i) for all i < n.
# Then, 
# S(n) =    max  { S(i) | box A[n] is larger than box A[i] } + height(A[n])
#          i < n
# In other words, to find S(n) we simply take the best stack which we can put
# A[n] on top of, and put A[n] on top of it
# We can now formulate a bottom-up DP solution:
def maxHeight(W, H, D):
	A = sorted(zip(H, W, D), reverse=True)
	N = len(A)

	S = [0] * N
	for n in range(N):
		hn, wn, dn = A[n]
		S[n] = hn
		for m in range(n):
			hm, wm, dm = A[m]
			if hm > hn and wm > wn and dm > dn:
				S[n] = max(S[n], S[m] + hn)
	return max(S) if N > 0 else 0

# Here's the book's solution:
def create(A, bottomIndex, stackMap):
	N = len(A)
	if bottomIndex < N and stackMap[bottomIndex] > 0:
		return stackMap[bottomIndex]
	bottom = A[bottomIndex]
	maxHeight = 0
	for i in range(bottomIndex + 1, N):
		hi, wi, di = A[i]
		hbot, wbot, dbot = bottom
		if hi < hbot and wi < wbot and di < dbot:
			h = create(A, i, stackMap)
			maxHeight = max(h, maxHeight)
	maxHeight += bottom[0]
	stackMap[bottomIndex] = maxHeight
	return maxHeight

def createStack(W, H, D):
	A = sorted(zip(H, W, D), key=lambda x: (x[1], x[2], x[0]), reverse=True)
	N = len(A)
	maxHeight = 0
	stackMap = [0] * N
	for i in range(N):
		h = create(A, i, stackMap)
		maxHeight = max(maxHeight, h)
	return maxHeight

# Here we test that they are the same
import numpy as np
for n in range(1000):
	X = 50

	widths = np.random.randint(0, 100, X)
	heights = np.random.randint(0, 100, X)
	depths = np.random.randint(0, 100, X)

	assert maxHeight(widths, heights, depths) == createStack(widths, heights, depths)
