class Solution:
    def isAnagram(self, s, t):
        count2, count1 = [0] * 26, [0] * 26
        
        for c in s:
            count1[ord(c) - ord('a')] += 1 
            
        for c in t:
            count2[ord(c) - ord('a')] += 1 
            
        return count1==count2