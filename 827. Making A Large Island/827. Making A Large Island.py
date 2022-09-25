def largestIsland(grid):
    m, n = len(grid), len(grid[0])
    
    colors = {0:0}
    
    def dfs(x, y, color):
        grid[x][y] = color
        visited.add((x, y))
        
        for i, j in ((x-1, y), (x+1, y), (x, y-1), (x,y+1)):
            if 0<=i<m and 0<=j<n and (i, j) not in visited and grid[i][j]==1:
                dfs(i, j, color)
    
    visited = set()
    color = 2
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1 and (i, j) not in visited:
                dfs(i, j, color)
                color+=1
    
    # for i in range(m):
    #     print(grid[i])

    for i in range(m):
        for j in range(n):
            if grid[i][j]!=0:
                if grid[i][j] not in colors:
                    colors[grid[i][j]] = 0
                colors[grid[i][j]] += 1
    
    # print(colors)
                
    max_area = float('-inf')
    for i in range(m):
        for j in range(n):
            if grid[i][j]==0:
                neighbors = set()
                # print(i, j, end = ' ')
                left, top, bottom, right = 0, 0, 0, 0
                if i-1>=0:
                    # print(",top = ", grid[i-1][j], end = ' ')
                    neighbors.add(grid[i-1][j])
                    top = colors[grid[i-1][j]]
                if i+1<m:
                    # print(", bottom = ", grid[i+1][j], end = ' ')
                    neighbors.add(grid[i+1][j])
                    bottom = colors[grid[i+1][j]]
                if j-1>=0:
                    # print(",left = ", grid[i][j-1], end = ' ')
                    left = colors[grid[i][j-1]]
                    neighbors.add(grid[i][j-1])
                if j+1<n:
                    # print(",right = ", grid[i][j+1], end = ' ')
                    right = colors[grid[i][j+1]]
                    neighbors.add(grid[i][j+1])
                # print()
                # print(i, j, left, top, right, bottom)
                area = 1
                for color in neighbors:
                    area+=colors[color]
                max_area = max(area, max_area)
    
    if max_area==float('-inf'):
        # print("FH")
        return max(colors.values())
    
    return max_area
        