def dfs(A, x, y, src, visit):
    visit[x][y] = True
    src += [(x,y)]
    for i, j in [[x-1,y], [x+1,y], [x,y-1], [x,y+1]]:
        if 0<=i<m and 0<=j<n and not visit[i][j] and A[i][j]==1:
            dfs(A, i, j, src, visit)
    
    return src


A = [[0,1],[1,0]]
print("Matrix: ")
m, n = len(A), len(A[0])
for i in range(m):
    print(A[i])

visit = [[False for _ in range(n)] for _ in range(n)]
source = []
target = []
for i in range(m):
    for j in range(n):
        if A[i][j]==1:
            source = dfs(A, i, j, [], visit)
            break 
    if len(source)>0:
        break

print("Source = ", source)

for i in range(m):
    for j in range(n):
        if A[i][j]==1 and not visit[i][j]:
            target = dfs(A, i, j, [], visit)
            break 
    if len(target)>0:
        break

print("Target = ", target)

queue = [(node, 0) for node in source]
visited = set(source)
dist = []

# BFS
while queue:
    node, d = queue.pop(0)
    if node in target:
        dist.append(d-1)
        break
    x, y = node
    for i, j in [[x-1,y], [x+1,y], [x,y-1], [x,y+1]]:
        if 0<=i<m and 0<=j<n and (i,j) not in visited:
            queue.append(((i,j), d+1))
            visited.add((i,j))

print("Distances : ", dist)