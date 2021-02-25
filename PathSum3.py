from collections import defaultdict
# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Questions:
    # Is the binary tree a search tree?
    # Can it have null value nodes? If so, how should we deal with that?
    # Assume not a bst, and no null value nodes

    # Input: Node
    # Output: int

    # Ex: sum = 4
    #           1
    #       2       3
    #     1       0   7
    # Output: 3

    # {1}
    # {3, 2}
    # {4, 3, 1}
    
    # Brute force idea: try all nodes
    # Time complexity: hard to say
    # Space complexity: also hard to say
    def pathSum(self, node, sum):
        if node is None:
            return 0
        counter = self.pathAccumulate(node, sum, 0)
        counter += self.pathSum(node.left, sum)
        counter += self.pathSum(node.right, sum)
        return counter

    def pathAccumulate(self, node, sum, cum):
        if node is None:
            return 0
        cum += node.val

        counter = int(cum == sum)
        counter += self.pathAccumulate(node.left, sum, cum)
        counter += self.pathAccumulate(node.right, sum, cum)
        return counter
        
sol = Solution()

root = Node(1)
node = root
node.right = Node(2)
node = node.right
node.right = Node(3)
node = node.right
print(sol.pathSum(root, 3))
print()