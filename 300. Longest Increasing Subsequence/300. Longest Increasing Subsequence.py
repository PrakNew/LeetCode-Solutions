import bisect
class Solution:
    def lengthOfLIS(self, A):
        if A == []:
            return 0
        
        def quadratic():
            n = len(A)
            dp = [0] * (n)
            for i in range(n):
                for j in range(i):
                    if A[j] < A[i] and dp[j] > dp[i]:
                        dp[i] = dp[j]
                dp[i] += 1
            return max(dp)
        
        def followUp():
            n = len(A)
            dp = [None] * (n)
            size = 0
            for x in A:
                i = bisect.bisect_left(dp, x, 0, size)
                dp[i] = x
                size = max(i+1, size)
            return size
        
        
        return followUp()
        return quadratic()
    