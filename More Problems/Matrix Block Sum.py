
if __name__ == '__main__':

    K = 1

    matrix = [ [1,2,3], [4,5,6], [7,8,9] ]
    m, n = len(matrix), len(matrix[0])

    rangeSum = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m):
        for j in range(n):
            rangeSum[i+1][j+1] = rangeSum[i][j+1] + rangeSum[i+1][j] - rangeSum[i][j] + matrix[i][j]
    
    answer = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            r1, c1 = max(0, i-K), max(0, j-K)
            r2, c2 = min(i+K+1, m), min(j+K+1, n)

            answer[i][j] = rangeSum[r2][c2] - rangeSum[r1][c2] - rangeSum[r2][c1] + rangeSum[r1][c1]
    
    print("Answer: ")
    for row in answer:
        print(row)
    
    print()
    