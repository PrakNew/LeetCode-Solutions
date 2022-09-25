def rotateMatrix(matrix):
    N = len(matrix)

    for i in range(int(N/2)):
        for j in range(N):
            matrix[i][j], matrix[N-i-1][j] = matrix[N-i-1][j], matrix[i][j]
    
    for i in range(N):
        for j in range(N):
            if i<j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(N):
        print(matrix[i])

matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]  ]

rotateMatrix(matrix)