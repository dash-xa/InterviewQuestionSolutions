# Question: Rotate a matrix
# Short answer (LOL):
def rotateMatrixNumpy(M):
	return np.array(M).T
# Without NumPy:
# Questions: 
# 1) Can matrix be None? Assume yes
# 2) Is matrix square? Assume no
# 3) Which direction are we rotating in? Assume clockwise
def rotateSquareMatrixClockwise(M):
	if M is None:
		return None
	R = len(M)
	C = len(M[0])
	rotatedMatrix = [ [0] * R for i in range(C)]
	for r in range(R):
		for c in range(C):
			rotatedMatrix[c][-r - 1] = M[r][c]
	return rotatedMatrix

# Tests
M1 = None
assert rotateSquareMatrixClockwise(M1) is None
M2 = [ [1, 2, 3, 3], [4, 5, 6, 6], [7, 8, 9, 9] ]
M2R = [ [7, 4, 1], [8, 5, 2], [9, 6, 3], [9, 6, 3] ]
print(rotateSquareMatrixClockwise(M2))
assert rotateSquareMatrixClockwise(M2) == M2R