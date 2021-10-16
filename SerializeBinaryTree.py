# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # Idea: perform preorder traversal while keeping track of each time you go up
        def preorder_encode(node):
            if not node:
                order.append("up")
            else:
                order.append(str(node.val))
                preorder_encode(node.left)
                preorder_encode(node.right)
        order = []
        preorder_encode(root)
        return ' '.join(order)
        # return ' '.
        # Is the tree a binary search tree?
        # Does it have duplicate nodes?
        # Do all non-null nodes have non-null values?
        # It the tree a binary tree?
        
        # Idea: we could perform some traversal of tree. Then serialize that
        
        #         1
        #     2       3
        #   6  7    4   5  
        # 8
        # 1 2 6 8 up up up 7 up up 3 4 up up 5 up up
        # order = [], [1], [1, 2], [1, 2, 6], [1, 2, 6 8] [1 2 6 8 up up]
        # [1 2 6 8 up up up up up 7 up up up up 3 4 up up up 5 up up up up up]
        # First idea: perform level order traversal of tree. Put "Null" in string for null nodes\
        # Very inefficient for deep or unbalanced trees (O(N) unbalanced tree will take O(2^N) memory store)
        
        # Another idea: store path for each node
        # [1], [1->left->2], [1->right->3], [1->right->3->left->4]
        # Each node has path of at most length N to it. There are N nodes, so this would take O(N^2) time and space
        
        # Maybe better idea: store only paths to leaf nodes
        # [1->left->2], [1->right->3->left->4], [1->right->3->right->4]
        # Generate tree using this path
        
        # Another idea: Given a node, we want to know where its children are
        # Preorder traversal of tree above: [1 2 6 8 7 3 4 5]
        # Could we put data into preorder traversal to indicate where the node's children are?
        # Idea: try putting flag that says we go up after finishing with a node
        # [1 2 6 8 up up 7 up up 3 4 up 5 up up]
        # [1 2 6 8 up up up up up 7 up up up up 3 4 up up up 5 up up up up]
        # The example tree given above would be
        # [1 2 up up up 3 4 up up 5 up up up]
        
        # For 1268 tree, we can reconstruct it:
                # 1
            # 2     3
         # 6   7   4  5
       # 8             
    # O(N) time because each node is entered only once. Also only as many up chars as nodes
    # O(N) space for same reason as above
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # 1 2 6 8 up up up 7 up up 3 4 up up 5 up up
        def preorder_decode():
            nodeValue = nodes.pop()
            if nodeValue == "up":
                return None
            node = TreeNode(int(nodeValue))
            node.left = preorder_decode()
            node.right = preorder_decode()
            return node
        nodes = data.split()[::-1] # want to pop from beginning while pops from end take O(1), pop from beginning takes O(N) 
        return preorder_decode()
        # Ex: above
        # node = 1.
        # node.left = decode()
            # pop 2. 2.left = decode
                # pop 6. 6.left = decode
                    # pop 8. 8.left = decode
                        # pop up. return None, so 8.left=None
                    # 8.right = decode
                        # pop up. return None, so 8.right=None
                # 6.right = decode
                    # pop up. return None, so 6.right = None
            # 2.right = deocde
                # pop 7. 7.left=decode
                    # pop up
                    # 7.left = 7.right = no kids
        # 1.right = decode()
            # 3
                
        
        # First node: 1
        # 1.left = 2
            # 2.left = 6
                # 6.left = 8
                    # 8.left = up, ie none.
                    # 8.right = up, ie none
                # 6.right = up, ie none
            # 2.right = 7
                # 7.left = up
                # 7.right = up
        
            
        
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))