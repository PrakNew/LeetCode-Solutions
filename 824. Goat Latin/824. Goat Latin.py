'''
Time complexity : O(n)
Space complexity: O(n)
'''

class Solution:
    def toGoatLatin(self, S):
        words = S.split()
        n = len(words)
        res = ""
        for i in range(n):
            if words[i][0].lower() in ('a', 'e', 'i', 'o', 'u'):
                new_word = words[i] + 'ma' + 'a' * (i+1)
            else:
                new_word = words[i][1:] + words[i][0] + 'ma' + 'a' * (i+1)
            res += new_word + ' '
            
        return res[:-1]