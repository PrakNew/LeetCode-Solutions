"""
Idea: Permutation graph: Generate a positions array recording the current position of each person. 
    For each couple check if they are in correct position, else swap with the correct position.

Time complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def minSwapsCouples(self, row):
        
        def swap(position, x, y):
            temp = row[x]
            row[x] = row[y]
            row[y] = temp
            position[row[x]] = x
            position[row[y]] = y
            
        n = len(row)>>1
        position = {}
        res = 0
        
        for i, x in enumerate(row):
            position[x] = i
        
        for group in range(n):
            pos1, pos2 = (group<<1), (group<<1) + 1
            p1 = row[pos1]
            p2 = row[pos2]
            
            if (p1 & 1 == 0 and p2 != p1 + 1) or (p1 & 1 and p2 != p1 - 1):
                res += 1
                target_pos = position[p1 - 1] if p1 & 1 else position[p1 + 1]
                swap(position, pos2, target_pos)
        
        return res
        