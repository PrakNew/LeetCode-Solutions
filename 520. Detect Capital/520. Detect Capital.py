'''
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def detectCapitalUse(self, word):        
        ct = sum(1 for ch in word if 'A'<=ch<='Z')
        
        if ct==len(word) or (ct==1 and 'A'<=word[0]<='Z'):  # All uppercase or first letter uppercase
            return True
        elif ct==0: # all lowercase
            return True
        return False
            
        