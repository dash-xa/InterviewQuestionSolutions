# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.G = []
        self.kids = {}
    def loadGraph(self, head):
        q = [head]
        while q:
            n = q.pop(0)
            G.append(n)
            self.kids[n] = []
            for kid in [n.left, n.right]:
                if kid:
                    self.kids[n].append(kid)
                    q.append(kid)
            self.visited.add(n)
print({1:3 for i in range(3)})
S = set()
S.add(tuple([1, 2]))
print(S)
