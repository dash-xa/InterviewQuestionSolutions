def verifyArray(A):
	i = 0
	while i < len(A):
		if not (0 <= A[i] < len(A)): return False
		j = A[i]
		if j != i and A[j] == j: return False
		A[i], A[j] = A[j], A[i]
		i += (i == A[i])
	return True
A = [0, 2, 3, 1]
print(verifyArray(A))
print("done")
# [2 2 2] -> [2 2 2] -> [2 2 2]
 # |            |        
# [2 2 2] -> 
# arr = [2, 1, 0] -> [0, 1, 2]

# arr[2] = 2
# 2 = arr[pos]
# arr[arr[pos]] = arr[pos]

# arr[0] = 2
# 0 = arr[2] = arr[arr[pos]]

# v = arr[pos]
# [2, 0, 1] -> [1, 0, 2]

# i = 0
# v = 2
# arr[2] = 2
# arr[0] = arr[2] = 1
# ==> [1, 0, 2] ==> [0, 1, 2]

# [0, 2, 1]




