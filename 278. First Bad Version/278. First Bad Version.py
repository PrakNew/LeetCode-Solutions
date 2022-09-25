'''
Time complexity : O(log n)
Space complexity: O(1)
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        
        while l<r:
            mid = (l+r)>>1
            if not isBadVersion(mid):
                l = mid+1
            else:
                r = mid
        
        return l
        