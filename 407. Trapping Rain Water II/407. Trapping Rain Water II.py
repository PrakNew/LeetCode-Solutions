import heapq as hq

def trapRainWater(A):
    grid = A
    heap = []
    visited = set()
    max_height = float('-inf')
    
    m, n = len(A), len(A[0])
    
    # insert all boundary elements into heap
    for i in range(m):
        for j in (0, n-1):
            if (i, j) not in visited:
                heap.append((A[i][j], i, j))
                visited.add((i, j))
    
    for j in range(n):
        for i in (0, m-1):
            if (i, j) not in visited:
                heap.append((A[i][j], i, j))
                visited.add((i, j))

    water = 0
    
    hq.heapify(heap)
    
    while heap:
        height, x, y = hq.heappop(heap)
        # print(x, y, water)
        
        max_height = max(max_height, height)
        
        for i, j in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if 0<=i<m and 0<=j<n and (i, j) not in visited:
                if A[i][j] < max_height:
                    water += (max_height - A[i][j])
                    
                hq.heappush(heap, (A[i][j], i, j))
                visited.add((i, j))
                
    return water