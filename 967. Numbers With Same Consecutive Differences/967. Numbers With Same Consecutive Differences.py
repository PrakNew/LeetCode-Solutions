import collections

class Solution:    
    def numsSameConsecDiff(self, n, k):
        
        if n==1:
            return [i for i in range(10)]
        
        res = []
        q = collections.deque()
        for i in range(1, 10):
            q.append((i, n-1))
            
        while q:
            num, digits = q.popleft()
            if digits == 0:
                res += num,
                continue
            dgt = num % 10
            if 0<=(dgt-k)<=9:
                q.append((num*10 + dgt-k, digits-1))
            if k!=0 and 0<=(dgt+k)<=9:
                q.append((num*10 + dgt+k, digits-1))
        
        return res