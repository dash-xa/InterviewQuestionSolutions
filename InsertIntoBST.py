#MISTAKE: forgot to put node.left and node.right in recursive calls
#TIP: When making recursive calls, always make sure you make them with the right parameters!! Avoid stack overflow infinite recursion

# Write a program to insert node into binary tree
# Q: Is it a binary search tree? Assume yes
# Q: Can the number exist in the binary tree already? Assume No
# Q: Can the binary tree be null? Assume yes
# Q: Can the binary tree have equal values? Assume no
# Q: What are we returning? Assume the root

#       2
#    1    3
# Insert 2.5
# Result
#       2
#    1    2.5 
# 	     3

# Insert 3.5
# Result 
# 	    2
#    1     3
# 	         3.5
# Pseudocode. Idea: search for node in tree. If you get to a point where you can search no further (node has no kids), then place node there and make current one a child
# Assume node has val, left, right. Left, right are children nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, node: TreeNode, val: int) -> TreeNode:
        # deal with null tree input
        if not node:
            return TreeNode(val)
        if val < node.val:
            # check if there’s space in left
            if node.left:
                node.left = self.insertIntoBST(node.left, val)
            else:
                node.left = TreeNode(val)
        else: # val > node.val
            # check if there’s space in right
            if node.right:
                node.right = self.insertIntoBST(node.right, val)
            else:
                node.right = TreeNode(val)
        return node