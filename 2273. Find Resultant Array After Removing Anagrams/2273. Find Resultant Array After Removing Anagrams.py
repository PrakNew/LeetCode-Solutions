class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        l=[words[0]]
        for x in range(1,len(words)):
            if sorted(l[-1])!=sorted(words[x]):
                l.append(words[x])
        return l