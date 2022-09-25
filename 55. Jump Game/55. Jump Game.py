'''
Time complexity : O(n)
Space complexity : O(1)
'''

class Solution:
    def canJump(self, A):
        n = len(A)
        if n==1:
            return True
        
        max_so_far = 0
        for i in range(n-1):
            if max_so_far < i:
                return False
            max_so_far = max(max_so_far, i + A[i])
            if max_so_far >= n-1:
                return True
            
        return False
