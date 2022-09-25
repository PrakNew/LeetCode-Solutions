def merge(A, B):
    ans = []
    i = 0
    j = 0

    while i<len(A) and j<len(B):
        
        lo = max(A[i][0], B[j][0])
        hi = min(A[i][1], B[j][1])

        if lo<=hi:
            ans.append([lo, hi])
        
        # discard interval with smallest end time
        if A[i][1] <= B[j][1]:
            i+=1
        else:
            j+=1 
    
    print(ans)


if __name__ == '__main__':

    A = [[0,2],[5,10],[13,23],[24,25]]
    B = [[1,5],[8,12],[15,24],[25,26]]

    merge(A, B)