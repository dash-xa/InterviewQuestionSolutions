# Question: Check that binary tree is complete
# Setup:
class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

# Both solutions passed on LeetCode
# A tree is complete if every node except last is filled
# And tree is far left as possible
# Complexity: O(n), where n is the number of nodes
# Solution essentially a BFS with null checking
# Both sol'ns are O(n) for space, O(n) for time

# Solution 1, using Python Queue:
# Supposed to give O(1) time, but in practice list implementation is often faster because
# list stuff is implemented in C and Queue is implemented in Python
from queue import Queue
def isTreeCompleteQueue(head):
	toVisit = Queue()
	toVisit.put(head)
	while not toVisit.empty():
		node = toVisit.get()
		if node is None:
			while not toVisit.empty():
				if not (toVisit.get() is None):
					return False
			return True
		toVisit.put(node.left)
		toVisit.put(node.right)

# Solution 2: Cleaner solution using Python list. Faster in practice 
# (amortized times are equal, but list implemented in C so faster)
# but queue gives better worst case performance
def isTreeCompleteList(head):
	toVisit = [head]
	while True:
		node = toVisit.pop(0)
		if node is None:
			return not any(toVisit)
		toVisit.extend([node.left, node.right])
	
# Tests
a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(6)
assert not isTreeCompleteQueue(a)
assert not isTreeCompleteList(a)