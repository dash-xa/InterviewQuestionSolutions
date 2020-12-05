# Problem Statement:
# A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

# Example
# Example 1:

# Input:
# [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
# Output:
# 6

# Explanation:
# The point `(0,2)` is an ideal meeting point, as the total travel distance of `2 + 2 + 2 = 6` is minimal. So return `6`.
# Example 2:

# Input:
# [[1,1,0,0,1],[1,0,1,0,0],[0,0,1,0,1]]
# Output:
# 14

# Solution 1:
# Time Complexity: O(n log n)
# Space complexity: O(n)
class Solution:
    """
    @param grid: a 2D grid
    @return: the minimize travel distance
    """
    def minTotalDistance(self, grid):
        xPos = []
        yPos = []
        R = len(grid)
        C = len(grid[0])
        numHouses = 0
        for row in range(R):
            for col in range(C):
                if grid[row][col]:
                    numHouses += 1
                    xPos.append(col)
                    yPos.append(row)
        if numHouses == 0:
            return 0
        xPos.sort()
        yPos.sort()
        midPoint = (xPos[numHouses // 2], yPos[numHouses // 2])
        xDist = sum(map(lambda x: abs(x - midPoint[0]), xPos))
        yDist = sum(map(lambda y: abs(y - midPoint[1]), yPos))
        return xDist + yDist

# Solution 2: O(NH), where H is the number of houses and N is the number of noders
#============= Ok so apparently this solution doesn't work. See above solution which works in O(n log n) time
def dist(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
def getBestMeetingSpot(grid):
	# assuming grid is not empty
	R = len(grid)
	C = len(grid[0])
	toVisit = [] # queue
	visitedBy = {} # dictionary st. visitedBy[coordinate] = set of houses which visited it
	houses = set() # set of all houses
	for row in range(R):
		for col in range(C):
			if grid[row][col]:
				toVisit.append(((row, col), (row, col)))
				houses.add((row, col))

	coords = (0, 0)
	while toVisit:
		coords, house = toVisit.pop(0)
		row, col = coords

# check if house already visited this location
		if house in visitedBy.get(coords, set()):
			continue
		
# visit location
		if coords in visitedBy:
			visitedBy[coords].add(house)
		else:
			visitedBy[coords] = set([house])

		# check if location has been visited by all houses
		if visitedBy[coords] == houses:
			break

		for pt in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
			if 0 <= pt[0] < R and 0 <= pt[1] < C:
				toVisit.append((pt, house))
	return sum(map(lambda house: dist(house, coords), houses))


# M = [ [1, 0, 1,], [0, 0, 0], [0, 1, 0]]
M2 = [[1, 0, 0, 0, 1], 
                [0, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0]]
M3 = [[1, 0, 1, 0, 1],
                     [0, 1, 0, 0, 0], 
                     [0, 1, 1, 0, 0]]
print(getBestMeetingSpot(M2))
print(getBestMeetingSpot(M3))


