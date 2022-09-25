class Solution:
    def shortestWordDistance(self, words, word1, word2):
        
        ind1, ind2 = [], []
        n = len(words)
        for i in range(n):
            if word1 == words[i]:
                ind1 += i,
            elif word2 == words[i]:
                ind2 += i,
        
        if word1==word2:
            res = float('inf')
            for i in range(1, len(ind1)):
                res = min(res, ind1[i]-ind1[i-1])
            return res
        
        res = float('inf')
        i, j = 0, 0
        while i < len(ind1) and j < len(ind2):
            res = min(res, abs(ind1[i] - ind2[j]))
            if ind1[i] < ind2[j]:
                i += 1
            else:
                j += 1
        
        return res
    