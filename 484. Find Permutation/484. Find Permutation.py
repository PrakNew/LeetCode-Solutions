'''
Idea: Two pointers

Time complexity : O(n)
Space complexity: O(1)

'''


class Solution:
    def findPermutation(self, s):
        
        n = len(s) + 1
        res = [i for i in range(1, n+1)]
        i = 0
        
        while i < n-1:
            if s[i]=='D':
                j = i
                while j<n-1 and s[j]=='D':
                    j += 1
                    
                # Reverse array from index i to j
                x, y = i, j
                while x<y:
                    res[x], res[y] = res[y], res[x]
                    x += 1
                    y -= 1
                
                # Update position
                i = j
                
            i += 1
    
        return res