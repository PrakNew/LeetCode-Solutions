class Solution:
    def numSquares(self, n):
        
        def DynamicProgramming():
            squares = []
            i = 1
            while i*i<=n:
                squares += i*i,
                i+=1

            dp = [float('inf')] * (n+1)
            dp[0] = 0

            for square in squares:
                for i in range(square, n+1):
                    dp[i] = min(dp[i], dp[i-square]+1)

            return dp[n]
        
        def BFS():
            squares = []
            i = 1
            while i*i<=n:
                squares += i*i,
                i+=1
            
            dist = 0
            q = collections.deque([(n,0)])
            
            while q:
                x, dist = q.popleft()
                for sq in squares:
                    if sq > x:
                        break
                    if sq==x:
                        return dist+1
                    q += (x-sq, dist+1),
            
            return -1
            
        return BFS()
        
        