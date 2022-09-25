"""
Time complexity: O(n)
Space complexity: O(26)
"""

class Solution:
    def canConvert(self, str1, str2):
        if str1 == str2:
            return True
        
        graph = {}
        n = len(str1)
        for a, b in zip(str1, str2):
            if a in graph and graph[a] != b:
                return False
            graph[a] = b 
        
        return len(set(str2)) < 26