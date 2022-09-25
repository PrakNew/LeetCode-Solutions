'''
Idea: Use two pointers. Keep moving right pointer until a duplicate is found. 
      Once duplicate is encountered keep moving left pointer until no more duplicates exist.

Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        hashMap = [0] * 150  # input ASCII characters in the range 0 to 150
        res = 0
        n = len(s)
        i = 0
        for j in range(n):
            hashMap[ord(s[j])] += 1
            while i<j and hashMap[ord(s[j])] > 1: # move left pointer until no duplicates exist
                hashMap[ord(s[i])] -= 1
                i += 1
            res = max(res, j-i+1)
                
        return res
        