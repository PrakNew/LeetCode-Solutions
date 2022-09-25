"""
Idea: Check the frequency counts match and character set of both the strings are same

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def closeStrings(self, word1, word2):
        m, n = len(word1), len(word2)
        if m != n:
            return False
        
        mp1 = [0] * 26
        mp2 = [0] * 26
        
        s1, s2 = set(word1), set(word2)
        
        for ch in word1:
            mp1[ord(ch) - 97] += 1
        
        for ch in word2:
            mp2[ord(ch) - 97] += 1
        
        mp1.sort()
        mp2.sort()
        
        return mp1 == mp2 and s1 == s2
        