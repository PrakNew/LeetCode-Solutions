class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def height(root):
    if not root:
        return  0
    return 1 + max(height(root.left), height(root.right))

def diameter(root):
    if not root:
        return 0  

    lHeight = height(root.left) 
    rHeight = height(root.right)

    lDiameter = diameter(root.left)
    rDiameter = diameter(root.right)

    return max(lDiameter, rDiameter, lHeight + rHeight)

one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)   
five = TreeNode(5)

root = one
root.left, root.right = two, three          
two.left, two.right = four, five    

print("Diameter = ", diameter(root))