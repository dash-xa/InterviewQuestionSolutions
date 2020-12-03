# Q1. There are 2 arrays. Smaller is of size m and has m elements in sorted order. The bigger array is
# of size m+n, where there are only n elements in initial n positions in sorted order. So, last m
# positions are empty in the bigger array. Insert smaller array’s m elements in m + n array has all numbers in sorted order.

# Example : 
# Input Array    N[]={5, 9, 15, 20,,,,,, }  n=4
#                M[]={1, 3, 6, 8, 19, 35}  m=6
# Output array   N[]={1, 3, 5, 6, 8, 9, 15, 19, 20, 35}
# Hint : Refer this article.

# Q2. Given a binary tree with integer values, find the sub-path with the maximum value in it
# Each path must include at least one node

   
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

# Questions:
# 1) Can nodes have value None?
# 2) Can tree be empty?
# 3) Can nodes with None value have children?

#==============Solution==============================

# Commentary:
# Basically, there are 2 kinds of paths: a "closed one" and an open one.

# A closed path is one of: 
# 1) left path + node
# 2) right path + node
# 3) left path + right path + node
# 4) node
# Each time we make sure the best existing closed path is >= both these options

# An open path is one of:
# 1) Left path + node
# 2) right path + node
# 3) node
# 4) nothing (value of 0)
# For returning the best open path, we just take the max of these values

# We construct a method which writes the best closed path to the self.maxClosed field,
# and returns the best open path

class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val
#Q4
class MaxPathFinder:
	def __init__(self):
		self.maxClosed = -float('inf')

	def _getMaxPath(self, node):
		# Dealing with null value node. 
		# If node has null value then open path no longer an option
		if node.val is None:
			if node.left:
				self._getMaxPath(node.left)
			if node.right:
				self._getMaxPath(node.right)
			return -float('inf')

		left = 0 if node.left is None else self._getMaxPath(node.left)
		right = 0 if node.right is None else self._getMaxPath(node.right)

		# update max closed path variable
		self.maxClosed = max(self.maxClosed, node.val, max(left, right) + node.val, left + right + node.val)

		# return max open path
		maxOpenPath = max(node.val, max(left, right) + node.val)
		return maxOpenPath

	def getMaxPath(self, node):
		self.maxClosed = -float('inf')
		self._getMaxPath(node)
		return self.maxClosed

#================Tests===================
pathFinder = MaxPathFinder()
head = Node(-1)
head.right = Node(9)
head.right.left = Node(-6)
head.right.right = Node(3)
head.right.right.right = Node(-2)
print('max path is', pathFinder.getMaxPath(head))

h = Node(1)
h.left = Node(2)
h.right = Node(3)
print('max path is', pathFinder.getMaxPath(h))

d = Node(None)
d.right = Node(5)
print('max path is', pathFinder.getMaxPath(d))