class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n,m=len(grid),len(grid[0])
        l=[0]*m
        for y in range(m):
            x=0
            y1=y
            flag=1
            while x!=n:
                if grid[x][y1]==1 and (y1+1)<m and grid[x][y1+1]!=-1:
                    x += 1
                    y1=y1+1
                elif grid[x][y1] == -1 and y1 >= 1 and grid[x][y1 - 1] != 1:
                    x += 1
                    y1-=1
                else:
                    flag=-1
                    break
            l[y] = -1 if flag==-1 else y1
        return l
                    