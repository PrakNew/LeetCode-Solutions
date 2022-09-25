class Solution:
    def isAlienSorted(self, words, order):
        
        order = {key: val+1 for val, key in enumerate(order)}
        
        
        max_code = 0
        n = len(words)
        for i in range(1, n):
            j = 0
            while j < min(len(words[i-1]), len(words[i])) and words[i][j]==words[i-1][j]:
                j += 1
            
            if j==len(words[i]) and j < len(words[i-1]):
                return False
            
            if j < len(words[i-1]) and order[words[i-1][j]] > order[words[i][j]]:
                return False
            
            
        return True