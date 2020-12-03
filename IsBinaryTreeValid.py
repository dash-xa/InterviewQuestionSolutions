# Question: Check if binary tree is valid
#===========Solution============
class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
def isBstValid(node):
	if node is None:
		return True
	isCurrentValid = ((node.left is None) or (node.left.val <= node.val)) and ((node.right is None) or (node.right.val >= node.val))
	return isCurrentValid and isBstValid(node.left) and isBstValid(node.right)

#==============Tests==============
head = Node(3)
head.left  = Node(4)
head.right = Node(5)
assert not isBstValid(head)
head.left = Node(1)
assert isBstValid(head)
