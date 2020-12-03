# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
# 
# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the tree.

# Solution:
# Passed LeetCode, faster than 60%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ancestor = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self._findLowestCommonAncestor(root, p, q)
        return self.ancestor

    def _findLowestCommonAncestor(self, node, p, q):
        if node is None:
            return (False, False)
        leftP, leftQ = self._findLowestCommonAncestor(node.left, p, q)
        rightP, rightQ = self._findLowestCommonAncestor(node.right, p, q)
        foundP = leftP or rightP or node == p
        foundQ = leftQ or rightQ or node == q
        ancestorAlreadyFound = (leftP and leftQ) or (rightP and rightQ)
        currentIsAncestor = (not ancestorAlreadyFound) and foundP and foundQ
        if currentIsAncestor:
            self.ancestor = node
        return (foundP, foundQ)