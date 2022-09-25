class Solution:
    def myPow(self, x, n, dp={}):
        if n==-1:
            return 1/x
        elif n==0:
            return 1
        elif n==1:
            return x
        
        key = (x, n)
        
        if key not in dp:
            if n&1: 
                dp[key] =  self.myPow(x, n>>1, dp) * self.myPow(x, n>>1, dp) * x
            else:
                dp[key] = self.myPow(x, n>>1, dp) * self.myPow(x, n>>1, dp)
        
        return dp[key]
        
            
        
            
        
        