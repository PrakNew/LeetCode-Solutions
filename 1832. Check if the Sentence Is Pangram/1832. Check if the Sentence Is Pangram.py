#easy solution
from collections import Counter
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d=Counter(sentence)
        l=list('abcdefghijklmnopqrstuvwxyz')
        return all(x in d for x in l)