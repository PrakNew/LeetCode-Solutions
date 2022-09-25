class Solution:
    def uniquePaths(self, m, n):
        if m==1:
            return 1
        
        first = [1]*n
        second = [0]*n
        
        for i in range(1, m):
            second[0] = 1 # first column is always 1
            for j in range(1, n):
                second[j] = first[j] + second[j-1]
            first = second
        
        return second[-1]