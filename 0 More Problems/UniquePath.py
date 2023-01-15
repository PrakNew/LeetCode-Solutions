# def findStart(grid):
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j]==1:
#                 return i, j

# def isSafe(x, y, grid, visit):
#     N, M = len(grid), len(grid[0])  
#     # print(0<=x<N,0<=y<M, grid[x][y]!=-1, visit[x][y])
#     return 0<=x<N and 0<=y<M and grid[x][y]!=-1 and not visit[x][y]

# def isComplete(path, grid):
#     N, M = len(grid), len(grid[0])  
#     for i in range(N):
#         for j in range(M):
#             if grid[i][j]==0 and path[i][j]!=1:
#                 return False 
#     return True 

# def util(x, y, grid, path, visit, ans = 0):

#     # print(path)
#     N, M = len(grid), len(grid[0])  

#     if not 0<=x<N or not 0<=y<M:
#         return

#     if grid[x][y]==2:
#         path[x][y] = 1
#         if isComplete(path, grid):
#             ans += 1
#             print(ans)
#             # print("\nSolution : ")
#             # for i in range(len(path)):
#             #     print(path[i])
#         return True
    
#     if isSafe(x, y, grid, visit):
#         visit[x][y] = True
#         path[x][y] = 1

#         if 0<=x-1<N and 0<=y<M:
#             util(x-1, y, grid, path, visit, ans)
            
        
#         if 0<=x+1<N and 0<=y<M:
#             util(x+1, y, grid, path, visit, ans)
      
        
#         if 0<=x<N and 0<=y-1<M:
#              util(x, y-1, grid, path, visit, ans)
            
        
#         if 0<=x<N and 0<=y+1<M:
#             util(x, y+1, grid, path, visit, ans)
          
        
#         visit[x][y] = False
#         path[x][y] = 0
#         return False


# def uniquePath(grid):
#     N, M = len(grid), len(grid[0])
#     path = [[0 for _ in range(M)] for _ in range(N)]
#     visit = [[False for _ in range(M)] for _ in range(N)]

#     sx, sy = findStart(grid)
#     ans = 0

#     util(sx, sy, grid, path, visit, ans)

#     print("Ans : ", ans)

# if __name__ == '__main__':
#     grid  = [
#                 [1, 0, 0, 0],
#                 [0, 0, 0, 0],
#                 [0, 0, 2, -1]
#     ]

#     uniquePath(grid)

class Solution:
    def __init__(self):
        self.res = None

    def UniquePath(self, grid):
        self.res = 0
        n, m, empty = len(grid), len(grid[0]), 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    x, y = (i, j)
                if grid[i][j]==2:
                    end = (i, j)
                if grid[i][j]==0:
                    empty += 1
    
        def dfs(x, y, empty):
            if not (0<=x<n and 0<=y<m and grid[x][y]>=0):
                return 
            
            if (x, y) == end:
                # print("Here")
                # print(empty)
                self.res += empty==0
                # print(empty)
                return
            
            # marking the cell as visited
            grid[x][y] = -2

            dfs(x, y+1, empty-1)
            dfs(x, y-1, empty-1)
            dfs(x+1, y, empty-1)
            dfs(x-1, y, empty-1)

            # backtrack
            grid[x][y] = 0

        dfs(x, y, empty+1)
        return self.res

soln = Solution()

grid  = [
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 2, -1]
]

print("Answer : ", soln.UniquePath(grid))