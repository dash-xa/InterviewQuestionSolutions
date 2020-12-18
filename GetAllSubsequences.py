def getAllSubseq(A):
	N = len(A)
	if N == 0:
		return [[]]
	S = [[]] * N
	S[0] = [[], [A[0]]]
	for j in range(1, N):
		S[j] = S[j - 1][:]
		for lst in S[j - 1]:
			S[j].append(lst + [A[j]])
	return S[N - 1]

def getAllSubseqBetter(A):
	S = [[]]
	for j in range(len(A)):
		S.extend([lst + [A[j]] for lst in S[:]])
	return S
def generateSubseq(A):
	S = {()}
	for j in range(len(A)):
		for lst in S.copy():
			S.add(lst + (A[j], ) )
	return S
def longestCommonSubsequence(A, B):
	subseqA = generateSubseq(A)
	subseqB = generateSubseq(B)
	maxLength = 0
	for subseq in subseqA:
		if subseq in subseqB:
			maxLength = max(maxLength, len(subseq))
	return maxLength
# longestCommonSubsequence('abcde', 'ace')
assert longestCommonSubsequence('abcde', 'ace') == 3
assert longestCommonSubsequence('ace', 'ace') == 3
assert longestCommonSubsequence('abc', 'def') == 0
print(longestCommonSubsequence('ab', ''))
