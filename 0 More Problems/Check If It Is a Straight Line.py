'''
Time complexity : O(n)
Space complexity: O(1)
'''

class Solution:
    def checkStraightLine(self, coordinates):
        
        # Equation of line: y = mx + c 
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[-1]
        
        # m = (y2-y1)/(x2-x1)
        if x2!=x1:      # slope is not infinity
            m = (y2-y1)/(x2-x1)
            
            # c = y - mx
            c = y1 - m*x1
            
            for i in range(1, len(coordinates)-1):
                x, y = coordinates[i]
                if y != m*x + c:
                    return False
        
        else:       # slope is infinity
            for i in range(1, len(coordinates)-1):
                if coordinates[i][0]!=x1:
                    return False

        
        return True
            