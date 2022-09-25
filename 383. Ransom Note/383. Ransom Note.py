'''
Time complexity : O(n)
Space complexity: O(n)
'''

import collections

class Solution:
    def canConstruct(self, ransomNote, magazine):
        magazine = collections.Counter(magazine)
        ransomNote = collections.Counter(ransomNote)
        
        for letter in ransomNote:
            if letter not in magazine or ransomNote[letter] > magazine[letter]:
                return False
        
        return True
        