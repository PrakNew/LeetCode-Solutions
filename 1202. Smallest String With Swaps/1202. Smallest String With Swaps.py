"""
Idea: Find the connected components and sort the letters in each component

"""

import collections

class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        graph = collections.defaultdict(list)
        n = len(s)
        res = ['0'] * n
        for a, b in pairs:
            graph[a].append(b)
            graph[b].append(a)
        
        
        visited = set()
        for i in range(n):
            if i not in visited:
                q = collections.deque()
                q += i,
                visited.add(i)
                group = [i]
                sorted_letters = [s[i]]
                while q:
                    node = q.pop()
                    for nei in graph[node]:
                        if nei not in visited:
                            visited.add(nei)
                            group += nei,
                            sorted_letters += s[nei],
                            q += nei,
                
                sorted_letters.sort()
                for j, idx in enumerate(sorted(group)):
                    res[idx] = sorted_letters[j]
        
        return ''.join(res)