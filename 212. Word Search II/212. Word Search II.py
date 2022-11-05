#Python solution using Trie and DFS and backtracking
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                node.isWord = False
                res.add(word)
                root.removeWord(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)


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
        
        
        
        