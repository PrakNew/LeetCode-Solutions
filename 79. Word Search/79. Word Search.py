class Solution:
    def exist(self, A, word):
        
        m, n = len(A), len(A[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(x, y, word):
            if word == '':
                return True

            visited[x][y] = True

            for i, j in ((x+1, y), (x-1, y), (x,y+1), (x,y-1)):
                if 0 <= i < m and 0 <= j < n and not visited[i][j] and A[i][j] == word[0] and dfs(i, j, word[1:]):
                    return True

            # backtrack
            visited[x][y] = False
            return False



        for i in range(m):
            for j in range(n):
                if A[i][j] == word[0] and dfs(i, j, word[1:]):
                    return True

        return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m=len(board),len(board[0])
        d=[[False]*m for _ in range(n)]
        def check(x,y,word):
            if not word:
                return True
            d[x][y]=True

            for i, j in ((x+1, y), (x-1, y), (x,y+1), (x,y-1)):
                if 0<=i<n and 0<=j<m and d[i][j]==False and board[i][j]==word[0]:
                    q=check(i,j,word[1:])
                    if q:return True
            d[x][y]=False
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and check(i, j, word[1:]):
                    return True
        return False
    
                    