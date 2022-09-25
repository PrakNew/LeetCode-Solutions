class Solution:
    def maxUniqueSplit(self, s):
        
        def util(s, seen):
            max_len = 0
            for i in range(1, len(s)+1):
                candidate = s[0:i]
                if candidate not in seen:
                    seen.add(candidate)
                    max_len = max(max_len, 1 + util(s[i:], seen))
                    seen.remove(candidate)
            
            return max_len
                

        return util(s, set())
        