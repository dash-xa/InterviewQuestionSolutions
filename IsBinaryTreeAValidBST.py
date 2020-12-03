# Question: Check that binary tree is a BST
# Questions: Can tree have equal nodes? If so, which branch can they be in? Can nodes have null values? If so, how can they be treated
# Answers: Assume no equal nodes, and no null values


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, node, minValue=-float("inf"), maxValue=float("inf")):
        if node is None:
            return True
        leftValid = self.isValidBST(node.left, minValue, node.val)
        rightValid = self.isValidBST(node.right, node.val, maxValue)
        return leftValid and rightValid and (minValue < node.val < maxValue)