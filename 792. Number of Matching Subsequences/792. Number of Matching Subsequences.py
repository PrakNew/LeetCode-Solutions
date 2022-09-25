from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, S, words):
        word_dict = defaultdict(list)
        res = 0
        
        for word in words:
            word_dict[word[0]].append(word)
        
        for ch in S:
            temp_dict = word_dict[ch]
            word_dict[ch] = []
            for word in temp_dict:
                if len(word)==1:
                    res += 1
                else:
                    word_dict[word[1]].append(word[1:])
        
        return res
        