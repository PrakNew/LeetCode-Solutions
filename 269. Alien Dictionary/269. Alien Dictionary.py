import collections

class Solution:
    def alienOrder(self, words):
        n = len(words)
        reverse_graph = {c: [] for word in words for c in word}
        for i in range(n-1):
            word1, word2 = words[i], words[i+1]
            for x, y in zip(word1, word2):
                if x!=y:
                    reverse_graph[y].append(x)
                    break
            else:
                if len(word1) > len(word2):
                    return ""
        
        output = []
        seen = {}
        
        def dfs(node):
            if node in seen:
                return seen[node]
            seen[node] = False
            for nei in reverse_graph[node]:
                if not dfs(nei):
                    return ""
            
            seen[node] = True
            output.append(node)
            return True
        
        if not all(dfs(node) for node in reverse_graph):
            return ""
        
        return "".join(output)