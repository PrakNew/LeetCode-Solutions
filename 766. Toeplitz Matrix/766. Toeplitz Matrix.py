class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n,m=len(matrix),len(matrix[0])
        for x in range(1,n):
            for y in range(1,m):
                if matrix[x][y]!=matrix[x-1][y-1]:
                    return False
        return True
        