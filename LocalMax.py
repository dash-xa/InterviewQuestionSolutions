# Question: Find Local maxx in array

#================Solution===============
# Time complexity: O(n), Space: O(n)
def local_max(arr):
	local_maxes  = []
	for i in range(1, len(arr) - 1):
		if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
			return arr[i]
# Test
Arr = [1, 3, 5, 4, 7, 10, 6]
assert local_max(Arr) in [5, 10]
