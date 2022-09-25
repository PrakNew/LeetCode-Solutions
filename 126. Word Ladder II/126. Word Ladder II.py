import collections

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        
        if endWord not in wordList:
            return [] 
        graph = collections.defaultdict(list)
        n = len(beginWord)
        
        for word in wordList:
            for i in range(n):
                graph[word[:i] + '*' + word[i+1:]].append(word)
        
        res = []
        queue_start = collections.deque([beginWord])
        queue_end = collections.deque([endWord])
        visited_start = set([beginWord])
        visited_end = set([endWord])
        parents = collections.defaultdict(set)
        found = False
        depth = 0
        rev = False
        
        while queue_start and not found:
            depth += 1
            size = len(queue_start)
            localVisited = set()
            for _ in range(size):
                word = queue_start.popleft()
                for i in range(n):
                    for nextWord in graph[word[:i] + '*' + word[i+1:]]:
                        if nextWord not in visited_start:
                            localVisited.add(nextWord)
                            if nextWord in visited_end:
                                found = True
                            queue_start.append(nextWord)
                            if not rev:
                                parents[nextWord].add(word)
                            else:
                                parents[word].add(nextWord)
                            
            visited_start = visited_start.union(localVisited)
            
            queue_start, queue_end = queue_end, queue_start
            visited_start, visited_end = visited_end, visited_start
            rev = not rev
            
                                        
        def dfs(word, path, d):
            if d==0:
                if path[-1]==beginWord:
                    res.append(path[::-1])
                return
            
            for parent in parents[word]:
                dfs(parent, path + [parent], d-1)
        
        dfs(endWord, [endWord], depth)
        
        return res

                