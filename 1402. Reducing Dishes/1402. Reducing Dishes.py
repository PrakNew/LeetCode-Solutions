class Solution:
    def maxSatisfaction(self, A):
        A.sort()
        
        max_sum = A[-1]
        
        if A[-1]<0:
            return 0
        
        dishes = 2
        
        while dishes<=len(A):
            curr = 0
            time = 1
            for i in range(len(A)-dishes, len(A)):
                curr += time * A[i]
                time += 1
                
            if curr >= max_sum:
                max_sum = curr
            else:
                return max_sum
        
            dishes += 1
        
        return max_sum