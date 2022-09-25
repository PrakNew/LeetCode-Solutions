'''
Since we need information from only two rows at any given instance of time, we just maintain two rows instead of 
2-D matrix to compute LCS.


Time complexity : O(mn)
Space complexity : O(n)
'''

def LCS(x, y):
    m, n = len(x), len(y)
    T = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    first = [0 for _ in range(n+1)]
    second = [0 for _ in range(n+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1]==y[j-1]:
                second[j] = first[j-1] + 1
            else:
                second[j] = max(second[j-1], first[j])
        first = second[:]

    return second[n]

