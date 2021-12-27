import bisect

# Mistake: confused index with array value returned from binary search

"""
queries = [[GET, 1], [SET, 1], [GET, 1], [GET, 0]]
GET 1: bisect insort returns 0. this is equal to length of ones, so append -1
SET 1: ones = [1]
GET 1: Find index 0. Return ones[0]=1
GET 0: Find index 0. Return ones[0]=1
"""
"""
Ones will be an array of indices of max size Q
Time complexity to execute all queries is O(QlogQ), and space complexity is O(Q)
Each GET and SET operation is time complexity of O(logQ)
"""
def binarySearch(A, x):
	lo, hi = 0, len(A)-1
	while lo <= hi:
		mid = (lo + hi) // 2
		if A[mid] < x:
			lo = mid + 1
		elif A[mid] > x:
			hi = mid - 1
		else:
			return mid
	return lo
# arr = [1, 2]
# i = binarySearch(arr, 3)
# print(i)
# print(arr[i])


def answerQueries(queries):
	res, ones = [], []
	for qType, index in queries:
		if qType == 1:
			bisect.insort(ones, index)
		elif qType == 2:
			ceilIndex = bisect.bisect_left(ones, index)
			res.append(-1 if ceilIndex == len(ones) else ones[ceilIndex])
	return res

SET = 1
GET = 2
queries = [[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]]
# print(answerQueries(queries))

