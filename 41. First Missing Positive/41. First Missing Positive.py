'''
Time complexity : O(n)
Space complexity: O(1)
'''

class Solution:
    def firstMissingPositive(self, A):
            
        n = len(A)
   
        for i in range(n):
            while 1<=A[i]<=n and A[A[i]-1]!=A[i]:
                ind1, ind2 = i, A[i]-1
                A[ind1], A[ind2] = A[ind2], A[ind1]
                
        for i in range(n):
            if A[i]!=i+1:
                return i+1 
        
        return n+1
        
        
            
        
    
    