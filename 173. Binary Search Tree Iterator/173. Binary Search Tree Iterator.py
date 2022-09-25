# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.pointer = root


    def next(self):
        """
        @return the next smallest number
        """
        while self.pointer:
            self.stack += self.pointer,
            self.pointer = self.pointer.left 
        
        node = self.stack.pop()
        self.pointer = node.right
        
        return node.val 
        
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        """
        return len(self.stack)>0 or self.pointer!=None
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()