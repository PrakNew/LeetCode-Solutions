class Solution:
    def lengthOfLastWord(self, s):
        word = ""
        res = 0
        i = 0
        while i < len(s):
            word = ""
            while i < len(s) and s[i] != " ":
                word += s[i]
                i += 1
            if word != "":
                res = len(word)
            i += 1
        
        return res