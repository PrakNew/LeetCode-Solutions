#TRIE implementation and Backtracking over it

import sys
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord=False
        self.refs=0
        
    def addWord(self, word):
        cur=self
        cur.refs+=1
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
            cur.refs+=1
        cur.isWord=True
    
    def removeWord(self,word):
        cur=self
        cur.refs-=1
        for x in word:
            if x in cur.children:
                cur=cur.children[x]
                cur.refs-=1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        print(sys.version)
        root = TrieNode()
        for w in words:
            root.addWord(w)
            
        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):
            if (r<0 or r==ROWS or c<0 or c==COLS or (r,c) in visited or board[r][c] not in node.children or node.children[board[r][c]].refs < 1):return 
            visited.add((r,c))
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.isWord:
                res.add(word)
                node.isWord=False
                root.removeWord(word)
                
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visited.remove((r,c))

        for r,c in product(range(ROWS),range(COLS)):
            if board[r][c] in root.children:
                dfs(r, c, root, "")

        return res