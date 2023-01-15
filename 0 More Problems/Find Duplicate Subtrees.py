import collections 

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def findDuplicateSubtrees(root):
    trees = collections.defaultdict()

    trees.default_factory = trees.__len__  # to avoid keyError

    counter = collections.Counter() 
    ans = [] 

    def lookup(node): 
        # method returns the ID of given subtree 
        if node: 
            # get ID for current Subtree 
            subtree = trees[node.val,lookup(node.left), lookup(node.right)]
            
            # increment the count for given subtree
            counter[subtree] += 1 

            if counter[subtree]==2: # duplicate subtree 
                ans.append(node) # store only the root of the subtree  
        
            return subtree 
    
    lookup(root) 
    return ans 


if __name__ == '__main__':

    node1 = Node(1)
    node2_1 = Node(2)
    node2_2 = Node(2)
    node3 = Node(3)
    node4_1 = Node(4)
    node4_2 = Node(4)
    node4_3 = Node(4)

    root = node1
    node1.left = node2_1
    node1.right = node3 
    node2_1.left = node4_1
    node3.left = node2_2 
    node3.right = node4_2
    node2_2.left = node4_3 

    ans = findDuplicateSubtrees(root)
    print("Root of duplicate subtrees: ")
    for node in ans:
        print(node.val)


    

