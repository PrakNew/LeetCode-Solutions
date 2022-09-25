class Solution:
    def fourSum(self, A, target):
        
        def findNSum(l, r, N, target, result, results):
            
            if N<2 or (r-l+1)<N or target < (A[l]*N) or target > (A[r] * N):
                return
            
            elif N==2:
                while l<r:
                    curr_sum = A[l] + A[r]
                    
                    if curr_sum == target:
                        results.append(result + [A[l]] + [A[r]])
                        l+=1
                        while l<r and A[l] == A[l-1]:
                            l+=1
                    
                    elif curr_sum > target:
                        r-=1
                    
                    else:
                        l+=1
            
            else:
                for i in range(l, r+1):
                    if i==l or (i>l and A[i]!=A[i-1]):
                        findNSum(i+1, r, N-1, target - A[i], result + [A[i]], results)
            
        
        A.sort()
        results = []
        findNSum(0, len(A)-1, 4, target, [], results)
        return results
        