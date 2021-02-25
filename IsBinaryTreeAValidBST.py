# Question: Check that binary tree is a BST
# Questions: Can tree have equal nodes? If so, which branch can they be in? Can nodes have null values? If so, how can they be treated
# Answers: Assume no equal nodes, and no null values


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#=========== Version 1, using min/max variables ================
class Solution:
    def isValidBST(self, node, minValue=-float("inf"), maxValue=float("inf")):
        if node is None:
            return True
        leftValid = self.isValidBST(node.left, minValue, node.val)
        rightValid = self.isValidBST(node.right, node.val, maxValue)
        return leftValid and rightValid and (minValue < node.val < maxValue)

#========== Version 2, using modified inorder traversal =========
# (Sexier imo)
# If the binary tree is a BST, the function returns an increasing sequence of integers (the tree's inorder traversal).
# As soon as the sequence fails to be increasing, we return infinity and know that our tree is not a valid BST.
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def f(node, m):
            if node is None:
                return m
            elif node.val <= f(node.left, m):
                return float('inf')
            else:
                return f(node.right, node.val)
        return f(root, -float('inf')) < float('inf')
        