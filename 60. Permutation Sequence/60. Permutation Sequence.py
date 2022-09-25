class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        numbers = [i for i in range(1, n+1)]
        k-=1
        
        ans = ""
        
        while n>0:
            n-=1
            index, k = divmod(k, math.factorial(n))
            ans += str(numbers[index])
            numbers.remove(numbers[index])
        
        return ans