'''Sliding window direct implementation'''
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        d=Counter()
        cnt=0
        for r in range(len(fruits)):
            d[fruits[r]]+=1
            while len(d)==3:
                d[fruits[l]]-=1
                if not d[fruits[l]]:
                    del d[fruits[l]]
                l+=1
            cnt=max(cnt,r-l+1)
        return cnt


"""
Idea: Sliding window

Time complexity : O(n)
Space complexity: O(n)
"""

import collections

class Solution:
    def totalFruit(self, A):
        n = len(A)
        left = 0
        res = 0
        baskets = collections.defaultdict(int)
        for right in range(n):
            baskets[A[right]] += 1
            while len(baskets) > 2:
                if baskets[A[left]] == 1:
                    del baskets[A[left]]
                else:
                    baskets[A[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res
                
        