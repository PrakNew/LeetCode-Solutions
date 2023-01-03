#Python 1 liner solution
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(list(x) != sorted(x) for x in zip(*strs))