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
                        