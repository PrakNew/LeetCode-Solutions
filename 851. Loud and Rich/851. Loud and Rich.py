import collections

class Solution:
    def loudAndRich(self, richer, quiet):
            
        n = len(quiet)
        graph = collections.defaultdict(list)
        for x, y in richer:
            graph[y].append(x)
        
        def dfs(node):
            if res[node] is None:
                res[node] = node
                for child in graph[node]:
                    cand = dfs(child)
                    if quiet[cand] < quiet[res[node]]:
                        res[node] = cand
            return res[node]
        
        res = [None] * n 
        return map(dfs, range(n))