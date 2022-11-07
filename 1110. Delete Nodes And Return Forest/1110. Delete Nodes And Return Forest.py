'''Its not and optimized solution but we can use it to fetch all the subtrees where break point will be there and check out for all the subtrees'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.l=[root]
        flag=0
        if root.val in to_delete:flag=1
        to_delete1=set(to_delete)
        def convert(node,parent):
            if node.val in to_delete:
                to_delete.remove(node.val)
                if node.left : 
                    self.l.append(node.left)
                    if node.left.val in to_delete:to_delete.append(node.left.val)
                if node.right:
                    self.l.append(node.right)
                    if node.right.val in to_delete:to_delete.append(node.right.val)
                if parent:
                    if node==parent.left:parent.left=None
                    if node==parent.right:parent.right=None

                return 
            if node.left:
                convert(node.left,node)
            if node.right:
                convert(node.right,node)

        ini=0
        while to_delete:
            try:
                convert(self.l[ini],None)
            except Exception:
                break
            if not to_delete:
                break
            ini+=1
        if flag==1:
            self.l.pop(0)
        l1=[]
        for ind,x in enumerate(self.l):
            if x.val not in to_delete1:
                l1.append(x)

        return l1
            