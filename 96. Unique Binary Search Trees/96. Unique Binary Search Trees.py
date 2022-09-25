class Solution:
    def numTrees(self, n):
        # G(n) = F(1, n) + F(2, n) + .. + F(n, n)
        # F(3, 7) = [1, 2] * [4,5,6,7] = G(2) * G(4)
        # G(n) = G(i-1) * G(n-i)
        
        G = [0] * (n+1)
        G[0], G[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]
        
        return G[n]
        