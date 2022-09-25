class Solution:
    def openLock(self, deadends, target):
        deadends = set(deadends)
        lock = "0000"
        
        def move(lock):
            res = []
            if lock in deadends:
                return []
            for i in range(4):
                digit = (int(lock[i])+1)%10
                new_lock = lock[:i] + str(digit) + lock[i+1:]
                if new_lock not in deadends:
                    res.append(new_lock)
            
            for i in range(4):
                digit = int(lock[i])-1
                if digit==-1:
                    digit = 9
                new_lock = lock[:i] + str(digit) + lock[i+1:]
                if new_lock not in deadends:
                    res.append(new_lock)
            
            return res
        
        
        queue = [(lock, 0)]
        visited = set()
        
        while queue:
            state, dist = queue.pop(0)
            
            if state==target:
                return dist
            
            for new_state in move(state):
                if new_state not in visited:
                    queue.append((new_state, dist+1))
                    visited.add(new_state)
            
        return -1
        
        