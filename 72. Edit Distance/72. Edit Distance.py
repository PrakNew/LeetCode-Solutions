'''
Time Complexity : O(mn)
Space Complexity: O(n)

'''

class Solution:
    def minDistance(self, x, y):
        
        def bottomUp():
            m, n = len(x), len(y)
            T = [[0 for _ in range(n+1)] for _ in range(m+1)]

            for i in range(m+1):
                T[i][0] = i
            for j in range(1, n+1):
                T[0][j] = j

            for i in range(1, m+1):
                for j in range(1, n+1):
                    if x[i-1]==y[j-1]:
                        T[i][j] = T[i-1][j-1]
                    else:
                        T[i][j] = 1 + min(T[i-1][j], T[i][j-1], T[i-1][j-1])

            return T[m][n]
        
        
        def linearSpace():
            m, n = len(x), len(y)
            first = [j for j in range(n+1)]
            
            for i in range(1, m+1):
                second = [0 for _ in range(n+1)]
                second[0] = i
                for j in range(1, n+1):
                    if x[i-1]==y[j-1]:
                        second[j] = first[j-1]
                    else:
                        second[j] = 1 + min(first[j], second[j-1], first[j-1])
                
                first = second[::]
                
            return first[n]
        
        
        return linearSpace()
        
            