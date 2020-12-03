# Question: Rotate a matrix
# Short answer (LOL):
def rotateMatrixNumpy(M):
	return np.array(M).T
# Without NumPy:
# Questions: 
# 1) Can matrix be None? Assume yes
# 2) Is matrix square? Assume no
# 3) Which direction are we rotating in? Assume clockwise
# For CCW rotation just apply method 3 times!
def rotateRectMatrixClockwise(M):
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
assert rotateRectMatrixClockwise(M1) is None
M2 = [ [1, 2, 3, 3], [4, 5, 6, 6], [7, 8, 9, 9] ]
M2R = [ [7, 4, 1], [8, 5, 2], [9, 6, 3], [9, 6, 3] ]
print(rotateRectMatrixClockwise(M2))
assert rotateRectMatrixClockwise(M2) == M2R

# Question: Rotate square matrix IN PLACE without allocating new array
# Solution (passed Leetcode):
class Solution:
    def rotate(self, matrix):
        if matrix is None:
            return
        #We have oldMatrix[r][c] = newMatrix[c][R - 1 - r]
        N = len(matrix)
        for r in range(N):
            for c in range(r + 1, N):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for r in range(N):
            matrix[r] = matrix[r][::-1]