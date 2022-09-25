class Solution:
    def rangeBitwiseAnd(self, m, n):
        
        if m==n:
            return m
        
        def binary(x):
            ans = ""
            while x:
                if x&1:
                    ans += '1'
                else:
                    ans += '0'
                x = x>>1
            return ans[::-1]
                
        binary_m = binary(m)
        binary_n = binary(n)
        
        if len(binary_m)==len(binary_n):
            ans = m
            for i in range(m+1, n+1):
                ans = ans & i
            return ans
        
        return 0