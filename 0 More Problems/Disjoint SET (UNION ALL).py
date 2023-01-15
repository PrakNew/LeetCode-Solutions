l=[(1,2),(2,3),(4,5),(6,7),(5,6),(3,7)]
parent = list(range(8))
def find(n):
    if parent[n]!=n:
        parent[n]=find(parent[n])
    return parent[n]
def union(x,y):
    px,py=find(x),find(y)
    parent[px]=parent[py]
for x,y in l:
    union(x,y)
print(parent)
print(find(1)==find(3))