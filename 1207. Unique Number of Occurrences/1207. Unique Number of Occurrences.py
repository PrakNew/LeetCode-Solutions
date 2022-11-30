# Easy implementation   
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        l=Counter(arr).values()
        return len(l)==len(set(l))