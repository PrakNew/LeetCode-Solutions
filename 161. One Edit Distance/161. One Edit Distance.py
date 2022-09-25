'''
Time Complexity : O(n)
Space Complexity : O(n)
'''

class Solution:
    def isOneEditDistance(self, x, y):
        # x is smaller than y
        m, n = len(x), len(y)
        
        if m > n:
            return self.isOneEditDistance(y, x)
        
        if n - m > 1:
            return False
        
        for i in range(m):
            if x[i]!=y[i]:
                if m==n: 
                    return x[i+1:]==y[i+1:]
                else:
                    return x[i:]==y[i+1:]
        
        return m+1==n

            