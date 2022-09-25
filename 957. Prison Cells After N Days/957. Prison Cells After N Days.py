class Solution:
    def prisonAfterNDays(self, cells, N):
        if not cells or N<=0:
            return cells
        
        def nextDay(cells):
            res = [0] * 8
            for i in range(1, 7):
                if cells[i-1]==cells[i+1]:
                    res[i] = 1
            return res
        
        def toString(cells):
            res = ''
            for ch in cells:
                res += str(ch)
            return res
        
        hashset = {}
        hasCycle = False
        cycle = 0
        
        for i in range(N):
            next = nextDay(cells)
            key = toString(next)
            if key not in hashset:
                hashset[key] = True
                cycle += 1
                
            else:
                hasCycle = True
                break
            cells = next[::]
            
        
        if hasCycle:
            N %= cycle
            for i in range(N):
                cells = nextDay(cells)
        
        return cells
        