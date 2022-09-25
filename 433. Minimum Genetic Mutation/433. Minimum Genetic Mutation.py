import collections

class Solution:
    def minMutation(self, start, end, bank):  
        if end not in bank or not end or not bank:
            return -1
        
        bank = set(bank)
        graph = collections.defaultdict(list)
        for gene in bank:
            for i in range(8):
                graph[gene[:i] + '*' + gene[i+1:]].append(gene)
        q = collections.deque([start])
        visited = set([start])
        depth = 0
        found = False  
        while q and not found:
            depth += 1
            size = len(q)
            localVisited = set()
            for _ in range(size):
                gene = q.popleft()
                for i in range(8):
                    for nextGene in graph[gene[:i] + '*' + gene[i+1:]]:
                        if nextGene not in visited:
                            if nextGene == end:
                                found = True
                            localVisited.add(nextGene)
                            q += nextGene,
            visited = visited.union(localVisited)
        
        if found:
            return depth
        return -1