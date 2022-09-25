'''
Idea: Manacher's algorithm to find the longest palindromic substring

Time complexity: O(n)
Space complexity: O(n)
'''

class Solution:
    def longestPalindrome(self, s):
        
        def manachers(s):
            A = '@#' + '#'.join(s) + '#$'
            n = len(A)
            center = right = 0
            Z = [0] * n
            for i in range(1, n-1):
                if i < right:
                    Z[i] = min(right-i, Z[2*center-i])
                    
                while A[i+Z[i]+1] == A[i-Z[i]-1]:
                    Z[i] += 1
                
                if right < i + Z[i]:
                    right = i + Z[i]
                    center = i
            
            return Z
        
        
        maxlen, center = max((length, center) for center, length in enumerate(manachers(s)))
        l = (center - maxlen)>>1
        r = (center + maxlen)>>1
        return s[l:r]