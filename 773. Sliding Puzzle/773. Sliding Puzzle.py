def findZero(grid):
    for i in range(2):
        for j in range(3):
            if grid[i][j]==0:
                return i, j

def slidingPuzzle(grid):
    q = [(grid, 0)]
    visited = set(str([grid]))

    while q:
        state, move = q.pop(0)

        if state==[[1,2,3],[4,5,0]]:
            return move
        
        x, y = findZero(state)

        # swap it with 4 neighbors
        for i, j in ((x-1, y), (x, y-1), (x, y+1), (x+1, y)):
            if 0<=i<2 and 0<=j<3:
                new_state = [x[:] for x in state]
                new_state[x][y], new_state[i][j] = new_state[i][j], new_state[x][y]
                if str(new_state) not in visited:
                    visited.add(str(new_state))
                    q.append((new_state, move+1))

    return -1
        
board = [[3,2,4],[1,5,0]]
print("Minimum moves = ", slidingPuzzle(board))