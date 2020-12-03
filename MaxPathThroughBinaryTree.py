# Q1. There are 2 arrays. Smaller is of size m and has m elements in sorted order. The bigger array is
# of size m+n, where there are only n elements in initial n positions in sorted order. So, last m
# positions are empty in the bigger array. Insert smaller array’s m elements in m + n array has all numbers in sorted order.

# Example : 
# Input Array    N[]={5, 9, 15, 20,,,,,, }  n=4
#                M[]={1, 3, 6, 8, 19, 35}  m=6
# Output array   N[]={1, 3, 5, 6, 8, 9, 15, 19, 20, 35}
# Hint : Refer this article.

# Q2. Given a binary tree with integer values, find the sub-path with the maximum value in it

   
# Example : 
#        1
#      /   \ 
#     2      3
#   /   \  /   \
#  4     5 6    7

# Output : Max path is 5, 2, 1, 3, 7
# Explanation : 5+2+1+3+7=18 is the maximum value that can spanned.

#       -100
#      /     \
#     2        3
#    /  \     /  \
#   4    5   6    7

# Output : Max path is 6, 3, 7
# Explanation : 6+3+7=16 is the maximum value that can spanned.

#==============Solution==============================

# Commentary:
# Basically, there are 2 kinds of paths: a "closed one" and an open one.
# A closed path includes the node and both left and right subpaths, 
# but not any parent nodes
# An open path includes the node and either the left or the right subpath, and 
# can include the parent node
# We also need to consider the cases where we don't include either the right
# nor the left paths, and consider only the node.
# The node can be both a closed and an open path. Here are our cases:
# 1) A "closed path" (include node, left and right trees)
# 2) A "closed path" with only the node
# 3) An "open path", which includes either L or R + node
# 4) An "open path" with only the node

class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val
#Q4
class MaxPathFinder:
	def __init__(self):
		self.maxClosed = 0
	def _getMaxPath(self, node):
		if not node:
			return 0
		left = self._getMaxPath(node.left)
		right = self._getMaxPath(node.right)
		# update max closed path variable
		self.maxClosed = max(self.maxClosed, left + right + node.val, node.val) # notice how node is both in closed and open path terms
		# return max open path
		return max(node.val, max(left, right) + node.val)
	def getMaxPath(self, node):
		self.maxClosed = 0
		return max(self._getMaxPath(node), self.maxClosed)

#================Tests===================
pathFinder = MaxPathFinder()
head = Node(-100)

n2 = Node(2)
head.left = n2
n4 = Node(4)
n2.left = n4
n5 = Node(5)
n2.right = n5
n3 = Node(3)

head.right = n3
n6 = Node(6)
n3.left = n6
n7 = Node(7)
n3.right = n7

print(pathFinder.getMaxPath(head))

xhead = Node(1)
xhead.left = Node(2)
xhead.right = Node(3)
xhead.left.left = Node(4)
xhead.left.right = Node(5)
xhead.right.left = Node(6)
xhead.right.right = Node(7)
print('max path', pathFinder.getMaxPath(xhead))

xhead = Node(1)
xhead.left = Node(-2)
xhead.right = Node(-3)
xhead.left.left = Node(-4)
xhead.left.right = Node(-5)
xhead.right.left = Node(6)
xhead.right.right = Node(-7)
print('max path', pathFinder.getMaxPath(xhead))