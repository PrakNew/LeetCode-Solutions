def pacificAtlantic (grid):
    if len(grid)==0:
        return []
    
    res = []
    m, n = len(grid), len(grid[0])
    
    lookup = [["" for _ in range(n)] for _ in range(m)]
    P = [[None for _ in range(n)] for _ in range(m)]
    A = [[None for _ in range(n)] for _ in range(m)]
    
    # cells touching pacific
    visitedP = set()
    qP = []
    for i in range(m):
        P[i][0] = True
        qP.append((grid[i][0], i, 0))
        visitedP.add((i, 0))
    for j in range(1, n):
        P[0][j] = True
        qP.append((grid[0][j], 0, j))
        visitedP.add((0, j))
    
    # cells touching Atlantic
    visitedA = set()
    qA = []
    for i in range(m):
        A[i][n-1] = True
        qA.append((grid[i][n-1], i, n-1))
        visitedA.add((i, n-1))
    for j in range(n-1):
        A[m-1][j] = True
        qA.append((grid[m-1][j], m-1, j))
        visitedA.add((m-1, j))
    
    # do BFS and update their neighbors

    while qA:
        node, x, y = qA.pop(0)
        
        for i, j in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if 0<=i<m and 0<=j<n and (i, j) not in visitedA and grid[i][j]>=grid[x][y]:
                A[i][j] = True
                visitedA.add((i, j))
                qA.append((grid[i][j], i, j))
                
    while qP:
        node, x, y = qP.pop(0)
        
        for i, j in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if 0<=i<m and 0<=j<n and (i, j) not in visitedP and grid[i][j]>=grid[x][y]:
                P[i][j] = True
                visitedP.add((i, j))
                qP.append((grid[i][j], i, j))
    
    res = []
    for i in range(m):
        for j in range(n):
            if P[i][j] and A[i][j]: # a cell is reaching both atlantic and pacific
                res.append([i,j])
    
    return res