import collections

class WordDistance:

    def __init__(self, words):
        self.words = words
        self.indices = collections.defaultdict(list)
        for i in range(len(words)):
            self.indices[words[i]].append(i)
        

    def shortest(self, p, q):
        ind1, ind2 = self.indices[p], self.indices[q]
        
        res = float('inf')
        i, j = 0, 0
        while i<len(ind1) and j<len(ind2):
            res = min(res, abs(ind1[i]-ind2[j]))
            if ind1[i] < ind2[j]:
                i += 1
            else:
                j += 1
        
        return res
        
        
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)