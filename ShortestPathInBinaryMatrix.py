# Questions, and things I missed:
# 	Edge cases:
# 		Can origin have a 1 on it (not be accessible?)
# 		Is path length include origin point? (ie. does path start at 1?)
# 		To solve this, work through an example and try to predict what the answer should be. 
# 		You MUST carefully work through an example before doing the problem

# Pseudocode:
# Idea: Run bfs. Adjacent nodes are those which are nonzero and not out of range
# toVisit = [] # queue of type (node, pathLength)
# add (origin, pathLength = 0) to toVisit queue
# pop (node, pathLength) from queue
# if node has been visited before, go to next iteration
# Mark node as visited
# Check if the node is bottom right corner. If so, return pathLength
# for every adjacent in range node: add (adjNode, pathLength + 1) to queue
# repeat while toVisit has nodes in it
# If loop has ended, means there is no path. Return -1

# Time complexity: O(n). Space complexity: O(n). 
# We look at adjacent nodes but only perform n checks
class Solution:
	def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
		if grid[0][0]:
			return -1
		toVisit = [((0, 0), 0)] # queue
		bottomRight = (len(grid) - 1,) * 2
		visited = set()
		while toVisit:
			node, pathLength = toVisit.pop(0)
			if node in visited:
				continue
			visited.add(node)
			if node == bottomRight:
				return pathLength
			row, col = node
			for r in [row - 1, row, row + 1]:
				for c in [col - 1, col, col + 1]:
					if 0 <= r <= bottomRight[0] and 0 <= c <= bottomRight[1] and not grid[r][c]: 
					toVisit.append(((r, c), pathLength + 1))
	return -1