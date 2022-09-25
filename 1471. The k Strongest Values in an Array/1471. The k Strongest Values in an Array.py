class Solution:
    def getStrongest(self, arr, k):
        arr.sort()
        n = len(arr)
        median = arr[(n-1)//2]
        
        res = []
        i = 0
        j = n-1
        for _ in range(k):
            if abs(arr[i]-median) > abs(arr[j]-median):
                res += arr[i],
                i+=1
            elif abs(arr[i]-median) <= abs(arr[j]-median):
                res += arr[j],
                j-=1
        
        return res
            