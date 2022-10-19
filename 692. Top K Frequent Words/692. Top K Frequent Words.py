# Simple sorting question

from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d=Counter(words)
        words=list(set(words))
        words.sort(key=lambda x:(-d[x],x))
        return words[:k]