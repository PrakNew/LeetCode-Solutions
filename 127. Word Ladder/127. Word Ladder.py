import collections

class Solution:
    def __init__(self):
        self.graph = collections.defaultdict(list)
        self.n = 0
    
    def visitNode(self, q, visited, other_visited):
        current_word, level = q.popleft()
    
        for i in range(self.n):
            intermediate_word = current_word[:i] + '*' + current_word[i+1:]
            
            for word in self.graph[intermediate_word]:
                if word in other_visited:
                    return level + other_visited[word]
                if word not in visited:
                    q += (word, level+1),
                    visited[word] = level+1
        return None
        
    
    def ladderLength(self, beginWord, endWord, wordList):
        
        if not wordList or endWord not in wordList or not endWord or not beginWord:
            return 0
        
        self.n = len(beginWord)
        
        for word in set(wordList):
            for i in range(self.n):
                self.graph[word[:i] + "*" + word[i+1:]].append(word)
        
        q_start = collections.deque([(beginWord, 1)])
        q_end = collections.deque([(endWord, 1)])
        visited_start = {beginWord: 1}
        visited_end = {endWord: 1}
        
        while q_start and q_end:
            ans = self.visitNode(q_start, visited_start, visited_end)
            if ans:
                return ans
            ans = self.visitNode(q_end, visited_end, visited_start)
            if ans:
                return ans
        
        return 0
        