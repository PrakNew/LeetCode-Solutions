import collections

class UnionFind:
    def __init__(self, n):
        self.size = n
        self.components = n
        self.parent = list(range(n+1))
        self.sizeOf = [1] * (n+1)
    
    def find(self, p):
        root = p
        while self.parent[root]!=root:
            root = self.parent[root]
        while p!=root:
            next_node = self.parent[p]
            self.parent[p] = root
            p = next_node
        return root
    
    def union(self, u, v):
        root1, root2 = self.find(u), self.find(v)
        if root1==root2:
            return False
        elif self.sizeOf[root1] > self.sizeOf[root2]:
            self.sizeOf[root1] += self.sizeOf[root2]
            self.parent[root2] = root1
        else:
            self.sizeOf[root2] += self.sizeOf[root1]
            self.parent[root1] = root2
        self.components -= 1
        return True
    
class Solution:
    def findRedundantConnection(self, edges):
        
        n = len(edges)
        uf = UnionFind(n)
        for edge in edges:
            if not uf.union(*edge):
                return edge
        
        return [-1, -1]
        