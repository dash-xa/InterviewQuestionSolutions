# Idea: same as stacking boxes I, but with some modifications
# First, we generate all possible combinations of boxes
from itertools import permutations
def maxHeight(H, W, D):
	# Generate all possible combinations of boxes
	A = []
	for h, w, d in zip(H, W, D):
		A.extend(permutations([h, w, d]))
	A.sort(reverse=True)

	N = len(A)
	S = [0] * N
	for n in range(N):
		wn, dn, hn = A[n]
		S[n] = hn
		for m in range(n):
			wm, dm, hm = A[m]
			# if we can put this box atop another, do so
			if wm > wn and dm > dn: 
				S[n] = max(S[n], S[m] + hn)
	return max(S) if N > 0 else 0

h = [4,1,4,10]
w = [6,2,5,12]
d = [7,3,6,32]
# h = [1,4,3]
# w = [2,5,4]
# d = [3,6,1]
print(maxHeight(h, w, d))