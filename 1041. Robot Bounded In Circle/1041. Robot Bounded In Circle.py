'''
Idea: By limit cycle theory, there are two cases to identify limit cycle theory:
      1. Robot returns to initial position after one cycle
      2. Robot is not north facing after one cycle
      
Time complexity : O(n)
Space complexity: O(1)
'''

class Solution:
    def isRobotBounded(self, instructions):
        n = len(instructions)
        # north, east, south, west
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        pos = 0
        x = y = 0
        for i in range(n):
            if instructions[i]=="L":
                # from north jump to west in array
                pos = (pos+3)%4
            elif instructions[i]=='R':
                # from north jump to east in array
                pos = (pos+1)%4
            else:
                x += directions[pos][0]
                y += directions[pos][1]
        
        return (x==0 and y==0) or pos!=0