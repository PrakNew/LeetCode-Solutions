class Solution:
    def numTeams(self, A: List[int]) -> int:
        n = len(A)
        
        res = 0
        
        for i in range(n):
            lesser = 0
            greater = 0
        
            pivot = A[i]
            
            for j in range(i):
                if A[j]<A[i]:
                    lesser+=1
            
            for j in range(i+1, n):
                if A[j]>A[i]:
                    greater+=1
            
            res += lesser*greater
            
            reversed_lesser = i - lesser
            reversed_greater = (n-i-1) - greater
    
            res += reversed_lesser * reversed_greater

        
        return res