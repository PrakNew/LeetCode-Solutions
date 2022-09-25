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
    def findRedundantDirectedConnection(self, edges):
        
        # Case 1: There is no cycle, there exist two edges pointing to same node
        # case 2: There is a cycle, there exist no two edges pointing to same node
        # Case 3: There is a cycle, there exist two edges pointing to same node
        
        cand1, cand2, point_to = None, None, collections.defaultdict()
        n = len(edges)
        
        for u, v in edges:
            if v in point_to:
                cand1, cand2 = point_to[v], [u, v]
            else:
                point_to[v] = [u, v]
            
        uf = UnionFind(n)
        
        for u, v in edges:
            if [u, v] == cand2: 
                continue 
            if not uf.union(u, v):
                if cand1:
                    return cand1
                return [u, v]
        
        return cand2
            