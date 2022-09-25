"""
Idea: HashMaps

Time complexity: O(n log n)
Space complexity: O(n)
"""

import collections

class Solution:
    def countBalls(self, lowLimit, highLimit):
        def getSum(x):
            ans = 0
            while x:
                ans += (x%10)
                x//=10
            return ans
            
        mp = collections.defaultdict(int)
        res = 0
        for x in range(lowLimit, highLimit+1):
            bag = getSum(x)
            mp[bag] += 1
            res = max(res, mp[bag])
        
        return res
        