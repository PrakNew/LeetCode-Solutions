import collections

class TrieNode:
    
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.isWord = True
    
    def search(self, word):
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if not node:
                return False
        return node.isWord
    


class Solution:
    def findWords(self, board, words):
        m, n = len(board), len(board[0])
        res = []
        trie = Trie()
        node = trie.root
        
        for word in words:
            trie.insert(word)
        
        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, node, '', res)
        
        return res
    
    
    def dfs(self, A, x, y, node, path, res):
        
        if node.isWord:
            res.append(path)
            node.isWord = False
        
        if not 0<=x<len(A) or not 0<=y<len(A[0]):
            return
        
        ch= A[x][y]
        node = node.children.get(ch)
        if not node:
            return
        
        A[x][y] = "#"  # visited
        
        for i, j in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
            self.dfs(A, i, j, node, path + ch, res)
        
        # backtrack
        A[x][y] = ch
        
        
        
        