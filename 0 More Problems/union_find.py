def find(i, root):
    if i != root[i]:
        root[i] = find(root[i], root)
    return root[i]

def uni(x, y, root):
    x, y = find(x, root), find(y, root)
    if x == y: return 0
    root[x] = y
    return 1
root = list(range(n + 1))
