class Solution:
    def numSubmat(self, A):
        def countRow(C):
            ans = 0
            length = 0
            for i in range(len(C)):
                if C[i]==1:
                    length += 1
                else:
                    length = 0
                ans += length
            return ans
        
        m, n = len(A), len(A[0])
        res = 0
        for up in range(m):
            h = [1] * n
            for down in range(up, m):
                for j in range(n):
                    h[j] &= A[down][j]
                res += countRow(h)
        
        return res