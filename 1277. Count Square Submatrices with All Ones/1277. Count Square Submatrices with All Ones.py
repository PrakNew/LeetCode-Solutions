def countSquares(matrix):
    res = 0 
    m, n = len(matrix), len(matrix[0])
    T = []

    for i in range(len(matrix)):
        T.append(matrix[i][:])

    for i in range(m):
        for j in range(n):
            if i>0 and j>0 and matrix[i][j]==1:
                T[i][j] = min(T[i-1][j], T[i][j-1], T[i-1][j-1]) + 1 
            res += T[i][j]

    return res

# method returns side of largest square submatrix of 1s
def maxSquare(matrix):
    maxSide = 0 
    m, n = len(matrix), len(matrix[0])
    T = []

    for i in range(len(matrix)):
        T.append(matrix[i][:])
    
    for i in range(m):
        for j in range(n):
            if i>0 and j>0 and matrix[i][j]==1:
                T[i][j] = min(T[i-1][j], T[i][j-1], T[i-1][j-1]) + 1 
                maxSide = max(maxSide, T[i][j])
    
    print("Largest side = ", maxSide)
    

if __name__ == '__main__':
    matrix = [
                [0,1,1,1],
                [1,1,1,1],
                [0,1,1,1]
             ]   
    
    print(countSquares(matrix))

    # maxSquare(matrix)