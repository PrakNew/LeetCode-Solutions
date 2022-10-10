# The simple logic over here is to iterate over the boundaries and check whichever 'O' are connected to the boundary 'O'
class Solution:
    def solve(self, b: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n,m=len(b),len(b[0])
        self.l=[["X"]*m for _ in range(n)]
        visited=set()
        def check(x,y):
            if (x,y) in visited:
                return 
            if b[x][y]=='O':self.l[x][y]='O'
            visited.add((x,y))
            l=[(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
            for i,j in l:
                if 0<=i<n and 0<=j<m and b[i][j]=='O':
                    check(i,j)

        for x in range(n):
            if b[x][0] == 'O':
                check(x,0)
            if b[x][m-1]=='O':
                check(x,m-1)
        for x in range(m):
            if b[0][x]=='O':
                check(0,x)
            if b[n-1][x]=='O':
                check(n-1,x)
        for x in range(n):
            for y in range(m):
                b[x][y]=self.l[x][y]


import collections

class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        
        def checkBorder(x, y):
            return x in [0, m-1] or y in [0, n-1]
        
        if not board:
            return board
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                if not visited[r][c] and board[r][c]=='O':
                    isBorder = False
                    q = collections.deque([(r, c)])
                    visited[r][c] = True
                    seen = []
                    while q:
                        x, y = q.popleft()
                        if checkBorder(x, y):
                            isBorder = True
                        seen.append((x, y))
                        for i, j in ((x+1, y), (x, y+1), (x-1, y), (x, y-1)):
                            if 0<=i<m and 0<=j<n and not visited[i][j] and board[i][j]=='O':
                                visited[i][j] = True
                                q.append((i, j))
                    
                    if not isBorder:
                        for x, y in seen:
                            board[x][y] = 'X'
        
        return board
                        