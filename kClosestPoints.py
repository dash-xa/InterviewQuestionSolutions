# First, there's the most basic solution: sort data by distance, and splice list to get first k values. 
# This is O(nlogn) in time and O(n) in space:
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
	return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k]

# We can further reduce time complexity to O(nlogk) and space complexity to O(k) by using a heap.
# The idea here is to have a max heap containing the k smallest values.
# We iterate through the array and every time we encounter an element smaller than our heap's maximum, 
#	we pop the maximum and push that element into the heap. 
# By the end of our iteration our heap will contain the k smallest items:
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
	heap = [] # minHeap using key=-(distance from origin). heapq doesn't allow maxHeap :(
	for (x, y) in points:
		dist = x**2 + y**2
		if len(heap) < k:
			heapq.heappush(heap, (-dist, x, y))
		elif dist < -heap[0][0]:
			heapq.heappushpop(heap, (-dist, x, y))
	return [(x, y) for (_, x, y) in heap]