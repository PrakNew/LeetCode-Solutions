class Solution:
    def findDuplicate(self, A):
        # Floyds algorithm
        
        # Phase 1: Detect intersection point
        hare = tortoise = A[0]
        while True:
            hare = A[A[hare]]
            tortoise = A[tortoise]
            if hare == tortoise:
                break
        
        # Phase 2: Find the entrance of the cycle
        tortoise = A[0]
        while hare!=tortoise:
            hare = A[hare]
            tortoise = A[tortoise]
        
        return tortoise
        
        
            
        
        
        