class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = n
        self.components = n
        self.sizeOf = [1 for _ in range(n)]
    
    def find(self, p):
        root = p
        while self.parent[root]!=root:
            root = self.parent[root]
        while p!=root:
            next_node = self.parent[p]
            self.parent[p] = root
            p = next_node
        return root
    
    def union(self, x, y):
        root1, root2 = self.find(x), self.find(y)
        
        if root1==root2:
            return False
        elif self.sizeOf[root1] > self.sizeOf[root2]:
            self.parent[root2] = root1
            self.sizeOf[root1] += self.sizeOf[root2]
        else:
            self.parent[root1] = root2
            self.sizeOf[root2] += self.sizeOf[root1]
        self.components -= 1
        return True

class Solution:
    def validTree(self, n, edges):
        uf_obj = UnionFind(n)
        for edge in edges:
            if not uf_obj.union(*edge):
                return False
        
        return True if uf_obj.components==1 else False
                
        