# Problem: Given a BST,  and a reference to a Node x in the BST, 
#  find the Inorder Successor of the given node in the BST.

# Idea: inorder traversal
# Example:
#         2
#     1       3
#                 4
# inorderSuccessor(2, 3)
# Traverse bst in order. Once node equal to x has been reached, return next element in the traversal
# Question: what if x is already the max node? Return None
# Question: Can we have null value nodes? Assume yes
# Q: Can root be None? Assume no
# Q: Is our binary tree a bst? Assume yes
# Q: Are we guaranteed that x is in the bst? Assume yes
# Q: Are we guaranteed that an inorder successor exists? Assume yes

# Idea 1: generate array of sorted nodes. Search through it, and return node right after x. This has complexity O(n)
# Idea 2: We can achieve O(log n) complexity if we search for the item.
# There’s no point in recursing left if our node is less than x, and no point in recursing right if our 

# Given a BST,  and a reference to a Node x in the BST. Find the Inorder Successor of the given node in the BST.

'''
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
        self.key = k
'''
# returns the inorder successor of the Node x in BST (rooted at 'root')
def inorderSuccessor(node, x):
    if not node:
        return Node(-1)
    # if x >= current node, go right
    if x.data >= node.data: # guaranteed to find x
		return inorderSuccessor(node.right, x)
    # if x < current node, search for inorder successor
    if x.data < node.data:
        # want to be safe every time we recurse
        left = inorderSuccessor(node.left, x)
        if left.data == -1:
            return node
        return min(left, inorderSuccessor(node.left, x), key=lambda x: x.data)
