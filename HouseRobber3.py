# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.M = {}
    def K(self, node):
        return 0 if not node else self.rob(node.left) + self.rob(node.right)
    def rob(self, node: TreeNode) -> int:
        if not node:
            return 0
        if node in self.M:
            return self.M[node]
        include = node.val + self.K(node.left) + self.K(node.right)
        exclude = self.rob(node.left) + self.rob(node.right)
        self.M[node] = max(include, exclude)
        return self.M[node]