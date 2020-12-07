# Given a complete binary tree, count the number of nodes.

# Note:
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Example:
# Input: 
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
# Output: 6

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, node):
        return 0 if not node else 1 + self.depth(node.left)
    def __init__(self):
        self.nodePosition = 0
        self.treeDepth = 0
        
    def countNodes(self, node):
        if not node:
            return 0
        self.treeDepth = self.depth(node)
        self._countNodes(node)
        numNodes = 0
        for d in range(self.treeDepth - 1):
            numNodes += 2 ** d
        numNodes += (self.nodePosition + 1)
        return numNodes
    
    def _countNodes(self, node):
        if not node:
            return
        leftDepth = self.depth(node)
        rightDepth = 0 if not node.right else 1 + self.depth(node.right)
        if leftDepth == 0 and rightDepth == 0:
            return
        if rightDepth == leftDepth:
            self.nodePosition += 2 ** (leftDepth - 2)
            self._countNodes(node.right)
        else:
            self._countNodes(node.left)
