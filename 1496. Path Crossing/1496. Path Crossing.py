class Solution:
    def isPathCrossing(self, path):
        hashset = {}
        hashset[(0, 0)] = 1
        x, y = 0, 0
        for ch in path:
            if ch is 'N':
                y += 1
            elif ch is 'E':
                x += 1
            elif ch is 'W':
                x -= 1
            else:
                y -= 1
            if (x, y) in hashset:
                return True
            hashset[(x, y)] = 1
        
        return False
        