class Solution:
    def longestConsecutive(self, A):
        
        res = 0
        A = set(A)
        
        for num in A:
            if num-1 not in A:
                current_num = num
                current_streak = 1
            
                while current_num + 1 in A:
                    current_num += 1
                    current_streak += 1
            
                res = max(res, current_streak)
        
        return res
            
        
                
                
                