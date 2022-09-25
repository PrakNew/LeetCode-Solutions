'''
# 1. Create empty stack and push root
# 2. Keep popping stack until stack is not empty and preorder[i] > stack.top()
# 3. Make it left/right child and push it into stack
# 4. Repeat 2, 3 until stack is empty

Time complexity : O(n)
Space complexity: O(h)
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def bstFromPreorder(self, preorder):
    
    if not preorder:
        return None
    
    root = TreeNode(preorder[0])
    stack = [root]
    
    for i in range(1, len(preorder)):
        temp = None
        
        while stack and preorder[i]>stack[-1].val:
            temp = stack.pop()
        
        if temp:
            temp.right = TreeNode(preorder[i])
            stack.append(temp.right)
        else:
            stack[-1].left = TreeNode(preorder[i])
            stack.append(stack[-1].left)
    
    return root