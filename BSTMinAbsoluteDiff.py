# Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

# MISSED: node.val could be None
# MISSED: used (if not node.val) implicit boolean comparison. Evaluated to true for nodes with value 0, when I only wanted it to evaluate to true for nodes with value None
# MISSED: self check

# Q: Can root be null? Assume no
# Q: Can tree have just 1 node? Assume no
# Q: Can tree have identical nodes? Assume yes
# Q: Can tree have null value nodes? Assume yes

# Examples: 
#           5
#    1             9
#        4

# Idea: We need to traverse entire tree
# Idea 1: For every node, traverse tree again, and get the minimum. This is a O(n^2) solution
# Idea 2: Traverse tree, collect nodes, sort them, get minimum difference. O(n log n)
# Idea 3, much better: Inorder traversal, O(n)	

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nodes = []
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.traverse(root) # fill nodes list via inorder traversal
        minDiff = float('inf')
        for i in range(1, len(self.nodes)):
            minDiff = min(minDiff, abs(self.nodes[i] - self.nodes[i - 1]))
        return minDiff
    
    def traverse(self, node: TreeNode) -> None:
        if not node:
            return
        self.traverse(node.left)
        if node.val is not None:
            self.nodes.append(node.val)
        self.traverse(node.right)

