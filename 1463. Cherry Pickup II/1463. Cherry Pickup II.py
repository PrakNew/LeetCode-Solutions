class Solution:
    def cherryPickup(self, A):
        m, n = len(A), len(A[0])
        dp = {}
        res = 0
        
        def util(x, y, r, s):
            if not 0<=x<m or not 0<=y<n or not 0<=r<m or not 0<=s<n:
                return float('-inf')
            
            if x==m-1:
                return A[x][y] + A[r][s]
            
            key = (x, y, r, s)
            
            if key not in dp:
                
                one, two, three, four, five, six, seven, eight, nine = 0, 0, 0, 0, 0, 0, 0, 0, 0
  
                if (x+1, y-1)!=(r+1, s-1):
                    one = A[x][y] + A[r][s] + util(x+1,y-1, r+1, s-1)
                
                if (x+1, y)!=(r+1, s-1):
                    two = A[x][y] + A[r][s] + util(x+1,y, r+1, s-1)
                
                if (x+1, y+1)!=(r+1, s-1):
                    three = A[x][y] + A[r][s] + util(x+1,y+1, r+1, s-1)
                
                if (x+1, y-1)!=(r+1, s):
                    four = A[x][y] + A[r][s] + util(x+1,y-1, r+1, s)
                
                if (x+1, y)!=(r+1, s):
                    five = A[x][y] + A[r][s] + util(x+1,y, r+1, s)
                
                if (x+1, y+1)!=(r+1, s):
                    six = A[x][y] + A[r][s] + util(x+1,y+1, r+1, s)
                
                if (x+1, y-1)!=(r+1, s+1):
                    seven = A[x][y] + A[r][s] + util(x+1,y-1, r+1, s+1)
                
                if (x+1, y)!=(r+1, s+1):
                    eight = A[x][y] + A[r][s] + util(x+1,y, r+1, s+1)
                
                if (x+1, y+1)!=(r+1, s+1):
                    nine = A[x][y] + A[r][s] + util(x+1,y+1, r+1, s+1)
                
                
                dp[key] = max(one, two, three, four, five, six, seven, eight, nine)          
                
                
            return dp[key]
        
        return util(0, 0, 0, n-1)
    
            
        
        
        