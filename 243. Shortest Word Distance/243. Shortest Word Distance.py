import collections

class Solution:
    def shortestDistance(self, words, word1, word2):
        
        n = len(words)
        
        ind1, ind2 = [], []
        for i in range(n):
            if words[i]==word1:
                ind1.append(i)
            elif words[i]==word2:
                ind2.append(i)
        
        i, j = 0, 0
        res = float('inf')
        while i<len(ind1) and j<len(ind2):
            res = min(res, abs(ind1[i]-ind2[j]))
            if ind1[i] < ind2[j]:
                i+=1
            else:
                j+=1
        
        return res
        