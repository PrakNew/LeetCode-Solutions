#just checked which value is giving us the lexicographically least element

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        d=list('abcdefghijklmnopqrstuvwxyz')
        self.x='z'*10000
        def check(root,s):
            if not root.left and not root.right:
                s=d[root.val]+s
                self.x=min(self.x,s)
            s=d[root.val]+s
            if root.left:check(root.left,s)
            if root.right:check(root.right,s)
        check(root,'')
        return self.x