class Solution:
    def findLongestChain(self, A):
        n = len(A)
        A.sort()
        dp = [0] * n
        size = 0
        for a, b in A:
            i, j = 0, size
            while i!=j:
                mid = (i+j)>>1
                if A[mid][1] < a:
                    i = mid + 1
                else:
                    j = mid
            dp[i] = [a, b]
            size = max(i+1, size)
        
        return size
        