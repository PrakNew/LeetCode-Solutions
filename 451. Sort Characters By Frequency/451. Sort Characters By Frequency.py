class Solution:
    def frequencySort(self, s):
        table = set()
        for ch in set(s):
            table.add((s.count(ch), ch))
        
        res = ""
        
        for freq, ch in sorted(table, reverse=True):
            res += ch*freq
        
        return res