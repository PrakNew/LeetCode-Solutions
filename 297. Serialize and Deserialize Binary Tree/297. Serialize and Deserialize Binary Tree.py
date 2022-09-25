"""
Idea: Store the preorder traversal in a data structure. Decode the data in the same fashion.

Time complexity : O(n)
Space complexity: O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        
        def encode(node, data):
            if node:
                data += str(node.val),
                encode(node.left, data)
                encode(node.right, data)
            else:
                data += '#',
        
        data = []
        encode(root, data)
        return ' '.join(data)

    def deserialize(self, data):
        
        def decode(iterator):
            val = next(iterator)
            
            if val == '#':
                return None
            
            node = TreeNode(val)
            node.left = decode(iterator)
            node.right = decode(iterator)
            return node
        
        iterator = iter(data.split())
        return decode(iterator)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans