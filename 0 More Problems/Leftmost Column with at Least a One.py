'''
Time complexity : O(m+n)
Space complexity: O(1)
'''

class BinaryMatrix(object):
    def get(self, x: int, y: int): 
        pass
    def dimensions(self):
        pass

def leftMostColumnWithOne(self, binaryMatrix):
    m, n = binaryMatrix.dimensions()
    rowSum = {}
    row = 0
    col = n-1
    
    ans = -1
    
    while row<m and col>=0:
        if binaryMatrix.get(row, col)==1:
            ans = col
            col -= 1
        else:
            row += 1
    
    return ans