"""
Idea: Two pointers

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def minWindow(self, S, T):
        res = ""
        min_len = len(S) + 1
        j = 0
        i = 0
        while i < len(S):
            if S[i] == T[j]:
                j += 1
                if j == len(T): 
                    j -= 1
                    end = i + 1
                    while j >= 0:
                        if S[i] == T[j]:
                            j -= 1
                        i -= 1
                    
                    i += 1
                    j += 1
                    
                    if end - i < min_len:
                        min_len = end - i
                        res = S[i:end]
                        
            i+=1
            
        return res
        
        