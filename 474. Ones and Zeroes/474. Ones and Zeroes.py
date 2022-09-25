class Solution:
    def findMaxForm(self, strs, m, n):
        
        def calc(string):
            return [string.count('0'), string.count('1')]
        
        l = len(strs)
        dp = [[0  for _ in range(n+1)] for _ in range(m+1)]
        
        for zero, one in (calc(str) for str in strs):
            for x in range(m, -1, -1):
                for y in range(n, -1, -1):
                    if x>=zero and y>=one:
                        dp[x][y] = max(1 + dp[x-zero][y-one], dp[x][y])
            for i in range(m):
                print(dp[i])
        
        return dp[m][n]
