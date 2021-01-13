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
# Optimization:
# Let S(w, h, d) be the max height of stack such that bottom has dimensions at most (w, h, d).
# O(WHDN), where N = len(boxes)
# W, H, D, are largest dimesnions

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
	# print(W, H, D)
	A = sorted(zip(H, W, D), key=lambda x: (x[1], x[2], x[0]), reverse=True)
	N = len(A)
	maxHeight = 0
	stackMap = [0] * N
	for i in range(N):
		h = create(A, i, stackMap)
		maxHeight = max(maxHeight, h)
	return maxHeight

#Your task is to complete this function
#Function should return an integer denoting the required answer
def maxHeight(W, H, D):
	N = len(W)
	A = sorted(zip(H, W, D), key=lambda x: (x[1], x[2], x[0]), reverse=True)
	S = [0] * (N)
	for n in range(N):
		hn, wn, dn = A[n]
		S[n] = hn
		for m in range(n):
			hm, wm, dm = A[m]
			if hm > hn and wm > wn and dm > dn:
				S[n] = max(S[n], S[m] + hn)
	return max(S)

import numpy as np
# np.random.seed()
for n in range(1000):
	X = 50
	print(np.random.randint(0, 100, 1000))

	widths = np.random.randint(0, 100, X)
	heights = np.random.randint(0, 100, X)
	depths = np.random.randint(0, 100, X)
	assert maxHeight(widths, heights, depths) == createStack(widths, heights, depths)

# A = [(1, 1, 1), (2, 2, 2), (3, 3, 3), (2, 2, 3), (6, 6, 3)]

# widths = [x[0] for x in A]
# heights = [x[1] for x in A]
# depths = [x[2] for x in A]
# N = 3

# print(maxHeight(widths, heights, depths))
# print(createStack(widths, heights, depths))