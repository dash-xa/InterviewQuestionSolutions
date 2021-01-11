# [-10, -5, 1, 3]
# Find one magic index.
# output: 3

# Brute force gives O(n)

# Binary search idea:
# lo = 0
# hi = N - 1

# [-1, 1, 3, 7, 8]
# [-1, 10]
# [0]
# [-2, 4, 4, 4, 4, 5]
# [-2, 1, 1, 1, 1, 5]
def magicIndex(A):
	N = len(A)
	lo, hi = 0, N - 1
	while lo <= hi:
		mid = (lo + hi) // 2
		m = A[mid]
		if m < mid:
			lo = mid + 1
		elif m > mid:
			hi = mid
		else: # m == mid
			return mid if m == mid else -1
	return -1

def magicIndexNotDistinct(A):
	N = len(A)
	lo, hi = 0, N - 1
	while lo <= hi:
		mid = (lo + hi) // 2
		m = A[mid]
		if m < mid:
			lo = mid
			while lo > 0 and A[lo] == A[mid]:
				lo -= 1
		elif m > mid:
			hi = mid
			while hi < N - 1 and A[hi] == A[mid]:
				hi += 1
		else: # m == mid
			return mid if m == mid else -1
	return -1

print(magicIndex([-1]))
print(magicIndex([-1, 0, 2, 7, 8]))