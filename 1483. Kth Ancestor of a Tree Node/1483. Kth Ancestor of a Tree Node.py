from math import log2

class TreeAncestor:

    def __init__(self, n, parent):
        m = 1 + int(log2(n)) 
        self.dp = [[-1 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            self.dp[i][0] = parent[i]
            for j in range(1, m):
                if self.dp[i][j-1]!=-1:
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]

    def getKthAncestor(self, node, k):
        while k>0 and node!=-1:
            i = int(log2(k))
            node = self.dp[node][i]
            k -= (1<<i) # check in powers of 2: 1, 2, 4, 8,....
       
        return node
        
        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)