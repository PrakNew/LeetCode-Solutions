'''
Idea: Bread First Search with HashMap to prune bad paths
'''


import collections

class Solution:
    def minDays(self, n):
        
        ct = 0
        q = collections.deque([(n, 0)])
        dic = collections.defaultdict()
        while q:
            rem, days = q.popleft()
            if rem==1:
                return days + 1
            if rem not in dic:
                dic[rem] = days
            elif rem < 0 or days >= dic[rem]:
                continue
            dic[rem] = days
            if rem % 3 == 0 :
                q.append((rem//3, days + 1))
            if rem % 2 == 0:
                q.append((rem//2, days + 1))
            q.append((rem-1, days + 1))
        return -1
        